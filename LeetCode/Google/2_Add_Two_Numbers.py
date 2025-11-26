from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def parse(curr):
    num = ""
    while curr:
        num += str(curr.val)
        curr = curr.next
    return int(num[::-1])


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        data = str(parse(l1) + parse(l2))[::-1]
        head = ListNode()
        curr = head
        for i in range(len(data)):
            curr.next = ListNode(int(data[i]))
            curr = curr.next
        return head.next






