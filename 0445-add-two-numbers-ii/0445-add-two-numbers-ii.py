# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_l1 = []
        stack_l2 = []
        while l1:
            stack_l1.append(l1)
            l1 = l1.next
        while l2:
            stack_l2.append(l2)
            l2 = l2.next
        carry = 0
        head = None
        while stack_l1 or stack_l2:
            v1 = stack_l1.pop().val if stack_l1 else 0
            v2 = stack_l2.pop().val if stack_l2 else 0
            v = v1 + v2
            carry, v = divmod(v+carry, 10)
            temp = head
            head = ListNode(v)
            head.next = temp
        if carry:
            temp = head
            head = ListNode(carry)
            head.next = temp
        return head
        