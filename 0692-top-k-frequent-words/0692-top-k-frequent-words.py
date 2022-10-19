from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = dict(Counter(words))
        maxHeap = []
        heapq.heapify(maxHeap)
        for key, val in hashmap.items():
            heapq.heappush(maxHeap, (-val, key))
        output = []
        while k:
            popped = heapq.heappop(maxHeap)
            output.append(popped[1])
            k -=1 
        return output