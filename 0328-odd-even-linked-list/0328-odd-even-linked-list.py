# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root1=ListNode(0)
        root2=ListNode(0)
        root=root2
        t=root1
        count=0
        while head:
            if count%2!=0:
                root1.next=ListNode(head.val)
                root1=root1.next
            else:
                root2.next=ListNode(head.val)
                root2=root2.next
            count+=1
            head=head.next
        root2.next=t.next
        return root.next
        