class Solution(object):

    def uncommon_from_sentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        try:
            count_words = dict()
            a_list = A.split(" ")
            b_list = B.split(" ")
            output = list()
            for word in a_list:
                if word in count_words:
                    count_words[word] = count_words[word] + 1
                else:
                    count_words[word] = 1

            for word in b_list:
                if word in count_words:
                    count_words[word] = count_words[word] + 1
                else:
                    count_words[word] = 1
            for key in count_words:
                if count_words[key] == 1:
                    output.append(key)
            return output

        except Exception as exc:
            raise exc


if __name__ == "__main__":

    s = Solution()
    A = "this apple is sweet"
    B = "this apple is sour"
    print(s.uncommon_from_sentences(A, B))
