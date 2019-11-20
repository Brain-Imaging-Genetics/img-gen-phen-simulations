#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" orign_sim setup script """


def main():
    """ Install entry-point """
    from io import open
    from os import path as op
    from inspect import getfile, currentframe
    from setuptools import setup, find_packages
    from orign_sim.info import (
        __packagename__,
        __version__,
        __author__,
        __email__,
        __maintainer__,
        __license__,
        __description__,
        __longdesc__,
        __url__,
        DOWNLOAD_URL,
        CLASSIFIERS,
        REQUIRES,
        PYTHON_REQUIRES
    )

    setup(
        name=__packagename__,
        version=__version__,
        description=__description__,
        long_description=__longdesc__,
        author=__author__,
        author_email=__email__,
        maintainer=__maintainer__,
        maintainer_email=__email__,
        url=__url__,
        license=__license__,
        classifiers=CLASSIFIERS,
        download_url=DOWNLOAD_URL,
        # Dependencies handling
        python_requires=PYTHON_REQUIRES,
        install_requires=REQUIRES,
        packages=find_packages(exclude=("tests",)),
        zip_safe=False
    )


if __name__ == '__main__':
    main()
