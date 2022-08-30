from  bisect import bisect_left as bl , insort as ins
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])
        res = float('-inf')
        for i in range(m):
            for j in range(1,n):
                matrix[i][j] += matrix[i][j-1]
        
        for i in range(n):
            for j in range(i,n):
                cur = 0
                s = [0]
                for r in range(m):
                    cur += matrix[r][j] - (matrix[r][i-1] if i> 0 else 0)
                    
                    it = bisect.bisect_left(s, cur-k)
                    if it != len(s):
                        res= max(res,cur-s[it])
                    bisect.insort(s, cur)
        return res