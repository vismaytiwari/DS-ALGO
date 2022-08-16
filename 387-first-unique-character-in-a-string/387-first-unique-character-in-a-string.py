class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0)+1
        for ind,i in enumerate(s):
            if dic[i]==1:
                return ind
        return  -1
            