# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                value1 = l1.val

            else:
                value1 = 0


            if l2:
                value2 = l2.val

            else:
                value2 = 0


            total = value1 + value2 + carry

            #seperate the total to single digits
            digit = total %  10
            carry = total // 10

            current.next = ListNode (digit)

            current = current.next


            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
        