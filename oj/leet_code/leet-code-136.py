class Solution:
    def single_number_bitwise_solution(self, nums):
        if nums:
            xored_value = 0
            for x in nums:
                xored_value = xored_value ^ x

            return xored_value


    def single_number_better_approach(self, nums):

        if nums:

            frequency_container = {}

            for x in nums:
                try:
                    frequency_container.pop(x)
                except:
                    frequency_container[x] = 1

            return frequency_container.popitem()[0]

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums:

            def number_frequency_count(arr):
                dic = {}
                for x in nums:
                    if x is not None:
                        if dic.get(x):
                            dic[x] = dic[x] + 1
                        else:
                            dic[x] = 1

                return dic

            num_freq = number_frequency_count(nums)

            if num_freq:
                filtered_dic = [x for x, y in num_freq.items() if y == 1]
                if filtered_dic:
                    return filtered_dic[0]


s = Solution()
print(s.single_number_bitwise_solution([2, 2, 1]))
print(s.single_number_bitwise_solution([4, 1, 2, 1, 2]))
print(s.single_number_bitwise_solution([1, 0, 1]))

print(s.single_number_better_approach([1, 0, 1]))
print(s.single_number_bitwise_solution([1, 0, 1]))
