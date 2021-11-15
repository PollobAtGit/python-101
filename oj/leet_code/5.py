class Solution(object):
    
    def isPalindrome(self, x):

        i = 0
        j = len(x) - 1
        
        while i <= j and i >= 0 and j < len(x):
            if x[i] == x[j]:
                i = i + 1
                j = j - 1
            else:
                return False
        
        return True
        
    def longestPalindrome(self, s):
        
        palindromes = []
        
        for i in range(len(s)):
            
            j = len(s) - 1
            
            while i <= j and i >= 0 and j < len(s):
        
                v = s[i:j + 1]
        
                if self.isPalindrome(v):
                    palindromes.append(v)
                    break
                
                j = j - 1
               
        # print(len(palindromes))
        
        palindromes.sort(key = len)
        palindromes.reverse()
        
        return palindromes[0]
                
                
        
