class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        if paragraph is not None and banned is not None:

            punc = "!?',;."

            def strip_punc_from_end(para):
                if para:
                    if para[len(para) - 1] not in punc:
                        return para

                    i = len(para) - 2

                    while i >= 0:
                        if para[i] not in punc:
                            break
                        i = i - 1

                    return para[:i + 1]

            for c in punc:
                paragraph = paragraph.replace(c + " ", " ")

            paragraph = strip_punc_from_end(paragraph)

            paragraph = [x.lower() for x in paragraph.split() if x.lower() not in banned]

            dic = {}

            for y in paragraph:
                if y in dic:
                    dic[y] = dic[y] + 1
                else:
                    dic[y] = 1

            return sorted(dic.items(), key=lambda x: x[1], reverse=True)[0][0]


s = Solution()
print(s.mostCommonWord("Bob hit a BALL, the hit BALL flew far after it was hit.", ["hit"]))
print(s.mostCommonWord("a.", []))
print(s.mostCommonWord("Z? Z, Z. S. O. z; X, R. k? X, R' M! D! i. W, p. X, t; s, U; T? Z? W! X, O. g, M; y? t; X; O, X' C' Y; x! q! Y' T; u? R. j? w, M. F' n' F; y, V' z. R, V; x' y? F' m' p? M. w, n! Y' Y? i. S' P? w; w; y! Z; P' o? I, H! L; U; p' i; s' Z. V; S! V! H! y' I? K; d. L! r? u! U. O! s? j. y. G, g, r; Z, X, x' L! l? Z, w! Z' W! b. N! T. P! Y, Z. u! Z, q! Y? P' G' u' t, N' k, H' T, I. S' q? J. q! i? E! Q. O, j' r; r' L' C, z! G, p. S. p' s' L! u. S. t, V; z, Z' p! t? Z. x! h; T; T' V, w; P? Q' T! q. J; E? n. V' X. M? Q, v; U; O, H? h; T. s, n! Y? a, N; o, V, o. S! K' j! Y, W! v; Q! u? U' l. k. r, o. o; m. E, I. n! H' w? u? x! w! U' m; w; R' n. y. Y, W' d; P? z! K! g? m, J' i. t, j. x! F. F' U? K! r' V, r, s! O, Q, v, v, c. E. s! X. k; F' Y! r? P! g! r! V! w; S! X, S! N, z? m. y. B; Y' n' U? r. u; R. l? U? v, r, y' W' W' Q; n' Y? Z, L? O. T? Q' q. l, z! V. T. k; x' q! s; u? W! x' X; P; m! t; T? X, v, v' t. Y' q; X? u; V; X! q! w. j! W; z; v. u, j. w; v. z; W' P' z; l! l. o! Z, Y. H; Q; k' O' m, U!", ["c","y","u","i","p","j","g","r","o","h","t","m","k","z","s","q","v","a","e","x"]))
