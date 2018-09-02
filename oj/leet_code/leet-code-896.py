class Solution:
    def isMonotonic(self, A):
        if A:

            is_increasing = None
            prev_el = A[0]

            for x in A[1:]:
                if is_increasing is None:
                    if prev_el < x: 
                        is_increasing = True
                    elif prev_el > x:
                        is_increasing = False
                else:
                    if is_increasing and x < prev_el:
                        return False
                    elif not is_increasing and x > prev_el:
                        return False

                prev_el = x

            return True
        return False

s = Solution()

'''
print(s.isMonotonic([1,2,4,5]))
print(s.isMonotonic([1,1,1]))
print(s.isMonotonic([6,5,4,4]))
print(s.isMonotonic([1,2,2,3]))
print(s.isMonotonic([1,3,2]))
'''

print(s.isMonotonic([1,1,1,3,20]))
print(s.isMonotonic([-1, 2]))
