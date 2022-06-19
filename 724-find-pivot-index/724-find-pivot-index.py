class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        dp_l = [0]*len(nums)
        dp_r = [0]*len(nums)
        for i,v in enumerate(nums):
            if i==0:
                continue
            dp_l[i] = dp_l[i-1]+nums[i-1]
        
        nums.reverse()
        for i,v in enumerate(nums):
            if i==0:
                continue
            dp_r[i] = dp_r[i-1]+nums[i-1]
            
        nums.reverse()
        dp_r.reverse()
        print(dp_l,dp_r)
        for i,v in enumerate(nums):
            if dp_l[i]==dp_r[i]:
                return i
        return -1
            