class Solution(object):

    @staticmethod
    def num_jewels_in_stones(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        try:
            jewels_dict = dict()
            jewel_count = 0
            for jewel in list(J):
                jewels_dict[jewel] = 1
            for stone in list(S):
                if stone in jewels_dict:
                    jewel_count = jewel_count + 1
            return jewel_count
        except Exception as exc:
            raise exc
