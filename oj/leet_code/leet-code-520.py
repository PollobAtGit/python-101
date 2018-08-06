class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if word:
            if word.lower() == word or word.upper() == word or word == (word[:1].upper() + word[1:].lower()):
                return True
            return False


s = Solution()
print(s.detectCapitalUse("USA"))
print(s.detectCapitalUse("FlaG"))
print(s.detectCapitalUse(None))
print(s.detectCapitalUse(""))
print(s.detectCapitalUse("trr"))
print(s.detectCapitalUse("TRR"))
print(s.detectCapitalUse("Trr"))
print(s.detectCapitalUse("TrR"))
