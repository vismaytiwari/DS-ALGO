class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for i in ransomNote:
            dic[i] = dic.get(i,0) + 1
        for i in magazine:
            if i in dic:
                dic[i]-=1
        for k,v in dic.items():
            if v > 0 :
                return False
        return True