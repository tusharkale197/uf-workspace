import numpy as np

import traceback


class LongestCommonSubsequence:

    @staticmethod
    def find_lcs(seq_1, seq_2):
        """
            Method to return the c and b 2 d arrays to find LCS
        :param seq_1:
        :param seq_2:
        :return:
        """
        try:
            subseq_lens = np.zeros(shape=(len(seq_1), len(seq_2)), dtype=int)
            direction = np.zeros(shape=(len(seq_1), len(seq_2)))

            for i in range(0,len(seq_2)):
                direction[0, i] = ord('n')

            for i in range(0, len(seq_1)):
                direction[i, 0] = ord('n')

            for i in range(1, len(seq_1)):
                for j in range(1, len(seq_2)):
                    if seq_1[i] == seq_2[j]:
                        subseq_lens[i][j] = subseq_lens[i-1][j-1] + 1
                        direction[i][j] = ord('d')
                    elif subseq_lens[i-1][j]>=subseq_lens[i][j-1]:
                        subseq_lens[i][j] = subseq_lens[i-1][j]
                        direction[i][j] = ord('u')
                    else:
                        subseq_lens[i][j] = subseq_lens[i][j-1]
                        direction[i][j] = ord('l')

            return subseq_lens, direction

        except Exception as exc:
            raise exc

    @staticmethod
    def print_lcs( c_arr, seq_1, seq_2):
        """
        :param c_arr:
        :param seq_1:
        :param seq_2:
        :return:
        """
        try:
            i = len(seq_1)-1
            j = len(seq_2)-1

            while True:
                if i == 0 or j == 0:
                    break
                if c_arr[i-1][j] == ord('d'):
                    print(seq_1[i])
                    i = i-1
                    j = j-1
                elif c_arr[i-1][j] == ord('u'):
                    i = i-1
                else:
                    j = j-1

        except Exception as exc:
            traceback.print_exc()
            raise exc


if __name__ == "__main__":
    lcs = LongestCommonSubsequence()
    x = 'BDCABA'
    y = 'ABCBDAB'

    test1, test2 = lcs.find_lcs(list(y), list(x))
    
    lcs.print_lcs(test2, y, x)
    print(test1)
    print(test2)
