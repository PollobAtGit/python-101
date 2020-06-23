
def has_common_substring(p, q):
    if p is not None and q is not None:
        for ch in p:
            if ch in q:
                return "YES"
        return "NO"
