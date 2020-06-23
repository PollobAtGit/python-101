
import collections

def can_replicate(m, r):
    if m is not None and r is not None:
        m_hash = collections.Counter(m)
        r_hash = collections.Counter(r)

        for x, c in r_hash.items():
            if not (x in m_hash and c <= m_hash[x]):
                print("No")
                return
        print("Yes")
        return
