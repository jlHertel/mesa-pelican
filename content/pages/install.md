Title: Compiling and Installing
slug: install


1. <a href="#prereq-general">Prerequisites for building</a>
  * <a href="#prereq-general">General prerequisites</a>
  * <a href="#prereq-dri">For DRI and hardware acceleration</a>
2. <a href="#autoconf">Building with autoconf (Linux/Unix/X11)</a>
3. <a href="#scons">Building with SCons (Windows/Linux)</a>
4. <a href="#android">Building with AOSP (Android)</a>
5. <a href="#libs">Library Information</a>
6. <a href="#pkg-config">Building OpenGL programs with pkg-config</a>

#<a name="prereq-general"></a>1. Prerequisites for building

##1.1 General

Build system.

* Autoconf is required when building on *nix platforms.
* [SCons](http://www.scons.org/) is required for building on
Windows and optional for Linux (it's an alternative to autoconf/automake.)
* Android Build system when building as native Android component. Autoconf
is used when building ARC.

The following compilers are known to work, if you know of others or you're
willing to maintain support for other compiler get in touch.

* GCC 4.2.0 or later (some parts of Mesa may require later versions)
* clang - exact minimum requirement is currently unknown.
* Microsoft Visual Studio 2013 Update 4 or later is required, for building on Windows.

Third party/extra tools.

**Note**: These should not be required, when building from a release tarball. If
you think you've spotted a bug let developers know by filing a [bug report](bugs.html).


* [Python](https://www.python.org/) - Python is required.
Version 2.6.4 or later should work.

* [Python Mako module](http://www.makotemplates.org/) -
Python Mako module is required. Version 0.3.4 or later should work.

* lex / yacc - for building the Mesa IR and GLSL compiler.<br>
   On Linux systems, flex and bison versions 2.5.35 and 2.4.1, respectively, (or later) should work.
   On Windows with MinGW, install flex and bison with:<br>
   ```mingw-get install msys-flex msys-bison```<br>
   For MSVC on Windows, install [Win flex-bison](http://winflexbison.sourceforge.net/).

**Note**: Some versions can be buggy (eg. flex 2.6.2) so do try others if things fail.

###<a name="prereq-dri"></a>1.2 Requirements

The requirements depends on the features selected at configure stage.
Check/install the respective -devel package as prompted by the configure error
message.

Here are some common ways to retrieve most/all of the dependencies based on
the packaging tool used by your distro.

    :::bash
    zypper source-install --build-deps-only Mesa # openSUSE/SLED/SLES
    yum-builddep mesa # yum Fedora, OpenSuse(?)
    dnf builddep mesa # dnf Fedora
    apt-get build-dep mesa # Debian and derivatives
    ... # others

#<a name="autoconf"></a>2. Building with autoconf (Linux/Unix/X11)

The primary method to build Mesa on Unix systems is with autoconf.

The general approach is the standard:

    :::bash
    ./configure
    make
    sudo make install

But please read the [detailed autoconf instructions](autoconf.html) for more details.


#<a name="scons"></a>3. Building with SCons (Windows/Linux)

To build Mesa with SCons on Linux or Windows do

    :::bash
    scons


The build output will be placed in
build/*platform*-*machine*-*debug*/..., where *platform* is for
example linux or windows, *machine* is x86 or x86_64, optionally followed
by -debug for debug builds.


To build Mesa with SCons for Windows on Linux using the MinGW crosscompiler toolchain do

    :::bash
    scons platform=windows toolchain=crossmingw machine=x86 libgl-gdi

This will create:

* build/windows-x86-debug/gallium/targets/libgl-gdi/opengl32.dll &mdash; Mesa + Gallium + softpipe (or llvmpipe), binary compatible with Windows's opengl32.dll

Put them all in the same directory to test them.

Additional information is available in [README.WIN32<](README.WIN32).


#<a name="android"></a>4. Building with AOSP (Android)

Currently one can build Mesa for Android as part of the AOSP project, yet
your experience might vary.

In order to achieve that one should update their local manifest to point to the
upstream repo, set the appropriate BOARD_GPU_DRIVERS and build the
libGLES_mesa library.

FINISHME: Improve on the instructions add references to Rob H repos/Jenkins,
Android-x86 and/or other resources.


#<a name="libs"></a>5. Library Information


When compilation has finished, look in the top-level ```lib/```
(or ```lib64/```) directory.
You'll see a set of library files similar to this:

    :::bash
    lrwxrwxrwx    1 brian    users          10 Mar 26 07:53 libGL.so -> libGL.so.1*
    lrwxrwxrwx    1 brian    users          19 Mar 26 07:53 libGL.so.1 -> libGL.so.1.5.060100*
    -rwxr-xr-x    1 brian    users     3375861 Mar 26 07:53 libGL.so.1.5.060100*
    lrwxrwxrwx    1 brian    users          14 Mar 26 07:53 libOSMesa.so -> libOSMesa.so.6*
    lrwxrwxrwx    1 brian    users          23 Mar 26 07:53 libOSMesa.so.6 -> libOSMesa.so.6.1.060100*
    -rwxr-xr-x    1 brian    users       23871 Mar 26 07:53 libOSMesa.so.6.1.060100*


**libGL** is the main OpenGL library (i.e. Mesa).

**libOSMesa** is the OSMesa (Off-Screen) interface library.

If you built the DRI hardware drivers, you'll also see the DRI drivers:

    :::bash
    -rwxr-xr-x   1 brian users 16895413 Jul 21 12:11 i915_dri.so
    -rwxr-xr-x   1 brian users 16895413 Jul 21 12:11 i965_dri.so
    -rwxr-xr-x   1 brian users 11849858 Jul 21 12:12 r200_dri.so
    -rwxr-xr-x   1 brian users 11757388 Jul 21 12:12 radeon_dri.so

If you built with Gallium support, look in lib/gallium/ for Gallium-based
versions of libGL and device drivers.


#<a name="pkg-config"></a>6. Building OpenGL programs with pkg-config

Running ```make install``` will install package configuration files
for the pkg-config utility.

When compiling your OpenGL application you can use pkg-config to determine
the proper compiler and linker flags.

For example, compiling and linking a GLUT application can be done with:

    :::bash
    gcc `pkg-config --cflags --libs glut` mydemo.c -o mydemo
