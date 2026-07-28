# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#even funnier solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        for _ in range(1000):
            head = head.next if head is not None else None

        return head is not None
        