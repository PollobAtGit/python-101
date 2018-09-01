class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator is not None and denominator is not None:
            div = str(numerator / denominator)
            splits = div.split(".")
            fraction = splits[1]

            if int(fraction) == 0:
                return splits[0]

            print(fraction)

            # fraction can be 0

            def next_index_of(str, ch, begin_index=0):
                if ch and str:
                    i = begin_index
                    while i < len(str):
                        if ch == str[i]:
                            return i
                        i = i + 1

                    return None

            ret_fraction = ""
            i = 0
            while i < len(fraction):

                tmp = ""
                while i + 1 < len(fraction) and fraction[i] == fraction[i + 1]:
                    tmp = tmp + fraction[i]
                    i = i + 1

                if len(tmp) == 0:
                    ret_fraction = ret_fraction + fraction[i]
                else:
                    ret_fraction = ret_fraction + "(" + tmp[0] + ")"
                    i = i + 1

                j = next_index_of(fraction, fraction[i], i + 1)

                if j is None:
                    ret_fraction = ret_fraction + fraction[i]
                elif j is not None:

                    tmp_frac = ""

                    while i < len(fraction) and j < len(fraction) and fraction[i] == fraction[j]:
                        tmp_frac = tmp_frac + fraction[i]
                        i = i + 1
                        j = j + 1

                    ret_fraction = ret_fraction + "(" + tmp_frac + ")"
                    i = j
                    continue

                i = i + 1

            return splits[0] + "." + ret_fraction

s = Solution()

'''
print(s.fractionToDecimal(1, 2))
print(s.fractionToDecimal(2, 1))
print(s.fractionToDecimal(2, 3))
'''
print(s.fractionToDecimal(1032, 990))
