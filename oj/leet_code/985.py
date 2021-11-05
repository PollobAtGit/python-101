class Solution(object):
    def isEven(self, num):
        return num % 2 == 0
    
    def sumEvenAfterQueries(self, nums, queries):
        answers = []
        
        sumOfEvens = self.summationOfEvens(nums)
        
        for i in range(len(queries)):
            query = queries[i]
            index = query[1]
            val = query[0]
            
            current = nums[index]
            
            nums[index] = nums[index] + val
            
            # print(nums)
            
            if self.isEven(current) and not self.isEven(nums[index]):
                sumOfEvens = sumOfEvens - current
                
            if not self.isEven(current) and self.isEven(nums[index]):
                sumOfEvens = sumOfEvens + nums[index]
                
            if self.isEven(current) and self.isEven(nums[index]):
                sumOfEvens = sumOfEvens - current
                sumOfEvens = sumOfEvens + nums[index]

            answers.append(sumOfEvens)
            
        return answers
    
    def summationOfEvens(self, nums):
        r = 0
        length = len(nums)
        index = 0
        
        while index < length:

            if nums[index] % 2 == 0:
                r = r + nums[index]
            
            index = index + 1
            
        return r            

            
        
