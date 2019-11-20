# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

from numpy.random import choice

def generate_sex(size=10,
                 probabilities=[0.5, 0.5]):
    """
    Parameters
    ----------
    size : int
        The number of observations to return
    probabilities : np.array
        The relative probability of each sex.
        By default, sexes are assumed to have equal
        probability
    
    Returns
    -------
    np.array
        Phenotype of genders following the
        provided probabilities
    """
    return choice(2, size, p=probabilities)
