# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size = 0

        node = head

        while node:
            node = node.next
            size += 1

        k = size - n

        node = head

        dummy = ListNode('dummy')

        dummy.next = node
        previous = dummy

        i = 0
        while node:

            if i == k:
                previous.next = node.next

            i += 1

            previous = node
            node = node.next

        return dummy.next
