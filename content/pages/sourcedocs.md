Title: Source Code Documentation
slug: sourcedocs

[Doxygen][1]
is used to automatically
produce cross-referenced documentation from the Mesa source code.

The Doxygen configuration files and generated files are not included
in the normal Mesa distribution (they're very large).
To generate Doxygen documentation, download Mesa from git, change to
the ```doxygen``` directory and run ```make```.

For an example of Doxygen usage in Mesa, see a recent source file
such as [bufferobj.c][2].

If you're reading this page from your local copy of Mesa, and have
run the doxygen scripts, you can read the documentation
[here][3]

Gallium is also documented using Sphinx. The generated output can be found
[on Gallium.ReadTheDocs.io][4].

[1]: http://www.doxygen.org
[2]: https://cgit.freedesktop.org/mesa/mesa/tree/src/mesa/main/bufferobj.c
[3]: ../doxygen/main/index.html
[4]: https://gallium.readthedocs.io