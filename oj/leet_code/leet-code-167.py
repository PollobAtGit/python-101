# base
"""
if start_index == end_index:
    if search_value == sequence[start_index]:
        return start_index
    else:
        return []
"""

class Solution(object):

    def binary_search(self, search_value, start_index, end_index, sequence):
        
        if sequence:
            
            if end_index < start_index:
                return []
            else:

                mid_index = start_index + (end_index - start_index) / 2

                if search_value == sequence[mid_index]:
                    return mid_index

                if search_value > sequence[mid_index]:
                    return self.binary_search(search_value = search_value, \
                        start_index = mid_index + 1, \
                        end_index = end_index, \
                        sequence = sequence)

                elif search_value < sequence[mid_index]:

                    return self.binary_search(search_value = search_value, \
                        start_index = start_index, \
                        end_index = mid_index - 1, \
                        sequence = sequence)
                

    def with_binary_sort(self, numbers, target):

        if numbers and len(numbers) > 1 and target is not None:

            if len(numbers) == 2:
                if numbers[0] + numbers[1] == target:
                    return [1, 2]

                # ignoring else

            for i, x in enumerate(numbers):

                looking_for = target - x

                binary_search_result = self.binary_search(search_value = looking_for, \
                    start_index = i + 1, \
                    end_index = len(numbers) - 1, \
                    sequence = numbers)

                if binary_search_result:
                    return [i + 1, binary_search_result + 1]

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # non zero based index

        if numbers and target is not None:

            if len(numbers) == 1:
                if numbers[0] == target:
                    return 1

                # ignoring else

            hash_table = {}

            for i, x in enumerate(numbers):
                if x in hash_table:
                    return [min(i + 1, hash_table[x]), max(i + 1, hash_table[x])]
                else:
                    hash_table[target - x] = (i + 1)

"""

assumption: 
    only one solution exists
    all numbers are unique
    sorted in ascending order
    there will always be only one solution
    each numbers [-min, 0, +max]

"""

s = Solution()

# print(s.twoSum([2,7,11,15], 9))
"""
print(s.with_binary_sort([-11, -7, 2, 15], -18))
print(s.with_binary_sort([-7, -5, -2, 7, 9], -9))
print(s.with_binary_sort([-2, -1, 0, 2, 7, 9], 0))
"""

# print(s.with_binary_sort([1,2,3,4,4,9,56,90], 8))
print(s.with_binary_sort([12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997], \
    542))

