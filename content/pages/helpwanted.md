Title: Help Wanted / To-Do List
slug: helpwanted

We can always use more help with the Mesa project.
Here are some specific ideas and areas where help would be appreciated:

1. **Driver patching and testing.**
Patches are often posted to the [mesa-dev mailing list][1], but aren't
immediately checked into git because not enough people are testing them.
Just applying patches, testing and reporting back is helpful.

2. **Driver debugging.**
There are plenty of open bugs in the [bug database][2].

3. **Remove aliasing warnings.**
Enable gcc -Wstrict-aliasing=2 -fstrict-aliasing and track down aliasing
issues in the code.

4. **Windows driver building, testing and maintenance.**
Fixing MSVC builds.

5. **Contribute more tests to [Piglit][3].**

6. **Automatic testing.**
It would be great if someone would set up an automated system for grabbing
the latest Mesa code and run tests (such as piglit) then report issues to
the mailing list.

You can find some further To-do lists here:

**Common To-Do lists:**

* [**features.txt**][4] - Status of OpenGL 3.x / 4.x features in Mesa.</li>
* [**MissingFunctionality**][5] - Detailed information about missing OpenGL features.</li>


**Driver specific To-Do lists:**

* [**LLVMpipe**][6] - Software driver using LLVM for runtime code generation.</li>
* [**radeonsi**][7] - Driver for AMD Southern Island.</li>
* [**r600g**][8] - Driver for ATI/AMD R600 - Northern Island.</li>
* [**r300g**][9] - Driver for ATI R300 - R500.</li>
* [**i915g**][10] - Driver for Intel i915/i945.</li>

If you want to do something new in Mesa, first join the Mesa developer's
mailing list.
Then post a message to propose what you want to do, just to make sure
there's no issues.

Anyone is welcome to contribute code to the Mesa project.
By doing so, it's assumed that you agree to the code's licensing terms.

Finally:

1. Try to write high-quality code that follows the existing style.
2. Use uniform indentation, write comments, use meaningful identifiers, etc.
3. Test your code thoroughly.  Include test programs if appropriate.

[1]: https://lists.freedesktop.org/mailman/listinfo/mesa-dev
[2]: https://bugs.freedesktop.org/describecomponents.cgi?product=Mesa
[3]: https://piglit.freedesktop.org/
[4]: https://cgit.freedesktop.org/mesa/mesa/tree/docs/features.txt
[5]: https://dri.freedesktop.org/wiki/MissingFunctionality
[6]: https://cgit.freedesktop.org/mesa/mesa/tree/src/gallium/docs/llvm-todo.txt
[7]: https://dri.freedesktop.org/wiki/RadeonsiToDo
[8]: https://dri.freedesktop.org/wiki/R600ToDo
[9]: https://dri.freedesktop.org/wiki/R300ToDo
[10]: https://cgit.freedesktop.org/mesa/mesa/tree/src/gallium/drivers/i915/TODO