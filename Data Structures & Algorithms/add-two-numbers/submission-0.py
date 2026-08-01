# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        num1 = num2 = ""
        while l1:
            stack.append(str(l1.val))
            l1 = l1.next
        while stack:
            num1 += stack.pop()
        while l2:
            stack.append(str(l2.val))
            l2 = l2.next
        while stack:
            num2 += stack.pop()
        num = str(int(num1) + int(num2))
        dummy = ListNode(67)
        curr = dummy
        for i in range(len(num)-1, -1, -1):
            curr.next = ListNode(int(num[i]))
            curr = curr.next
        return dummy.next