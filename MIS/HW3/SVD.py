# """
# https://github.com/tusharkaley/uf-workspace/tree/master/MIS/HW3
# """

from scipy.misc.pilutil import imread
import numpy as np
import matplotlib.pyplot as plt
import skimage


def compute_a_dash(u, s, v, threshold):
    """

    :param u: U matrix
    :param s: Sigma values
    :param v: V transpose matrix
    :param threshold:
    :return:
    """
    try:
        a_dash_float = np.zeros(shape=(2000, 2000), dtype=float)
        a_dash_int = np.zeros(shape=(2000, 2000), dtype=int)

        for matrix_ind in range(0, threshold):
            test_1 = u[:, [matrix_ind]]
            test_2 = v[[matrix_ind], :]

            a_dash_float = np.add(a_dash_float, s[matrix_ind] * np.matmul(test_1, test_2))

        min_a_dash = np.amin(a_dash_float)
        max_min_diff = np.amax(a_dash_float) - min_a_dash

        for i in range(0, 2000):
            for j in range(0, 2000):
                a_dash_int[i][j] = 255*(a_dash_float[i][j]-min_a_dash)/max_min_diff
        return a_dash_int
    except Exception as exc:
        raise exc


def svd_on_image(r_channel, g_channel, b_channel, sigma_threshold=50):
    """

    :param r_channel: Matrix reprensenting r channel
    :param g_channel: Matrix reprensenting g channel
    :param b_channel: Matrix reprensenting b channel
    :param sigma_threshold: the number of sigma values (dimensions) to be considered
    :return:
    """
    try:
        # 2.1 Execute the SVD separately on the R, G and B channels of the image
        r_chan_u, r_chan_s, r_chan_v = np.linalg.svd(r_channel)
        g_chan_u, g_chan_s, g_chan_v = np.linalg.svd(g_channel)
        b_chan_u, b_chan_s, b_chan_v = np.linalg.svd(b_channel)

        a_dash_r = compute_a_dash(r_chan_u, r_chan_s, r_chan_v, sigma_threshold)
        a_dash_g = compute_a_dash(g_chan_u, g_chan_s, g_chan_v, sigma_threshold)
        a_dash_b = compute_a_dash(b_chan_u, b_chan_s, b_chan_v, sigma_threshold)

        output_img = np.empty([2000, 2000, 3], dtype=int)
        output_img[:, :, 0] = a_dash_r
        output_img[:, :, 1] = a_dash_g
        output_img[:, :, 2] = a_dash_b

        plt.imshow(output_img)
        plt.show()

    except Exception as exc:
        raise exc


def frobenius_norm(sigma_threshold, channel_select=0):
    """
    :param sigma_threshold Dimension restriction
    :param channel_select 0 -> R, 1 -> G, 2 -> B
    :return:
    """
    try:
        read_img = imread("hendrix_final.png", mode="RGB")
        read_img = skimage.img_as_float(read_img)
        u, s, v = np.linalg.svd(read_img[:, :, channel_select])

        a_dash_float = np.zeros(shape=(2000, 2000), dtype=float)
        fro_norm_list = list()
        for matrix_ind in range(0, sigma_threshold):
            print(matrix_ind)
            test_1 = u[:, [matrix_ind]]
            test_2 = v[[matrix_ind], :]

            a_dash_float = np.add(a_dash_float, s[matrix_ind] * np.matmul(test_1, test_2))

            recon_error_matrix_r = np.subtract(read_img[:, :, channel_select], a_dash_float)
            fro_norm = np.linalg.norm(recon_error_matrix_r, ord="fro")
            fro_norm_list.append(fro_norm)

        return fro_norm_list

    except Exception as exc:
        raise exc


def log_log_plot_sigmas(channel_matrix):
    """
    :param channel_matrix : Matrix who is to be log log plotted
    :return:
    """
    try:

        r_chan_u, r_chan_s, r_chan_v = np.linalg.svd(channel_matrix)
        x = [n for n in range(1, 2001)]
        plt.loglog(x, r_chan_s)
        plt.show()

    except Exception as exc:
        raise exc


if __name__ == '__main__':

    # 1. Load the hendrix_final.png image and extract the R, G and B channels.
    read_image = imread("hendrix_final.png", mode="RGB")

    # 1.1 Convert each channel image to double precision.
    read_image = skimage.img_as_float(read_image)

    # 1.2 Extract R, G and B channels
    r_chan = read_image[:, :, 0]
    g_chan = read_image[:, :, 1]
    b_chan = read_image[:, :, 2]

    # log-log plot of the non-zero singular values for the R channel
    log_log_plot_sigmas(r_chan)

    # Frobenius norm of the reconstruction error matrix for each channel
    x = [n for n in range(1, 2001)]
    fro_norms_list = frobenius_norm(sigma_threshold=2000, channel_select=0)
    plt.plot(x, fro_norms_list)
    plt.show()

    fro_norms_list = frobenius_norm(sigma_threshold=2000, channel_select=1)
    plt.plot(x, fro_norms_list)
    plt.show()

    fro_norms_list = frobenius_norm(sigma_threshold=2000, channel_select=2)
    plt.plot(x, fro_norms_list)
    plt.show()

    # Display the final reconstructed images for different dimensions
    svd_on_image(r_chan, g_chan, b_chan, sigma_threshold=100)


