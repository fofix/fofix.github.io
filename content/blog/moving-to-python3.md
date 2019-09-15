title: Moving to Python 3
date: 2019-09-15
category: general
tags: general, python3
slug: moving-to-python3


## Python 3

Python 2 will reach its end of life in [01/01/2020](https://pythonclock.org). This means we will need to move our code to Python 3.

This work already began, and an issue was opened [#110](https://github.com/fofix/fofix/issues/110).

However, this is not an easy task for us to move to Python 3 because:

- we have few _unit tests_ to be sure we don't break everything
- we have some _rewrite modules_ that we need to replace with dependencies:

    - `fofix.core.Collada` (issue [#11](https://github.com/fofix/fofix/issues/11))
    - `fofix.core.LinedConfigParser` (PR [#203](https://github.com/fofix/fofix/pull/203)).


Furthermore, we have the same work to do in Fretwork (issue [#57](https://github.com/fofix/fretwork/issues/57)).


## Planning

Before moving FoFiX to Python 3, we need to do some things:

- in Fretwork:

    - releasing Fretwork 1.0
    - writing max unittests for Fretwork
    - moving Fretwork to Python 3
    - releasing Fretwork 2.0

- in FoFiX:

    - removing `fofix.core.LinedConfigParser`
    - replacing `fofix.core.Collada`
    - releasing FoFiX 4.0
    - writing max unittests for FoFiX
    - moving FoFiX to Python 3
    - releasing FoFiX 5.0

This list may be not complete, but it gives an idea of the remaining work.

So, for now, Python 3 is planned for **Fretwork 2.0** and **FoFiX 5.0**.
