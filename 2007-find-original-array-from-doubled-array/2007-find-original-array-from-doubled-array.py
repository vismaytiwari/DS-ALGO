class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        '''
        1,2,3,4,6,8
        [8]
        [1,3,4]
        '''
        arr = sorted(changed)
        dq = deque([])
        res = []
        for i in arr:
            if dq and i == dq[0]:
                dq.popleft()
            else:
                dq.append(2*i)
                res.append(i)
        
        if dq:
            return []
        return res