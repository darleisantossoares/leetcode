# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.arr = []

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        sentinel = ListNode(None, None)
        ans = sentinel
        self.traverse_ll(list1)
        self.traverse_ll(list2)
        heapq.heapify(self.arr)
        prev = sentinel
        while self.arr:
            new_node = ListNode()
            v = heapq.heappop(self.arr)
            new_node.val = v
            sentinel = new_node
            prev.next = sentinel
            prev = sentinel
            sentinel = sentinel.next
        return ans.next

    def traverse_ll(self, node):
        if node is None:
            return
        self.arr.append(node.val)
        self.traverse_ll(node.next)
