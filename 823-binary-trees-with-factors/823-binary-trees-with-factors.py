class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        mod = (10**9) + 7
        mem = {n: 1 for n in arr} 

        for i, root in enumerate(arr):
            limit = sqrt(root) # limiter 
            cnt = 0

            for left in arr: 
                if left > limit: # break early if the current value is greater than sqrt(root)
                    break

                if root % left: # if (root % left) returns any value then there is no divisor so we continue
                    continue

                right = root // left

                if right in mem:
                    cnt += (mem[left] * mem[right] * (1 if left == right else 2))
                    """
                    1. In order to be more efficient when we attempt to find each factor pair, 
                       we only need to iterate through arr up to the square root of the number in question (root)
                    2. So that we don't duplicate the same factor pairs going the opposite direction.
                    3. That means we need to double every pair result where left and right are not the same.
                    """

            mem[root] += (cnt % mod)

        return sum(mem.values()) % mod
