class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        if words is not None:

            rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
            ret = []

            for i, word in enumerate([w.lower() for w in words if w]):
                if word:
                    if len([x for x in word if x in rows[0]]) == len(word):
                        ret.append(words[i])
                    elif len([x for x in word if x in rows[1]]) == len(word):
                        ret.append(words[i])
                    elif len([x for x in word if x in rows[2]]) == len(word):
                        ret.append(words[i])

            return ret


s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
print(s.findWords([]))
print(s.findWords([None]))
print(s.findWords(None))
