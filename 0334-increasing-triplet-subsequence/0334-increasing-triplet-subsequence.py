class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = []
        for elem in nums:
            ind = bisect_left(dp, elem)
            if ind == len(dp):
                dp.append(elem)
            else:
                dp[ind] = elem
            if len(dp)>2: return True
        return False