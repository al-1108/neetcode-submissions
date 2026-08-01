# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multi = 1
        num = 0
        while l1 and l2:
            num += (l1.val+l2.val)*multi
            multi *= 10
            l1, l2 = l1.next, l2.next
        while l1:
            num += l1.val*multi
            multi *= 10
            l1 = l1.next
        while l2:
            num += l2.val*multi
            multi *= 10
            l2 = l2.next
        dummy = ListNode(1)
        curr = dummy
        while num != 0 or curr is dummy:
            curr.next = ListNode(num%10)
            num = num // 10
            curr = curr.next
        return dummy.next
        