class Solution:
    def trap(self, height: List[int]) -> int:
        lst  = height
        maax = lst[0]
        lst_lft = [0]*(len(lst))
        for i in range(1,len(lst)):
            lst_lft[i] = max(lst[i-1],maax)
            maax = max(maax,lst[i-1])
        
        lst.reverse()
        maax = lst[0]
        lst_rgt = [0]*(len(lst)-1)
        for i in range(1,len(lst)):
            lst_rgt[i-1] = max(lst[i-1],maax)
            maax = max(maax,lst[i-1])
        
        
        lst.reverse()
        
        lst_rgt.reverse()
        lst_rgt.append(0)
        ans = 0
        for i,v in enumerate(lst):
            if lst_lft[i] == 0 or lst_rgt[i] == 0 :
                continue
            temp = 0
            temp2 = min (lst_lft[i], lst_rgt[i])
            temp = temp2 - lst[i]
            if temp > 0:
                ans += temp
                
        return ans
    