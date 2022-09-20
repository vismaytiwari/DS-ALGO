class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        maax = 0
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j] = 1 if nums1[j]==nums2[i] else 0
                else:
                    dp[i][j] = dp[i-1][j-1] + 1 if nums1[j]==nums2[i] else 0
                maax = max(maax,dp[i][j])
        return maax