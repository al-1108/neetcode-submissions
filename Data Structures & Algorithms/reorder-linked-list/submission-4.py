# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr, fast = head, head
        prev = curr
        while fast and fast.next:
            prev = curr
            curr = curr.next
            fast = fast.next.next
        prev.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            if temp is None:
                break
            curr = temp
        l1, l2 = head, prev
        while l1 and l2:
            next1 = l1.next
            next2 = l2.next
            l1.next = l2
            if next1 is None:
                l2.next = next2
                break
            l2.next = next1
            l1 = next1
            l2 = next2

        