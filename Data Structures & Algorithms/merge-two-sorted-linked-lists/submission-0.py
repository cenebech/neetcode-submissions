# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #temp starter node
        dummy = ListNode()
        current = dummy

        #while loop
        while list1 is not None and list2 is not None:
            #compare list1.val < list2.val:
            if list1.val < list2.val:

                #do something - attach node to list1
                current.next = list1

                #move node to the next candidat for list1
                list1 = list1.next    

            else:
                #do something but with list2
                current.next = list2
                list2 = list2.next

            current = current.next

        #if only list1 is left
        if list1 is not None:
            #do something -> move current.next to list1 node
            current.next = list1

        #if only list2 is lifet
        if list2 is not None:
            #do something
            current.next = list2

        return dummy.next
        