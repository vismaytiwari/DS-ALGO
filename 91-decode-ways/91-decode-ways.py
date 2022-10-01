class Solution:
    def numDecodings(self, s: str) -> int:
        s += "#"
        dp = [ 0]*len(s) 
        n = len(s)
        
        for i,v in enumerate(s):
            if i==0:
                
                if int(v)!=0: dp[0] =1
            elif i==1:
                
                if 0<int(s[i-1:i])<10: dp[i] += dp[i-1]
            else:
                if 0<int(s[i-1])<10: dp[i] += dp[i-1]
                if 9<int(s[i-2:i])<27: dp[i] += dp[i-2]
        # print(dp)    
        return dp[-1]