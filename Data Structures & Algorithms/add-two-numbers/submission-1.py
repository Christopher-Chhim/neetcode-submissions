# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # setting l1 and l2 values to val1 and val2 variables and val 1 and val2 = 0 if there's no value.
            val1 = l1.val if l1 else 0  
            val2 = l2.val if l2 else 0

            # new digit
            total = val1 + val2 + carry
            carry = total // 10
            total = total % 10
            curr.next = ListNode(total)

            # update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next