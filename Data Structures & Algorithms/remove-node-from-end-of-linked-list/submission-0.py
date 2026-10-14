# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        itr = head
        while itr:
            length += 1
            itr = itr.next
        if n == length:
            return head.next

        remove = length - n
        prev, curr = head, head.next

        for _ in range(remove - 1):
            prev = prev.next
            curr = curr.next

        prev.next = curr.next
        return head
        
        