# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            # Get the current values
            if l1:
                x = l1.val
            else:
                x = 0

            if l2:
                y = l2.val
            else:
                y = 0

            # Add the two digits and carry
            total = x + y + carry

            # Get the digit for the new node
            digit = total % 10

            # Get the carry for the next calculation
            carry = total // 10

            # Add new node to the result
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next