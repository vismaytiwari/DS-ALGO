class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        lst = [nums[0],1]
        for i in range(1,n):
            if nums[i]==lst[0]:
                lst[1]+=1
            else:
                if lst[1]==1:
                    lst[0]=nums[i]
                else:
                    lst[1]-=1
        return lst[0]