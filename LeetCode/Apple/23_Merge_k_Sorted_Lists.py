from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(first, second):
    head = ListNode(0)
    curr = head

    while first and second:
        if first.val < second.val:
            curr.next = first
            first = first.next
            curr = curr.next
        else:
            curr.next = second
            second = second.next
            curr = curr.next

    if first:
        curr.next = first
    if second:
        curr.next = second
    return head.next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            lists.append(merge(lists.pop(0), lists.pop(0)))
        return lists[0]









