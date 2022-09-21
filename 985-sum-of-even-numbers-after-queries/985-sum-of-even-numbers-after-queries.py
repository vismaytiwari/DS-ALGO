class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        dic = {}
        suum = 0
        ans = []
        for i,v in enumerate(nums):
            dic[i] = v
            if v%2== 0:
                suum += v
        for v,i in queries:
            if nums[i]%2==0:
                suum-=nums[i]
            nums[i]+=v
            if nums[i]%2==0:
                suum+=nums[i]
            ans.append(suum)
        return ans