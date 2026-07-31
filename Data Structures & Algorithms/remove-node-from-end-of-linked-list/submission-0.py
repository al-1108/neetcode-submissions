# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        count = 0
        while start:
            count += 1
            start = start.next
        start = head
        prev = None
        for i in range(count-n):
            prev = start
            start = start.next
        if prev:
            prev.next = start.next
            start.next = None
            return head
        else:
            return head.next

        