class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def inner(arr):
            if arr:
                inner_stack = []
                for x in arr:
                    if x == "#" and inner_stack:
                        inner_stack.pop()
                    elif x != "#":
                        inner_stack.append(x)

                return inner_stack

        return "".join(inner(S)) == "".join(inner(T))


s = Solution()
print(s.backspaceCompare("ab#c", "ad#c"))
print(s.backspaceCompare("ab##", "c#d#"))
print(s.backspaceCompare("a##c", "#a#c"))
print(s.backspaceCompare("y#fo##f", "y#f#o##f"))
print(s.backspaceCompare("a#c", "b"))
