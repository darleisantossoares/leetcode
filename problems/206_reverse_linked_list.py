# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        node = head
        previous = None

        while node:
            tmp_next = node.next
            node.next = previous
            previous = node
            node = tmp_next

        return previous
