from typing import Optional


class ListNode:
    def __init__(self, val:int=0,next:ListNode=None):
        self.val=val
        self.next=next
class Solution:
    def RotateList(self,head:Optional[ListNode],k:int)->Optional[ListNode]:
        end = head
        count = 0
        while end:
            end=end.next
            count+=1
        tail = head
        for i in range (count-k-1):
            tail=tail.next


    def print_list(self,node:Optional[ListNode]):
        while node.next:
            print(node.val,end="->")
            node=node.next
        print(node.val)

l1 = ListNode(1, ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
s = Solution()
s.print_list(l1)
s.RotateList(l1,1)