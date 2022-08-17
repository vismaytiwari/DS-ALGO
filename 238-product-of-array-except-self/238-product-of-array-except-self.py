class Solution:
    def productExceptSelf(self, lst: List[int]) -> List[int]:
        pre = [1]
        suf = [1]
        lst2 = lst[::-1]
        for i,v in enumerate(lst):
            if i == 0: continue
            else:
                pre.append(pre[-1]*lst[i-1])
                suf.append(suf[-1]*lst2[i-1])
        suf = suf[::-1]
        for i in range(len(lst)):
            lst[i] = suf[i]*pre[i]
        return lst