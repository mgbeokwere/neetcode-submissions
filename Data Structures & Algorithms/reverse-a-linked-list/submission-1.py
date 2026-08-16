# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head, None)

    def helper(self, curr, prev):
        if curr == None:
            return prev
        secondParam = curr.next # we have to have a reference to the next in line before we redirect what was referencing it

        curr.next = prev

        

        return self.helper(secondParam, curr)
        