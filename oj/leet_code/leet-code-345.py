class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s:

            l_p = 0
            r_p = len(s) - 1

            vowels = "aeiou"

            s = list(s)

            while l_p < r_p:

                l_p_vowel = s[l_p].lower() in vowels
                r_p_vowel = s[r_p].lower() in vowels

                if l_p_vowel and r_p_vowel:
                    s[l_p], s[r_p] = s[r_p], s[l_p]

                if l_p_vowel and not r_p_vowel:
                    r_p = r_p - 1
                elif not l_p_vowel and r_p_vowel:
                    l_p = l_p + 1
                else:
                    r_p = r_p - 1
                    l_p = l_p + 1

            return "".join(s)
        return ""


s = Solution()
print(s.reverseVowels("leetcode"))
print(s.reverseVowels("hello"))


