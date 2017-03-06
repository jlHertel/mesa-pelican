# Mesa Pelican
A simple port of the [mesa3d.org](mesa3d.org) website from HTML to Markdown.
This repository is using a wordpress theme called nisarg that I've ported to pelican too.

## Instalation
To use this repository you need to have the latest [Python](https://www.python.org/) and [pelican](http://docs.getpelican.com/en/stable/install.html) software installed.

## View the generated site
After everything is installed, simply issue:

    cd cloned_repository_folder
    pelican

If everything is setup correctly, this will create a folder called `output` with all the website content. Note that right now the website is using a web rootFolder of `/`. If you want to publish the website at a website, say `www.example.com/mesa` you need to change the property `SITEURL` in the file `pelicanconf.py` to `SITEURL = 'www.example.com/mesa'`.

To view the website at local machine you can start the local python server.
For python 2:

    cd output
    python -m SimpleHTTPServer

For python 3:

    cd output
    python -m http.server


