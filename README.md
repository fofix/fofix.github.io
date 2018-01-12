Frets on Fire X: website
========================

This repository contains the source code of our website:

- branch ``sources``: source code, pages and blog of the pelican website
- branch ``master``: generated HTML (by Travis).


All Pull Requests should be merged in the ``sources`` branch.


How to build
------------

This website is generated with [Pelican](https://blog.getpelican.com/) and the [Flex](http://flex.alxd.me) theme.

To test this website, you should use the following:

    pip install -r requirements.txt
    make devserver

Once you are done testing your changes, you should stop the development server via:

    ./develop_server.sh stop
