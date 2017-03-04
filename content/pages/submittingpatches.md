Title: Submitting patches
slug: submittingpatches

* [Basic guidelines][1]
* [Patch formatting][2]
* [Testing Patches][3]
* [Mailing Patches][4]
* [Reviewing Patches][5]
* [Nominating a commit for a stable branch][6]
* [Criteria for accepting patches to the stable branch][7]
* [Sending backports for the stable branch][8]
* [Git tips][9]

## <a name="guidelines"></a>Basic guidelines

* Patches should not mix code changes with code formatting changes (except, perhaps, in very trivial cases.)
* Code patches should follow Mesa [coding conventions][10].
* Whenever possible, patches should only effect individual Mesa/Gallium components.
* Patches should never introduce build breaks and should be bisectable (see ```git bisect```)
* Patches should be properly [formatted][2]
* Patches should be sufficiently [tested][3] before submitting.
* Patches should be submitted to [mesa-dev][4] for [review][5] using ```git send-email```.

## <a name="formatting"></a>Patch formatting

* Lines should be limited to 75 characters or less so that git logs displayed in 80-column terminals avoid line wrapping.
Note that git log uses 4 spaces of indentation (4 + 75 < 80).

* The first line should be a short, concise summary of the change prefixed with a module name.  Examples:

        :::text
        mesa: Add support for querying GL_VERTEX_ATTRIB_ARRAY_LONG

        gallium: add PIPE_CAP_DEVICE_RESET_STATUS_QUERY

        i965: Fix missing type in local variable declaration.
        
* Subsequent patch comments should describe the change in more detail, if needed.  For example:

        :::text
        i965: Remove end-of-thread SEND alignment code.
    
        This was present in Eric's initial implementation of the compaction code for Sandybridge (commit 077d01b6).
        There is no documentation saying this is necessary, and removing it causes no regressions in piglit on any platform.

* A "Signed-off-by:" line is not required, but not discouraged either.

* If a patch addresses a bugzilla issue, that should be noted in the patch comment.  For example:

        :::text
        Bugzilla: https://bugs.freedesktop.org/show_bug.cgi?id=89689

* If a patch addresses a issue introduced with earlier commit, that should be noted in the patch comment.  For example:

        :::text
        Fixes: d7b3707c612 "util/disk_cache: use stat() to check if entry is a directory"

* If there have been several revisions to a patch during the review process, they should be noted such as in this example:

        :::text
        st/mesa: add ARB_texture_stencil8 support (v4)
    
        if we support stencil texturing, enable texture_stencil8 there is no requirement to support native S8 for this, the texture can be converted to x24s8 fine.
    
        v2: fold fixes from Marek in:
        a) put S8 last in the list
        b) fix renderable to always test for d/s renderable fixup the texture case to use a stencil only format for picking the format for the texture view.
        v3: hit fallback for getteximage
        v4: put s8 back in front, it shouldn't get picked now (Ilia)

* If someone tested your patch, document it with a line like this:

        :::text
        Tested-by: Joe Hacker <jhacker@foo.com>

* If the patch was reviewed (usually the case) or acked by someone, that should be documented with:

        :::text
        Reviewed-by: Joe Hacker <jhacker@foo.com>
        Acked-by: Joe Hacker <jhacker@foo.com>

* If sending later revision of a patch, add all the tags - ack, r-b, Cc: mesa-stable and/or other.
    This provides reviewers with quick feedback if the patch has already been reviewed.

* In order for your patch to reach the prospective reviewer easier/faster, use the script scripts/get_reviewer.pl to get a list of individuals and include them in the CC list.
    
    Please use common sense and do **not** blindly add everyone.

        :::text
        $ scripts/get_reviewer.pl --help # to get the help screen
        $ scripts/get_reviewer.pl -f src/egl/drivers/dri2/platform_android.c
        Rob Herring <robh@kernel.org> (reviewer:ANDROID EGL SUPPORT,added_lines:188/700=27%,removed_lines:58/283=20%)
        Tomasz Figa <tfiga@chromium.org> (reviewer:ANDROID EGL SUPPORT,authored:12/41=29%,added_lines:308/700=44%,removed_lines:115/283=41%)
        Emil Velikov <emil.l.velikov@gmail.com> (authored:13/41=32%,removed_lines:76/283=27%)


## <a name="testing"></a>Testing Patches

It should go without saying that patches must be tested. In general,do whatever testing is prudent.

You should always run the Mesa test suite before submitting patches.
The test suite can be run using the 'make check' command.
All tests must pass before patches will be accepted, this may mean you have to update the tests themselves.

Whenever possible and applicable, test the patch with [Piglit][11] and/or [dEQP][12] to check for regressions.


## <a name="mailing"></a>Mailing Patches

Patches should be sent to the mesa-dev mailing list for review: [mesa-dev@lists.freedesktop.org][13].
When submitting a patch make sure to use [git send-email][14] rather than attaching patches to emails.
Sending patches as attachments prevents people from being able to provide in-line review comments.

When submitting follow-up patches you can use --in-reply-to to make v2, v3,
etc patches show up as replies to the originals. This usually works well
when you're sending out updates to individual patches (as opposed to
re-sending the whole series). Using --in-reply-to makes
it harder for reviewers to accidentally review old patches.

When submitting follow-up patches you should also login to [patchwork][15]
and change the state of your old patches to Superseded.


## <a name="reviewing"></a>Reviewing Patches

When you've reviewed a patch on the mailing list, please be unambiguous
about your review.  That is, state either

    :::text
    Reviewed-by: Joe Hacker <jhacker@foo.com>

or

    :::text
    Acked-by: Joe Hacker <jhacker@foo.com>

Rather than saying just "LGTM" or "Seems OK".

If small changes are suggested, it's OK to say something like:

    :::text
    With the above fixes, Reviewed-by: Joe Hacker <jhacker@foo.com>

which tells the patch author that the patch can be committed, as long
as the issues are resolved first.


## <a name="nominations"></a>Nominating a commit for a stable branch

There are three ways to nominate a patch for inclusion in the stable branch and release.

*  By adding the Cc: mesa-stable@ tag as described below.
*  Sending the commit ID (as seen in master branch) to the mesa-stable@ mailing list.
*  Forwarding the patch from the mesa-dev@ mailing list.

Note: resending patch identical to one on mesa-dev@ or one that differs only
by the extra mesa-stable@ tag is **not** recommended.


### <a name="thetag"></a>The stable tag

If you want a commit to be applied to a stable branch,
you should add an appropriate note to the commit message.

Here are some examples of such a note:

* CC: <mesa-stable@lists.freedesktop.org>

Simply adding the CC to the mesa-stable list address is adequate to nominate
the commit for all the active stable branches. If the commit is not applicable
for said branch the stable-release manager will reply stating so.

This "CC" syntax for patch nomination will cause patches to automatically be
copied to the mesa-stable@ mailing list when you use "git send-email" to send
patches to the mesa-dev@ mailing list. If you prefer using --suppress-cc that
won't have any negative effect on the patch nomination.

Note: by removing the tag [as the commit is pushed] the patch is
**explicitly** rejected from inclusion in the stable branch(es).

Thus, drop the line **only** if you want to cancel the nomination.


## <a name="criteria"></a>Criteria for accepting patches to the stable branch

Mesa has a designated release manager for each stable branch, and the release
manager is the only developer that should be pushing changes to these branches.
Everyone else should nominate patches using the mechanism described above.

The following rules define which patches are accepted and which are not. The
stable-release manager is also given broad discretion in rejecting patches
that have been nominated.

* Patch must conform with the [Basic guidelines][1]

* Patch must have landed in master first. In case where the original
patch is too large and/or otherwise contradicts with the rules set within, a
backport is appropriate.

* It must not introduce a regression - be that build or runtime wise.

    Note:  If the regression is due to faulty piglit/dEQP/CTS/other test the
latter must be fixed first. A reference to the offending test(s) and
respective fix(es) should be provided in the nominated patch.

* Patch cannot be larger than 100 lines.

* Patches that move code around with no functional change should be rejected.

* Patch must be a bug fix and not a new feature.

    Note: An exception to this rule, are hardware-enabling "features".
For example, [backports][8] of new code to support a newly-developed hardware
product can be accepted if they can be reasonably determined not to have effects on other hardware.

* Patch must be reviewed, For example, the commit message has Reviewed-by,
Signed-off-by, or Tested-by tags from someone but the author.

* Performance patches are considered only if they provide information
about the hardware, program in question and observed improvement.
Use numbers to represent your measurements.

If the patch complies with the rules it will be [cherry-picked][16].
Alternatively the release manager will reply to the patch in question stating why the patch has been
rejected or would request a backport.

A summary of all the picked/rejected patches will be presented in the
[pre-release][17] announcement.

The stable-release manager may at times need to force-push changes to the
stable branches, for example, to drop a previously-picked patch that was later
identified as causing a regression). These force-pushes may cause changes to
be lost from the stable branch if developers push things directly. Consider
yourself warned.


## <a name="backports"></a>Sending backports for the stable branch

By default merge conflicts are resolved by the stable-release manager. In which
case he/she should provide a comment about the changes required, alongside the
```Conflicts``` section. Summary of which will be provided in the
[pre-release][17] announcement.

Developers are interested in sending backports are recommended to use either a
```[BACKPORT #branch]``` subject prefix or provides similar information
within the commit summary.


## <a name="gittips"></a>Git tips

* ```git rebase -i ...``` is your friend. Don't be afraid to use it.

* Apply a fixup to commit FOO.

        :::bash
        git add ...
        git commit --fixup=FOO
        git rebase -i --autosquash ...

* Test for build breakage between patches e.g last 8 commits.

        :::bash
        git rebase -i --exec="make -j4" HEAD~8

* Sets the default mailing address for your repo.

        :::bash
        git config --local sendemail.to mesa-dev@lists.freedesktop.org

*  Add version to subject line of patch series in this case for the last 8 commits before sending.

        :::bash
        git send-email --subject-prefix="PATCH v4" HEAD~8
        git send-email -v4 @~8 # shorter version, inherited from git format-patch

*  Configure git to use the get_reviewer.pl script interactively. Thus you can avoid adding the world to the CC list.

        :::bash
        git config sendemail.cccmd "./scripts/get_reviewer.pl -i"

[1]: #guidelines
[2]: #formatting
[3]: #testing
[4]: #mailing
[5]: #reviewing
[6]: #nominations
[7]: #criteria
[8]: #backports
[9]: #gittips
[10]: codingstyle.html
[11]: https://piglit.freedesktop.org
[12]: https://android.googlesource.com/platform/external/deqp/
[13]: https://lists.freedesktop.org/mailman/listinfo/mesa-dev
[14]: https://git-scm.com/docs/git-send-email
[15]: https://patchwork.freedesktop.org
[16]: releasing.html#pickntest
[17]: releasing.html#prerelease