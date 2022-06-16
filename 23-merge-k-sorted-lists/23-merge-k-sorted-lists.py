# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush as hpu, heappop as hp
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = head = ListNode(0)
        heap = []
        #adding a tupple to queue for sorting and also need  to insert index to prevent tie in case of two node of same value
        for i,v in enumerate(lists):
            if v is not None:
                hpu(heap,(v.val,i,v))
        while heap:
            _,i,cur.next = hp(heap)
            cur = cur.next
            if cur.next is not None:
                hpu(heap,(cur.next.val,i,cur.next))
        return head.next
            
            
            