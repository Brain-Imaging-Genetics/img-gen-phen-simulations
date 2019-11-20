# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

import nilearn
import numpy as np
import nibabel as nib
from scipy.stats import uniform
from scipy.ndimage import filters
from nilearn.datasets import neurovault


def generate_image(fwhm=2):
    """
    Parameters
    ----------
    fwhm : int
        The desired FWHM for the Gaussian kernel
        used in smoothing a uniform RVS

    Returns
    -------
    simg : nibabel.nifti1.Nifti1Image
        A Nifti image with smooth uniform noise
    """
    # Load generic neurovault image
    neurovault_entry = neurovault.fetch_neurovault_auditory_computation_task()
    img_path = neurovault_entry.images
    img = nib.load(img_path.pop())

    # Generate uniform, gaussian noise
    rv = uniform.rvs(size=np.array(img.shape))
    sigma = fwhm / np.sqrt(8 * np.log(2))
    srv = filters.gaussian_filter(rv, sigma=sigma)

    # Add generated noise to the neurovault image
    new_data = img.get_fdata() + srv
    simg = nilearn.image.new_img_like(img, new_data)

    return simg
