from scipy.misc.pilutil import imread
import random
import numpy as np
import matplotlib.pyplot as plt
import webbrowser

# dict to avoid duplicate patches
patch_loc_dict = dict()


def get_random_patches(first_dim, num_patches, dimension):
    """
    Function to get an nd array of random patches from the given image

    :param first_dim: the array from which we need to extract patches
    :param num_patches: The number of patches required
    :param dimension: Size of each patch -> dimension * dimension
    :return: returns an nd array of dimension * dimension patches
    """
    func_tag = "get_random_patches"
    try:
        random_patches = np.zeros(shape=(dimension, dimension, num_patches), dtype=int)
        size_x, size_y = first_dim.shape
        for x in range(0, num_patches):
            offset_x, offset_y = get_random_patch_origin(size_x, size_y, dimension)
            m = 0
            for i in range(offset_x, offset_x+dimension):
                n = 0
                for j in range(offset_y, offset_y+dimension):
                    random_patches[m][n][x] = first_dim[i][j]
                    n = n+1
                m = m+1

        return random_patches
    except Exception as exc:
        print("Exception %s in %s" % (e, func_tag))
        raise exc


def get_random_patch_origin(size_of_x, size_of_y, dimension):
    """
    Function to get the origin (arbitrary location where the dimension*dimension patch starts
    and fits completely in the image dimensions) of a random patch

    :param size_of_x: Number of x values available
    :param size_of_y: Number of y values available
    :param dimension: Size of a patch
    :return: Returns the start and end diagonal elements of a patch
    """
    func_tag = "get_random_patch_origin"
    try:
        limit_x = size_of_x-dimension-1
        limit_y = size_of_y-dimension-1
        while True:
            rand_x = random.randint(0, limit_x)
            rand_y = random.randint(0, limit_y)
            rand_loc = "%s%s" % (rand_x, rand_y)
            if rand_loc in patch_loc_dict:
                continue
            else:
                patch_loc_dict[rand_loc] = 1
                break

        return rand_x, rand_y
    except Exception as exc:
        print("Exception %s in %s" % (exc, func_tag))
        raise exc


def get_reshaped_patch(patches, dimension, num_patches):
    """
    Reshaping the patch into an nd array of dim^2 * 1 patches

    :param patches: ndarray of patches that needs to be reshaped
    :param dimension: dimension of each patch
    :param num_patches: total number of patches
    :return: An nd array of dim^2 * 1 * num_patches
    """
    func_tag = "get_reshaped_patch"
    try:
        reshaped_patches = np.zeros(shape=(dimension*dimension, 1, num_patches), dtype=int)

        for x in range(0, num_patches):
            reshape_array_index = 0
            for m in range(0, dimension):
                for n in range(0, dimension):
                    reshaped_patches[reshape_array_index][0][x] = patches[m][n][x]
                    reshape_array_index = reshape_array_index+1

        return reshaped_patches
    except Exception as exc:
        print("Exception %s in %s" % (exc, func_tag))
        raise exc


def get_reshaped_eigenvectors(patches, dimension, num_patches):
    """
    Function to piece back the dim^2 * 1 nd array into a dim*dim nd array using the same scheme as used by "get_reshaped_patch"

    :param patches: ndarray of patches that needs to be reshaped
    :param dimension: dimension of each patch
    :param num_patches: total number of patches
    :return: An nd array of dim^2 * 1 * num_patches
    """
    func_tag = "get_reshaped_patch"
    try:
        reshaped_eig_vects = np.zeros(shape=(dimension, dimension, num_patches))

        for x in range(0, num_patches):
            reshape_array_index = 0
            for m in range(0, dimension):
                for n in range(0, dimension):
                    reshaped_eig_vects[m][n][x] = patches[reshape_array_index][0][x]
                    reshape_array_index = reshape_array_index+1

        return reshaped_eig_vects

    except Exception as exc:
        print("Exception %s in %s" % (exc, func_tag))
        raise exc


def compute_correlation_matrix(patches, dimension):
    """
    Function to compute the correlation matrix

    :param patches: ND array of reshaped patches
    :param dimension: dimension of the patches
    :return: returns the "dimension by dimension" correlation matrix
    """
    func_tag = "compute_correlation_matrix"
    try:
        correlation_matrix = np.zeros(shape=(dimension, dimension), dtype=int)

        for patch_num in range(0, total_patches):
            correlation_matrix = np.add(correlation_matrix, np.matmul(patches[:, :, patch_num], patches[:, :, patch_num].transpose()))

        return correlation_matrix
    except Exception as exc:
        print("Exception %s in %s" % (exc, func_tag))
        raise exc


def get_top_n_eigenvectors(sorted_eig_values, locator_dict, eigen_vec, cutoff):
    """
    Fuction to return the top n eigenvectors in decreasing order of eigenvalues
    :param sorted_eig_values: List of sorted eigen values
    :param locator_dict: dictionary to locate correct eigenvector
    :param eigen_vec: eigenvectors nd array
    :param cutoff: The number of top values needed
    :return: Returns the ndarray of top n eigenvectors
    """
    func_tag = "get_top_n_eigenvectors"
    try:
        x, y = eigen_vec.shape
        top_eig_vects = np.zeros(shape=(x, 1, cutoff))
        count = 0
        for e_val in sorted_eig_values:
            index = locator_dict[e_val]
            top_eig_vects[:, 0, count] = eigen_vec[:, index]
            count = count + 1
            if count == cutoff:
                break
        return top_eig_vects
    except Exception as exc:
        print("Exception %s in %s" % (exc, func_tag))
        raise exc


def concat_images(m):
    """

    :param m: index of the part of the nd array being concatenated
    :return: a concatenated array of top 64 eigenvectors in the form of an 8*8 grid
    """
    func_tag = "concat_images"
    try:
        img = np.pad(reshaped_eigenvectors[:, :, 8 * m], (1, 1), 'constant', constant_values=0)
        for i in range(1, 8):
            vect_pad = np.pad(reshaped_eigenvectors[:, :, 8 * m + i], (1, 1), 'constant', constant_values=0)
            img = np.concatenate((img, vect_pad), axis=1)
        return img
    except Exception as exc:
        print("Exception %s in %s" % (exc, func_tag))
        raise exc


if __name__ == '__main__':

    total_patches = 1000

    dimension_index = 0

    size_patch = 16
    # 1. Read the image
    read_image = imread("clockwork-angels.jpg", mode="RGB")

    # 2. Pick the first dimension of the image
    chosen_dimension = read_image[:, :, dimension_index]

    # 3. Creating 1000 random 16x16 patches
    rand_pat = get_random_patches(chosen_dimension, total_patches, size_patch)

    # 4.1 Reshaping the patches created above
    reshape_patches = get_reshaped_patch(rand_pat, size_patch, total_patches)

    # 4.2 Computing teh correlation matrix
    corr_mat = compute_correlation_matrix(reshape_patches, 256)

    # 5.1 Computing all eigenvectors of above matrix
    eig_val, eig_vec = np.linalg.eig(corr_mat)

    eig_val_list = eig_val.tolist()

    # 5.2 Sorting the eigenvectors in decreasing order of eigenvalues
    index_dict = dict()
    counter = 0
    for e in eig_val_list:
        index_dict[e] = counter
        counter = counter + 1

    eig_val_list.sort(reverse=True)
    # 5.3 listing the top 64 eigenvalues
    patch_count_cutoff = 64
    print(eig_val_list[:patch_count_cutoff])

    top_eigen_vectors = get_top_n_eigenvectors(eig_val_list, index_dict, eig_vec, patch_count_cutoff)

    # 6.1 Reshaping the 256*1 eigenvectors as 16*16 patches
    reshaped_eigenvectors = get_reshaped_eigenvectors(top_eigen_vectors, size_patch, patch_count_cutoff)

    # 6.2 Displaying the top 64 eigenvectors as 16x16 images in an 8x8 table
    image = concat_images(0)
    for q in range(1, 8):
        image = np.concatenate((image, concat_images(q)), axis=0)

    plt.imshow(image, cmap='gray')
    plt.show()

    # 8 Clockwork Angels and Steampunk

    response1 = input("Would you like to know the relationship between Clockwork Angels and Steampunk?(yes/no)")
    if response1 == 'yes':
        webbrowser.open('https://www.etonline.com/music/122647_Rush_Goes_Steampunk_with_Clockwork_Angels')

    response2 = input("Would you like to listen to the song Clockwork Angels from the album Clockwork Angels on youtube?(yes/no)")
    if response2 == 'yes':
        webbrowser.open('https://www.youtube.com/watch?v=IIAftTV4tBk')

    response3 = input("Would you like to buy it on Amazon?(yes/no)")
    if response3 == 'yes':
        webbrowser.open('https://www.amazon.com/Clockwork-Angels-Rush/dp/B007I2BZIE')
