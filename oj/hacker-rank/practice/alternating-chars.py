
# AAAA
# BBBBB
# ABABABAB
# BABABA
# AAABBB

def find_mini_deletion(s):
    if s is not None:
        i = 0
        del_count = 0
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                del_count += 1
            i += 1
        return del_count
