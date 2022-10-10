class Solution:
    def breakPalindrome(self, pal: str) -> str:
        n = len(pal)
        if n <= 1 : return ""
        flag = False
        for i in range(n):
            if (i==n//2 and n%2!=0 ):
                continue 
            if pal[i] !='a' : 
                flag = True
                break
        
        if flag:
            return pal[:i]+'a'+pal[i+1:]
        else:
            return pal[:n-1]+'b'