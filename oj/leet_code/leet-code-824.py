class Solution:

    def to_goat_latin_better_solution(self, S):

        def covert_to_gl(w):

            vowels = "aeiouAEIOU"

            if w[:1] in vowels:
                return w[:] + 'ma'
            return w[1:] + w[:1] + 'ma'

        return " ".join([covert_to_gl(w) + 'a' * i for i, w in enumerate(S.split(), 1)])

    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """

        vowels = ['a', 'e', 'i', 'o', 'u']

        words = S.split()

        for indx, word in enumerate(words):
            if word and len(word) > 0:

                itr = ("a" * (indx + 1))

                if vowels.count(word[0].lower()) > 0:
                    words[indx] = word + "ma"
                else:
                    words[indx] = word[1:] + word[0] + "ma"

                words[indx] = words[indx] + itr

        return " ".join(words)


s = Solution()
print(s.to_goat_latin_better_solution("I speak Goat Latin"))
print(s.to_goat_latin_better_solution(
    "The quick brown fox jumped over the lazy dog"))
print(s.to_goat_latin_better_solution(
    "Each word consists of lowercase and uppercase letters only"))
print(s.to_goat_latin_better_solution(
    "Each word consists of lowercase and uppercase letters only"))
