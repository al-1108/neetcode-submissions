# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev_group_end = dummy = ListNode(1, head)
        while True:
            count, curr = k, prev_group_end
            while curr and count > 0:
                curr, count = curr.next, count-1
            if not curr:
                break

            next_group_start, prev, cur = curr.next, curr.next, prev_group_end.next
            group_start = cur
            while cur != next_group_start:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            prev_group_end.next = prev
            prev_group_end = group_start
        return dummy.next

