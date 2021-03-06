Title: Compilation and Installation using Autoconf
slug: autoconf

1. [Basic Usage][1]
2. [Driver Options][2]
    * [Xlib Driver Options][3]
    * [DRI Driver Options][4]
    * [OSMesa Driver Options][5]


## <a name="basic"></a>1. Basic Usage

The autoconf generated configure script can be used to guess your
platform and change various options for building Mesa. To use the
configure script, type:

    :::bash
    ./configure

To see a short description of all the options, type ```./configure
--help```. If you are using a development snapshot and the configure
script does not exist, type ```./autogen.sh``` to generate it
first. If you know the options you want to pass to
```configure```, you can pass them to ```autogen.sh```. It
will run ```configure``` with these options after it is
generated. Once you have run ```configure``` and set the options
to your preference, type:

    :::bash
    make

This will produce libGL.so and/or several other libraries depending on the
options you have chosen. Later, if you want to rebuild for a different
configuration run ```make realclean``` before rebuilding.

Some of the generic autoconf options are used with Mesa:

--prefix=PREFIX
:   This is the root directory where
    files will be installed by ```make install```. The default is
    ```usr/local```.

--exec-prefix=EPREFIX
:   This is the root directory
    where architecture-dependent files will be installed. In Mesa, this is
    only used to derive the directory for the libraries. The default is
    ```${prefix}```.

--libdir=LIBDIR
:   This option specifies the directory
    where the GL libraries will be installed. The default is
    ```${exec_prefix}/lib```. It also serves as the name of the
    library staging area in the source tree. For instance, if the option
    ```--libdir=/usr/local/lib64``` is used, the libraries will be
    created in a ```lib64``` directory at the top of the Mesa source
    tree.

--sysconfdir=DIR
:   This option specifies the directory where the configuration
    files will be installed. The default is ```${prefix}/etc```.
    Currently there's only one config file provided when dri drivers are
    enabled - it's ```drirc```.

--enable-static, --disable-shared
:   By default, Mesa
    will build shared libraries. Either of these options will force static
    libraries to be built. It is not currently possible to build static and
    shared libraries in a single pass.

CC, CFLAGS, CXX, CXXFLAGS
:   These environment variables
    control the C and C++ compilers used during the build. By default,
    ```gcc``` and ```g++``` are used and the debug/optimisation
    level is left unchanged.

LDFLAGS
:   An environment variable specifying flags to
    pass when linking programs. These should be empty and
    ```PKG_CONFIG_PATH``` is recommended to be used instead. If needed
    it can be used to direct the linker to use libraries in nonstandard
    directories. For example, ```LDFLAGS="-L/usr/X11R6/lib"```.

PKG_CONFIG_PATH
:   The ```pkg-config``` utility is a hard requirement for configuring and
    building mesa. It is used to search for external libraries
    on the system. This environment variable is used to control the search
    path for ```pkg-config```. For instance, setting
    ```PKG_CONFIG_PATH=/usr/X11R6/lib/pkgconfig``` will search for
    package metadata in ```/usr/X11R6``` before the standard
    directories.

There are also a few general options for altering the Mesa build:

--enable-debug
:   This option will set the compiler debug/optimisation levels (if the user
    hasn't already set them via the CFLAGS/CXXFLAGS) and macros to aid in
    debugging the Mesa libraries. Note that enabling this option can lead to noticeable loss of performance.

--disable-asm
:   There are assembly routines
    available for a few architectures. These will be used by default if
    one of these architectures is detected. This option ensures that
    assembly will not be used.

--build=
--host=
:   By default, the build will compile code for the architecture that
    it's running on. In order to build cross-compile Mesa on a x86-64 machine
    that is to run on a i686, one would need to set the options to:

    ```--build=x86_64-pc-linux-gnu --host=i686-pc-linux-gnu```

    Note that these can vary from distribution to distribution. For more
    information check with the 
    [autoconf manual][6].
    Note that you will need to correctly set ```PKG_CONFIG_PATH``` as well.

    In some cases a single compiler is capable of handling both architectures
    (multilib) in that case one would need to set the ```CC,CXX``` variables
    appending the correct machine options. Seek your compiler documentation for
    further information - [gcc machine dependent options][7]

    In addition to specifying correct ```PKG_CONFIG_PATH``` for the target 
    architecture, the following should be sufficient to configure multilib Mesa

    ```./configure CC="gcc -m32" CXX="g++ -m32" --build=x86_64-pc-linux-gnu --host=i686-pc-linux-gnu ...```


## <a name="driver"></a>2. GL Driver Options

There are several different driver modes that Mesa can use. These are
described in more detail in the <a href="install.html">basic
installation instructions</a>. The Mesa driver is controlled through the
configure options ```--enable-glx``` and ```--enable-osmesa```


### <a name="xlib"></a>Xlib

It uses Xlib as a software renderer to do all rendering. It corresponds
to the option ```--enable-glx=xlib``` or ```--enable-glx=gallium-xlib```.


### <a name="dri"></a>DRI

This mode uses the DRI hardware drivers for
accelerated OpenGL rendering. To enable use ```--enable-glx=dri
--enable-dri```.

--with-dri-driverdir=DIR
:   This option specifies the
    location the DRI drivers will be installed to and the location libGL
    will search for DRI drivers. The default is ```${libdir}/dri```.

--with-dri-drivers=DRIVER,DRIVER,...
:   This option
    allows a specific set of DRI drivers to be built. For example,
    ```--with-dri-drivers="swrast,i965,radeon,nouveau"```. By
    default, the drivers will be chosen depending on the target platform.
    See the directory ```src/mesa/drivers/dri``` in the source tree
    for available drivers. Beware that the swrast DRI driver is used by both
    libGL and the X.Org xserver GLX module to do software rendering, so you
    may run into problems if it is not available.

<!-- This explanation might be totally bogus. Kristian? -->
--disable-driglx-direct
:   Disable direct rendering in
    GLX. Normally, direct hardware rendering through the DRI drivers and
    indirect software rendering are enabled in GLX. This option disables
    direct rendering entirely. It can be useful on architectures where
    kernel DRM modules are not available.

--enable-glx-tls
:   Enable Thread Local Storage (TLS) in GLX.

--with-expat=DIR
:   **DEPRECATED**, use ```PKG_CONFIG_PATH``` instead.
    The DRI-enabled libGL uses expat to
    parse the DRI configuration files in ```${sysconfdir}/drirc``` and
    ```~/.drirc```. This option allows a specific expat installation
    to be used. For example, ```--with-expat=/usr/local``` will
    search for expat headers and libraries in ```/usr/local/include```
    and ```/usr/local/lib```, respectively.


### <a name="osmesa"></a>OSMesa

No libGL is built in this
mode. Instead, the driver code is built into the Off-Screen Mesa
(OSMesa) library. See the [Off-Screen Rendering](osmesa.html)
page for more details.  It corresponds to the option
```--enable-osmesa```.

--with-osmesa-bits=BITS
:   This option allows the size
    of the color channel in bits to be specified. By default, an 8-bit
    channel will be used, and the driver will be named libOSMesa. Other
    options are 16- and 32-bit color channels, which will add the bit size
    to the library name. For example, ```--with-osmesa-bits=16```
    will create the libOSMesa16 library with a 16-bit color channel.


## <a name="library"></a>3. Library Options

The configure script provides more fine grained control over the libraries
that will be built.

[1]: #basic
[2]: #driver
[3]: #xlib
[4]: #dri
[5]: #osmesa
[6]: https://www.gnu.org/savannah-checkouts/gnu/autoconf/manual/autoconf-2.69/html_node/Specifying-Target-Triplets.html
[7]: https://gcc.gnu.org/onlinedocs/gcc/Submodel-Options.html