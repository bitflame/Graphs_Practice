from typing import Optional


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int):
        if not head: return None
        curr = head
        prev = None
        tail = curr
        counter = 0
        temp = None
        while self.have_next( curr, k):
            for i in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                counter += 1
            if counter == k:
                head = prev
                temp = curr
                prev = None
            else:
                tail.next = prev
                if temp:
                    tail = temp
                    temp = curr
                prev = None
        if tail: tail.next = curr
        return head

    def have_next(self, current: [ListNode], k: int):
        for i in range(k):
            if not current:
                return False
            current = current.next
        return True

    def print_list(self, head: [ListNode]):
        if not head:
            print(head)
            return
        while head.next:
            print(head.val, " ", end="")
            head = head.next
        print(head.val)


l1 = ListNode(1, None)
l1.next = ListNode(2, None)
l1.next.next = ListNode(3, None)
l1.next.next.next = ListNode(4, None)
l1.next.next.next.next = ListNode(5, None)
s = Solution()
s.print_list(s.reverseKGroup(l1, 2))
