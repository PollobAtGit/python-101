
class Solution(object):

    # not working
    def find_where_to_put_target_value(self, letters, target):
        
        if letters and target:

            target_index = self.binary_search(letters, target, 0, len(letters), return_index = True)

            print(target_index)
            if target_index is None:
                target_index = -1
            
            return letters[(target_index + 1) % len(letters)]



    def binary_search(self, sequence, search_for, start_index, end_index, return_index = False):

        if sequence and search_for:

            if end_index < start_index:
                if not return_index:
                    return False
                else:
                    return None

            else:                
                mid_index = start_index + (end_index - start_index) / 2

                if search_for == sequence[mid_index]:
                    if not return_index:
                        return True
                    else:
                        return mid_index

                if search_for > sequence[mid_index]:
                    return self.binary_search(sequence, \
                        search_for, \
                        start_index = mid_index + 1, \
                        end_index = end_index, \
                        return_index = return_index)

                else:
                    return self.binary_search(sequence, \
                        search_for, \
                        start_index = start_index, \
                        end_index = mid_index - 1, \
                        return_index = return_index)

    def next_greater_iterate_over_ascii_list_with_binary_sort(self, letters, target):

        """
            complexity: O(26 * log(n))
        """

        if letters and target:

            for x in range(ord(target) + 1, 123):

                binary_search_result = self.binary_search(sequence = letters, \
                                        search_for = chr(x), \
                                        start_index = 0, \
                                        end_index = len(letters) - 1)

                if binary_search_result:
                    return chr(x)

            return letters[0]


    def next_greater_iterate_over_ascii_list(self, letters, target):

        """
            complexity: O(26 * n) n : n = len(letters)
        """

        if letters and target:

            for x in range(ord(target) + 1, 123):
                if letters.count(chr(x)) > 0:
                    return chr(x)

            return letters[0]

    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        """
        complexity: O(n) : n = len(letters)
        space complexity: O(1) for pointer 'x'
        """

        if letters and target:

            for x in letters:
                if x > target:
                    return x

            return letters[0]
        

s = Solution()

"""
print(s.nextGreatestLetter(["c", "f", "j"], "a"))# c
print(s.nextGreatestLetter(["c", "f", "j"], "c"))# f
print(s.nextGreatestLetter(["c", "f", "j"], "k"))# c
print(s.nextGreatestLetter(["c"], "c"))# c
print(s.nextGreatestLetter([], "c"))# _
print(s.nextGreatestLetter([], ""))# _

print(s.nextGreatestLetter(["c", "f", "j"], "d"))# _
print(s.nextGreatestLetter(["c", "f", "j"], "g"))# _
print(s.nextGreatestLetter(["c", "f", "j"], "j"))# _
print(s.nextGreatestLetter(["c", "f", "j"], "k"))# _
"""

def next_letter(nums, tar):
    print(s.find_where_to_put_target_value(nums, tar))

"""
next_letter(["c", "f", "j"], "d")
next_letter(["c", "f", "j"], "g")
next_letter(["c", "f", "j"], "j")
next_letter(["c", "f", "j"], "k")
"""

# next_letter(["c", "f", "j"], "a")# c
# next_letter(["c", "f", "j"], "c")# f

next_letter(["c", "f", "j"], "k")# c
"""
next_letter(["c"], "c")# c
next_letter([], "c")# _
next_letter([], "")# _
"""