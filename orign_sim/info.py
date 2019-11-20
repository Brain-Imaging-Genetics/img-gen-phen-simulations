# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Base module variables
"""

__author__ = 'ORIGN Sim developers'
__copyright__ = 'Copyright 2019, ORIGN Sim developers'
__credits__ = ['Jean-Baptiste Poline']
__license__ = '3-clause BSD'
__version__ = '0.0.0'
__maintainer__ = 'Jean-Baptiste Poline'
__email__ = 'jbpoline@gmail.com'
__status__ = 'Prototype'
__url__ = 'https://github.com/Brain-Imaging-Genetics/img-gen-phen-simulations'
__packagename__ = 'orign_sim'
__description__ = ('Open Reproducible Imaging Genetics Neuroscience '
                   '(ORIGN) simulations.')
__longdesc__ = ('To do.')

DOWNLOAD_URL = (
    'https://github.com/Brain-Imaging-Genetics/{name}/archive/{ver}.tar.gz'.format(
        name=__packagename__, ver=__version__))

REQUIRES = [
    'numpy >=1.14',
    'scikit-learn',
    'nilearn',
    'nibabel>=2.1.0',
    'nipy @ git+https://github.com/alexprz/nipy.git@ef3d245c28ceb015d7465fb29d63d0cee0fa6038',
    'scipy',
    'pandas',
    'matplotlib'
]

# Supported Python versions using PEP 440 version specifiers
# Should match the same set of Python versions as classifiers
PYTHON_REQUIRES = ">=3.5"

# Package classifiers
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
]
