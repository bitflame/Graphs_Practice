from typing import Optional


class ListNode:
    def __init__(self, val: Optional[int] = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def modiffied_rll(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        dummy = None
        while current != None:
            dummy = ListNode(current.val, dummy)
            current = current.next
        return dummy

    def rev_linked_list(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        dummy = None
        while current != None:
            while current.val >= left and current.val <= right:
                dummy = ListNode(current.val, dummy)
                if current.val == left:
                    left_bookmark = dummy
                current = current.next
                if current.val > right:
                    left_bookmark.next = current
                    break
            current = current.next
        head.next = dummy
        return head

    def print_list(self, l: Optional[ListNode]) -> None:
        while l != None:
            if l.next != None:
                print(l.val, "->", end=' ')
            else:
                print(l.val)
            l = l.next

    def reverse_linked_list(self, head: Optional[ListNode], left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        before_left = dummy
        # walk to just before left
        for _ in range(left-1):
            before_left=before_left.next
        tail=before_left.next
        curr = tail
        prev = None
        for _ in range(right-left+1):
            next_node = curr.next
            curr.next=prev
            prev = curr
            curr=next_node
        before_left.next = prev
        tail.next=curr
        return dummy.next

    def testing(self, head:[ListNode], left:int, right:int):
        dummy = ListNode(0)
        dummy.next = head
        before_left = dummy
        for _ in range(left-1):
            before_left=before_left.next
        tail = before_left.next
        curr = tail
        prev = None
        for _ in range(right-left+1):
            next_node = curr.next
            curr.next=prev
            prev = curr
            curr = next_node
        tail.next = curr
        before_left.next = prev
        return dummy.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
s = Solution()
s.modiffied_rll(l1, 0, 5)
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
result = s.rev_linked_list(l1, 2, 4)
s.print_list(result)
# write a test case for left and right equal to 1 and list of 3 and 5 head = [3, 5]
l1 = ListNode(3)
l1.next = ListNode(5)
result = s.rev_linked_list(l1, 1, 1)
print("Test 2 - expected [3, 5], actual: ",end='')
s.print_list(result)
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
result = s.reverse_linked_list(l1, 2, 4)
s.print_list(result)
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
result = s.testing(l1, 2, 4)
s.print_list(result)