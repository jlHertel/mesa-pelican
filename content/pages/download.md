Title: Downloading
slug: download

Primary Mesa download site: [ftp.freedesktop.org](ftp://ftp.freedesktop.org/pub/mesa/) (FTP)
or [mesa.freedesktop.org](https://mesa.freedesktop.org/archive/) (HTTP).


Starting with the first release of 2017, Mesa's version scheme is
year-based. Filenames are in the form <tt>mesa-Y.N.P.tar.gz</tt>, where
<tt>Y</tt> is the year (two digits), <tt>N</tt> is an incremental number
(starting at 0) and <tt>P</tt> is the patch number (0 for the first
release, 1 for the first patch after that).


When a new release is coming, release candidates (betas) may be found
in the same directory, and are recognisable by the
<tt>mesa-Y.N.P-<b>rc</b>X.tar.gz</tt> filename.

#Unpacking

Mesa releases are available in two formats: <tt>.tar.xz</tt> and <tt>.tar.gz</tt>.

To unpack the tarball:

    :::bash
    tar xf mesa-Y.N.P.tar.xz

or

    :::bash
    tar xf mesa-Y.N.P.tar.gz


##Contents

After unpacking you'll have these files and directories (among others):

    :::text
    autogen.sh  - Autoconf script for *nix systems
    scons/      - SCons script for Windows builds
    include/    - GL header (include) files
    bin/        - shell scripts for making shared libraries, etc
    docs/       - documentation
    src/        - source code for libraries
    src/mesa    - sources for the main Mesa library and device drivers
    src/gallium - sources for Gallium and Gallium drivers
    src/glx     - sources for building libGL with full GLX and DRI support


Proceed to the [compilation and installation instructions](install.html).

#Demos, GLUT, and GLU

A package of SGI's GLU library is available [here](ftp://ftp.freedesktop.org/pub/mesa/glu/)

A package of Mark Kilgard's GLUT library is available [here](ftp://ftp.freedesktop.org/pub/mesa/glut/)

The Mesa demos collection is available [here](ftp://ftp.freedesktop.org/pub/mesa/demos/)

In the past, GLUT, GLU and the Mesa demos were released in conjunction with
Mesa releases.  But since GLUT, GLU and the demos change infrequently, they
were split off into their own git repositories:
[GLUT](https://cgit.freedesktop.org/mesa/glut/),
[GLU](https://cgit.freedesktop.org/mesa/glu/) and
[Demos](https://cgit.freedesktop.org/mesa/demos/).

