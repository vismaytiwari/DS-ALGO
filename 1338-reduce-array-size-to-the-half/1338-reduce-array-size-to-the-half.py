class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic,n = {},len(arr)
        for i in arr: dic[i] = dic.get(i,0)+1
        lst = [ v for k,v in dic.items() ]
        lst.sort(reverse=True)
        tar = n//2
        for k,i in enumerate(lst):
            n-=i
            if n<=tar:
                return k+1