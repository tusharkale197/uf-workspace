
from scipy.misc.pilutil import imread

import numpy as np
import matplotlib.pyplot as plt
import skimage


def graham_schmidt(basis):
    """
    :param basis
    :return: orthogonal basis
    """
    try:
        ortho_basis = list()
        count = 0
        for row in basis:

            if count == 0:
                basis_vect = row
                count = count + 1
                ortho_basis.append(basis_vect)
            else:
                temp_vect = row
                for vect in ortho_basis:
                    temp_vect = temp_vect - ((np.dot(row, vect)/np.dot(vect, vect)) * vect)
                ortho_basis.append(temp_vect)
        return ortho_basis

    except Exception as exc:
        raise exc


if __name__ == '__main__':

    # 1. Load the hendrix_final.png image and extract the R, G and B channels.
    read_image = imread("hendrix_final.png", mode="RGB")

    # 1.1 Convert each channel image to double precision.
    read_image = skimage.img_as_float(read_image)

    # 1.2 Extract R, G and B channels
    r_chan = read_image[:, :, 0]

    orthogonal_basis = graham_schmidt(r_chan)
