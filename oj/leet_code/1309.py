class Solution(object):
    def __init__(self):
        self.mapping = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',

            '10': 'j',
            '11': 'k',
            '12': 'l',
            '13': 'm',
            '14': 'n',
            '15': 'o',
            '16': 'p',
            '17': 'q',
            '18': 'r',
            '19': 's',
            '20': 't',
            '21': 'u',
            '22': 'v',
            '23': 'w',
            '24': 'x',
            '25': 'y',
            '26': 'z',
        }

    def freqAlphabets(self, s):
        if s is not None:
            i = 0
            partial = ""
            r = []
            while i < len(s):
                if s[i] == "#":
                    q = []
                    if partial[len(partial)-2:] in self.mapping:
                        q.append(self.mapping[partial[len(partial)-2:]])
                    if len(partial[:len(partial)-2]) > 0:
                        for x in partial[:len(partial)-2][::-1]:
                            if x in self.mapping:
                                q.append(self.mapping[x])
                    r = r + q[::-1]
                    partial = ""
                else:
                    partial += s[i]
                i = i + 1

            if partial:
                for x in partial:
                    if x in self.mapping:
                        r.append(self.mapping[x])

            return "".join(r)
