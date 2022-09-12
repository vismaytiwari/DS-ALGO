class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans = 0
        n = len(tokens)
        if n == 0:
            return 0
        if tokens[0] > power:
            return 0
        
        i = 0
        j = n-1
        score = 0
        while i<=j:
            if tokens[i] <= power:
                power -= tokens[i]
                i+=1
                score +=1
                ans = max(ans,score)
                continue
            elif score > 0 :
                power += tokens[j]
                j-=1
                score -=1
                ans = max(ans,score)
                continue
            break
        return ans
                