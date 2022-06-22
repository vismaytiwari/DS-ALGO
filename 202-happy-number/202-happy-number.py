class Solution:
    def find_sum(self, num):
        s = 0
        for i in str(num):
            s += pow(int(i), 2)
        return s
    
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = self.find_sum(n)
            if n in seen:
                return False
            seen.add(n)
        return n == 1