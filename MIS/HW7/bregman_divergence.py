import numpy as np
import math
import matplotlib.pyplot as plt
import time
import lapjv


def row_col(benefit_matrix):
    """
    This method essentially performs one step of the Sinkhorn balancing
    :param benefit_matrix:
    :return:
    """
    try:

        (N, _) = benefit_matrix.shape
        sumr = benefit_matrix.sum(axis=0)
        sumr = np.diag(np.squeeze(np.asarray(sumr)))
        divisor = np.dot(np.ones((N, N)), sumr)
        benefit_matrix = benefit_matrix / divisor

        (N, _) = benefit_matrix.shape
        sumr = benefit_matrix.sum(axis=1)
        sumr = np.diag(np.squeeze(np.asarray(sumr)))
        divisor = np.dot(np.ones((N, N)), sumr)
        benefit_matrix = benefit_matrix / np.transpose(divisor)
        return benefit_matrix

    except Exception as exc:
        raise exc


def perm_norm(perm_mat):
    """
    Function to check how far perm_mat is away from being a permutation matrix

    :param perm_mat: input matrix to be checked
    :return:
    """
    try:

        (N, _) = perm_mat.shape
        perm_cond = np.dot(np.transpose(perm_mat), perm_mat) - np.eye(N)
        temp = np.dot(np.transpose(perm_cond), perm_cond)
        trace_temp = np.trace(temp) / N
        return math.sqrt(trace_temp)
    except Exception as exc:
        raise exc


def row_norm(perm_matrix):
    """
    This function checks how far you are from convergence
    :param perm_matrix:
    :return:
    """
    try:
        (N, _) = np.shape(perm_matrix)
        sumr = perm_matrix.sum(axis=0)
        dotprod = np.dot(sumr - 1, np.transpose(sumr - 1))
        return math.sqrt(dotprod / N)
    except Exception as exc:
        raise exc


def bregman(benefit_matrix, alpha):
    """

    :param benefit_matrix:
    :param alpha: free parameter
    :return:
    """
    (N, _) = benefit_matrix.shape
    W = np.ones((N, N))/N
    perm_mat = W
    l2thr = 0.001
    permthr = 0.2
    p = perm_norm(perm_mat)
    energy = np.trace(np.dot(np.transpose(benefit_matrix), perm_mat))

    ergplot = [energy]
    permplot = [p]
    while p > permthr:
        print(p)
        perm_mat = W * np.exp(alpha * benefit_matrix)
        sinkhorn = 0
        while row_norm(perm_mat) > l2thr:
            perm_mat = row_col(perm_mat)
            sinkhorn += 1
        W = perm_mat
        energy = np.trace(np.dot(np.transpose(benefit_matrix), perm_mat))
        p = perm_norm(perm_mat)
        ergplot.append(energy)
        permplot.append(p)
    cost = np.dot(np.transpose(benefit_matrix), perm_mat)
    return perm_mat, ergplot, permplot, cost


def plot(ergplot, permplot, unique_id):
    """
        Function to plot the permutation norm and objective function and save the images
    :param ergplot:
    :param permplot:
    :return:
    """
    try:

        plt.plot(ergplot, linewidth=3.0)
        plt.xlabel("Iterations")
        plt.ylabel("Trace (A transpose * V)")
        plt.title("Objective function plot")
        plt.savefig("Objective_function_%s.png" % unique_id)
        plt.clf()

        plt.plot(permplot, linewidth=3.0)
        plt.xlabel("Iterations")
        plt.ylabel("Permutation norm")
        plt.title("Permutation norm plot")
        plt.savefig("Permutation_norm_%s.png" % unique_id)
        plt.clf()
    except Exception as exc:
        raise exc


def compare_bregman_lapjv(benefit_mat):
    """
    Function to compare the difference in time required for lapjv and bregman
    :param benefit_mat:
    :return:
    """
    try:
        start_breg = time.time()
        permut_mat, erg_plot, perm_plot, cost= bregman(benefit_mat, 1)
        end_breg = time.time()
        breg_time = end_breg - start_breg

        start_lapjv = time.time()
        row_ind, col_ind, _ = lapjv.lapjv(benefit_mat)
        end_lapjv = time.time()
        lapjv_time = end_lapjv - start_lapjv

        return breg_time, lapjv_time
    except Exception as exc:
        raise exc


if __name__ == "__main__":

    # Plotting the values of the objective function and the permutation matrix
    # Also the variable cost here returns the 100*100 matrix for the final permutation matrix
    ben_mat = np.random.rand(100, 100)
    permut_mat, erg_plot, perm_plot, cost = bregman(ben_mat, 8)
    plot(erg_plot, perm_plot, 0)
    breg_time = list()
    lap_time = list()

    # Running the bregman divergence and lapjv on 10 randomly generated benefit matrices and
    # documenting the time required to output the result
    for i in range(0, 10):
        ben_mat = np.random.rand(100, 100)
        b_time, l_time = compare_bregman_lapjv(ben_mat)
        breg_time.append(b_time)
        lap_time.append(l_time)
        print("%s: iterations done" %i)
    print(breg_time)
    print(lap_time)

    # Varying alpha values we're documenting the number of iterations required to converge
    for alpha_val in range(1, 5):
        permut_mat, erg_plot, perm_plot, cost = bregman(ben_mat, alpha_val)
        print("Iterations for alpha = %s  are %s " %(alpha_val, len(erg_plot)))
        plot(erg_plot, perm_plot, alpha_val)
