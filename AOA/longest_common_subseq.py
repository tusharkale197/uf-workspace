import numpy as np


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
            direction = np.chararray(shape=(len(seq_1), len(seq_2)))

            for i in range(0,len(seq_2)):
                direction[0, i] = 'n'

            for i in range(0, len(seq_1)):
                direction[i, 0] = 'n'

            for i in range(1, len(seq_1)):
                for j in range(1, len(seq_2)):
                    if seq_1[i] == seq_2[j]:
                        subseq_lens[i][j] = subseq_lens[i-1][j-1] + 1
                        direction[i][j] = "d"
                    elif subseq_lens[i-1][j]>=subseq_lens[i][j-1]:
                        subseq_lens[i][j] = subseq_lens[i-1][j]
                        direction[i][j] = "u"
                    else:
                        subseq_lens[i][j] = subseq_lens[i][j-1]
                        direction[i][j] = "l"

            return subseq_lens, direction

        except Exception as exc:
            raise exc

    @staticmethod
    def print_lcs(c_arr, seq_1, seq_2):
        """
            *** GOT TO FIX THIS ***
        :param c_arr:
        :param seq_1:
        :param seq_2:
        :return:
        """
        try:
            i = len(seq_1)
            j = len(seq_2)
            while True:
                if i == 0 or j == 0:
                    break
                if seq_1[i-1] == seq_2[j-1]:
                    print(seq_1[i])
                    i = i-1
                    j = j-1
                else:
                    if c_arr[i-1][j] == c_arr[i][j]:
                        i = i-1
                    elif c_arr[i][j-1] == c_arr[i][j]:
                        j = j-1

        except Exception as exc:
            raise exc


if __name__ == "__main__":
    lcs = LongestCommonSubsequence()
    x = 'QBDCABA'
    y = 'QABCBDAB'

    test1, test2 = lcs.find_lcs(list(y), list(x))
    lcs.print_lcs(test1, list(y), list(x))
