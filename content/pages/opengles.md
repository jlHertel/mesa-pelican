Title: OpenGL ES
slug: opengles

Mesa implements OpenGL ES 1.1 and OpenGL ES 2.0.  More information about
OpenGL ES can be found at [https://www.khronos.org/opengles/][1].

OpenGL ES depends on a working EGL implementation.  Please refer to
[Mesa EGL][2] for more information about EGL.

##Build the Libraries

1. Run ```configure``` with ```--enable-gles1 --enable-gles2``` and enable the Gallium driver for your hardware.
2. Build and install Mesa as usual.

Alternatively, if XCB-DRI2 is installed on the system, one can use
```egl_dri2``` EGL driver with OpenGL|ES-enabled DRI drivers

1. Run ```configure``` with ```--enable-gles1 --enable-gles2```.
2. Build and install Mesa as usual.

Both methods will install libGLESv1_CM, libGLESv2, libEGL, and one or more
EGL drivers for your hardware.

##Run the Demos

There are some demos in ```mesa/demos``` repository.

##Developers

###Dispatch Table

OpenGL ES has an additional indirection when dispatching functions

    :::text
    Mesa:       glFoo() --> _mesa_Foo()
    OpenGL ES:  glFoo() --> _es_Foo() --> _mesa_Foo()

The indirection serves several purposes

* When a function is in Mesa and the type matches, it checks the arguments and calls the Mesa function.
* When a function is in Mesa but the type mismatches, it checks and converts the arguments before calling the Mesa function.
* When a function is not available in Mesa, or accepts arguments that are not available in OpenGL, it provides its own implementation.

Other than the last case, OpenGL ES uses ```APIspec.xml``` to generate functions to check and/or converts the arguments.

[1]: https://www.khronos.org/opengles/
[2]: egl.html