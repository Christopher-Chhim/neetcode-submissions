# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Create set
        visited = set()
        # set current node equal to head
        curr = head

        # loop through curr
        while curr:
            # checks to see if current node is in visited
            if curr in visited:
                return True

        # add current value to visited
            visited.add(curr)
        # update current node
            curr = curr.next

        return False