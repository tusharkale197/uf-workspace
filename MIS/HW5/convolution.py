import numpy as np
import time
import random


class Convolution:

    @staticmethod
    def direct_convolution(seq_1, seq_2):
        """
            Function to compute direct convolution of two sequences
        :param seq_1:
        :param seq_2:
        :return:
        """
        try:
            len_seq_1 = seq_1.shape[0]
            len_seq_2 = seq_2.shape[0]
            if len_seq_1 > len_seq_2:
                loop_len = len_seq_1
                master_seq = seq_1.tolist()
                slave_seq = seq_2.tolist()
            else:
                loop_len = len_seq_2
                master_seq = seq_2.tolist()
                slave_seq = seq_1.tolist()
            slave_seq.reverse()
            len_conv = len_seq_1 + len_seq_2 - 1
            conv_op = [0] * len_conv
            for i in range(0, len_conv):
                if i >= (loop_len-1):
                    offset = loop_len-1
                else:
                    offset = i
                count_1 = offset
                count_2 = -1
                while True:
                    if count_1 < 0 or count_2 < (-1) * len(slave_seq):
                        break
                    if ((-1) * count_2) + count_1 == i+1:
                        conv_op[i] = conv_op[i] + (master_seq[count_1]*slave_seq[count_2])
                        count_1 = count_1-1
                    count_2 = count_2-1

            return np.asarray(conv_op).transpose()
        except Exception as exc:
            raise exc

    @staticmethod
    def fft_convolution(seq_1, seq_2, zero_padding=True):
        """
            Function to compute convolution using FFT
        :param seq_1:
        :param seq_2:
        :param zero_padding:
        :return:
        """
        try:
            seq_1_list = seq_1.tolist()
            seq_2_list = seq_2.tolist()
            if zero_padding:
                seq_1_list.extend([0] * (len(seq_2_list) - 1))
                seq_2_list.extend([0] * (seq_1.shape[0] - 1))
            conv = np.real(np.fft.ifft(np.fft.fft(seq_1_list,n=len(seq_2_list)) * np.fft.fft(seq_2_list, n=len(seq_2_list))))

            return conv
        except Exception as exc:
            raise exc

    def compare_direct_and_fft_conv(self, seq_1, seq_2):
        """

        :return: Times taken by direct and FFT convolution

        """
        try:

            fft_start = time.time()
            fft_conv = self.fft_convolution(seq_1, seq_2)
            fft_end = time.time()
            fft_time = fft_end - fft_start
            dir_con_start = time.time()
            dir_conv = self.direct_convolution(seq_1, seq_2)
            dir_con_end = time.time()
            dir_time = dir_con_end - dir_con_start

            return fft_conv, dir_conv, fft_time, dir_time
        except Exception as exc:
            raise exc

    @staticmethod
    def get_random_sequence(start, end):
        """

        :return:
        """
        try:
            length = random.randint(start, end)
            return np.random.randn(length, )
        except Exception as exc:
            raise exc


if __name__ == "__main__":

    cv = Convolution()

    for j in range(0, 5):
        seqq_1 = cv.get_random_sequence(2000, 3000)
        seqq_2 = cv.get_random_sequence(2000, 3000)

        fft_con, dir_con, fft_tme, dir_tme = cv.compare_direct_and_fft_conv(seqq_1, seqq_2)

        print("Sequence 1 of length {}".format(seqq_1.shape[0]))
        print("Sequence 2 of length {}".format(seqq_2.shape[0]))
        print("FFT Convolution length {}".format(fft_con.shape[0]))
        print("Direct Convolution length {}".format(dir_con.shape[0]))
        print("Time for convolution using FFT {}".format(fft_tme))
        print("Time for Direct Convolution {}".format(dir_tme))

        # check if the sequencees are equal
        length = fft_con.shape[0]
        success = True
        for i in range(0, length-1):
            if round(fft_con[i], 9) != round(dir_con[i], 9):
                print("Sequences not equal at element number {}".format(i))
                success = False
        if success:
            print("Sequences are equal for direct convolution and convolution using fft")
        print("---------------------------------------------")
        # Checking for error when no zero padding

        fft_con_no_zero_pad = cv.fft_convolution(seqq_1, seqq_2, zero_padding=False)
        if fft_con_no_zero_pad.shape[0] != dir_con.shape[0]:
            print("Without zero padding the two sequences have different lengths")
            print("Convolution using FFT without zero pad sequence length {}".format(fft_con_no_zero_pad.shape[0]))
            print("Direct Convolution sequence length {}".format(dir_con.shape[0]))
        print("*********************************************")
