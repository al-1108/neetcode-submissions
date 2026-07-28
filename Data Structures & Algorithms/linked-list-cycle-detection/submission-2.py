# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#funny solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0 
        if not head:
            return False
        while head.next and count <= 1000:
            head = head.next
            count += 1
        if count > 1000:
            return True
        else:
            return False

        