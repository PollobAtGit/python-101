class Solution:

    def uncommonFromSentences_dic_2(self, A, B):

        if A and B:
            word_frq = {}

            for x in A.split():
                if x in word_frq:
                    word_frq[x] = word_frq[x] + 1
                else:
                    word_frq[x] = 1

            for x in B.split():
                if x in word_frq:
                    word_frq[x] = word_frq[x] + 1
                else:
                    word_frq[x] = 1

            return [w for w, frq in word_frq.items() if frq == 1]
        return []

    def uncommonFromSentences_dic(self, A, B):

        if A and B:

            def to_hash_table(words):
                if words:
                    dic = {}

                    for x in words:
                        if x in dic:
                            dic[x] = dic[x] + 1
                        else:
                            dic[x] = 1

                    return dic

            A = to_hash_table(A.split())
            B = to_hash_table(B.split())

            uncommons = []

            for x, frq in A.items():
                if x not in B and frq == 1:
                    uncommons.append(x)

            for x, frq in B.items():
                if x not in A and frq == 1:
                    uncommons.append(x)
            return uncommons
        return []

'''
    def remove_multiples(self, arr):

        if arr:

            if len(arr) == 1:
                return arr

            possible_insertion = arr[0]
            is_duplicate = False
            ret = []

            i = 1
            while i < len(arr):
                if possible_insertion != arr[i]:

                    if not is_duplicate:
                        ret.append(possible_insertion)

                    possible_insertion = arr[i]
                    is_duplicate = False
                else:
                    is_duplicate = True

                i = i + 1

            if not is_duplicate:
                ret.append(possible_insertion)

            return ret
        return []

    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        if A is not None and B is not None:
            A = sorted(A.split())
            B = sorted(B.split())

            i = 0
            j = 0
            uncommons = []

            # print("A:B ", A, B)

            while i < len(A) and j < len(B):

                if A[i] != B[j]:

                    if A[i] == A[i - 1]:
                        i = i + 1
                        continue
                    elif B[j] == B[j - 1]:
                        j = j + 1
                        continue

                    if A[i] > B[j]:

                        prev = j
                        while j < len(B) and A[i] > B[j]:
                            j = j + 1

                        uncommons = uncommons + self.remove_multiples(B[prev: j])
                    else:
                        prev = i
                        while i < len(A) and A[i] < B[j]:
                            i = i + 1

                        # print(A[prev: i], self.remove_multiples(A[prev: i]))
                        uncommons = uncommons + self.remove_multiples(A[prev: i])
                else:
                    i = i + 1
                    j = j + 1

            # print(uncommons)
            if i == len(A) and j == len(B):
                return uncommons
            else:
                return uncommons + self.remove_multiples(A[i:]) + self.remove_multiples(B[j:])

        return []
'''

s = Solution()

print(s.uncommonFromSentences_dic_2("this apple is sweet", "this apple is sour"))
print(s.uncommonFromSentences_dic_2("apple apple", "banana"))
print(s.uncommonFromSentences_dic_2("apple apple", "apple cat"))
print(s.uncommonFromSentences_dic_2("mqk g g", "uuz rk uuz"))
print(s.uncommonFromSentences_dic_2("s z z z s", "s z ejt"))
print(s.uncommonFromSentences_dic_2("xf tyl xf", "gw p gw xf"))
