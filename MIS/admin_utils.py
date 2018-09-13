import numpy as np

def verify_matrix_transformation(source_matrix, dest_matrix):
    counter = 0
    while True:
        counter_dest = 0
        if counter == 64:
            break
        for i in range(0, 16):
            for j in range(0, 16):
                print ("%s - %s" % (source_matrix[i][j][counter], dest_matrix[counter_dest][0][counter]))
                if source_matrix[i][j][counter] != dest_matrix[counter_dest][0][counter]:
                    print ("Something fishy")
                    return False
                counter_dest = counter_dest+1
        counter = counter + 1
    print ("returning value")
    return True


def frame_image(img, frame_width):
    b = frame_width # border size in pixel
    ny, nx = img.shape[0], img.shape[1] # resolution / number of pixels in x and y
    framed_img = np.zeros((b+ny+b, b+nx+b))
    framed_img[b:-b, b:-b] = img
    return framed_img


def compute_correlation_matrix_old(patches, dimension, total_patches):
    """
    *** INEFFICIENT  Use matplotlib to calculate transpose and do a matrix mult***
    :param patches: ND array of reshaped patches
    :param dimension: dimension of the patches
    :param total_patches: total number of patches
    :return: returns the "dimension by dimension" correlation matrix
    """

    func_tag = "compute_correlation_matrix"
    try:
        correlation_matrix = np.zeros(shape=(dimension, dimension), dtype=int)

        for patch_num in range(0, total_patches):
            for m in range(0, dimension):
                for n in range(0, dimension):
                    correlation_matrix[m][n] = correlation_matrix[m][n] + patches[m, 0, patch_num] * patches[n, 0, patch_num]

        return correlation_matrix
    except Exception as exc:
        print("Exception %s in %s" % (exc, func_tag))
        raise exc