class Solution:

    def compare_version(self, ver_one, ver_two):
        
        if ver_one and ver_two:

            def strip_last_zero(nums):
                
                if nums:
                    
                    if nums[len(nums) - 1] != 0:
                        return nums

                    i = len(nums) - 2
                    while i >= 0:
                        if nums[i] != 0:
                            break
                        i = i - 1

                    return nums[:i + 1]

            ver_one = strip_last_zero([int(x) for x in ver_one.split('.')])
            ver_two = strip_last_zero([int(x) for x in ver_two.split('.')])

            len_two = len(ver_two)
            len_one = len(ver_one)

            lower_v =  len_two if len_one > len_two else len_one

            for i in range(lower_v):
                if ver_one[i] > ver_two[i]:
                    return 1
                elif ver_one[i] < ver_two[i]:
                    return -1

            if len_one == len_two:
                return 0
            elif len_one > len_two:
                return 1
            else: 
                return -1

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # not working
        if version1 and version2:

            len_o = len(version1)
            len_t = len(version2)

            if len_o > len_t:
                version2 = version2 + (".0" * (len_o - len_t))
            else:
                version1 = version1 + (".0" * (len_t - len_o))

            for i, x in enumerate(version1):
                if x != '.':
                    if int(version1[i]) > int(version2[i]):
                        return 1
                    elif int(version1[i]) < int(version2[i]):
                        return -1

            return 0

s = Solution()
print(s.compare_version("0.1", "1.1"))
print(s.compare_version("1.0.1", "1"))
print(s.compare_version("7.5.2.4", "7.5.3"))
print(s.compare_version("1.1", "1.10"))
print(s.compare_version("1.0", "1"))
