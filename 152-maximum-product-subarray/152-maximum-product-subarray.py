class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #get prefix multiplication to get max prod excluding 0
        
        til = -1000000000
        cur = 1
        for i in nums:
            
            cur *= i
            til = max(cur,til)
            if i == 0 :
                cur = 1
            
        #get sufix multiplication to get max prod excluding 0
        cur = 1
        nums.reverse()
        for i in nums:
            cur *= i
            til = max(cur,til)
        
            if i == 0 :
                cur = 1
            
        return til