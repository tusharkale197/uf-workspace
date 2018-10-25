class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        try:
            reps = dict()
            morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            for word in words:
                morse_rep = ""
                for charac in word:
                    morse_rep = morse_rep + morse[ord(charac)-97]
                if morse_rep not in reps:
                    reps[morse_rep] = 1
            return len(reps)
        except Exception as e:
            raise e


if __name__ == "__main__":
    s = Solution()
    words = ["gin", "zen", "gig", "msg"]
    print(s.uniqueMorseRepresentations(words))