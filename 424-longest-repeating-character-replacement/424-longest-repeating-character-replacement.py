class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        n = len(s)
        cur_len = 0
        maax = 0
        dic = dict()
        for r,v in enumerate(s):
            if v not in dic:
                dic[v]=1
            else:
                dic[v]+=1
            cur_len = r-l+1
            if cur_len - max(dic.values()) <= k:
                maax = max(maax,cur_len)
            else:
                dic[s[l]]-=1
                l+=1
        return maax
                