class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dic = {}
        a,e,i,o,u = 'a','e','i','o','u'
        dic[a],dic[e],dic[i],dic[o],dic[u] = [u,e,i],[a,i],[o,e],[i],[o,i]
        dp = [[0]*5 for j in range(n)]
        dp[0] = [1,1,1,1,1]
        if n == 1:
            return sum(dp[0])
        else:
            for i in range(1,n):
                dp[i][0] = dp[i-1][4] + dp[i-1][1] + dp[i-1][2] 
                dp[i][1] = dp[i-1][0] + dp[i-1][2] 
                dp[i][2] = dp[i-1][3] + dp[i-1][1]  
                dp[i][3] = dp[i-1][2] 
                dp[i][4] = dp[i-1][3] +  dp[i-1][2] 
        # print(dp)
        return sum(dp[-1]) % (10**9 + 7)