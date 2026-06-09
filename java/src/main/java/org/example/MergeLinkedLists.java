package org.example;

import java.util.List;

public class MergeLinkedLists {
    public ListNode mergeTowLists(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;
        ListNode head;
        ListNode curr;
        if (list1.val < list2.val) {
            curr = list1;
            head = list1;
            if (list1.next != null) {
                list1 = list1.next;
            } else if (list2 != null) {
                head.next = list2;
                return head;
            } else {
                return head;
            }
        } else {
            curr = list2;
            head = list2;
            if (list2.next != null) {
                list2 = list2.next;
            } else if (list1 != null) {
                head.next = list1;
                return head;
            } else {
                return head;
            }
        }
        while (curr != null) {
            if (list1.val < list2.val) {
                curr.next = list1;
                curr = curr.next;
                if (list1.next != null) {
                    list1 = list1.next;
                } else if (list2 != null) {
                    curr.next = list2;
                    curr = curr.next;
                    return head;
                } else {
                    return head;
                }
            } else {
                curr.next = list2;
                curr = curr.next;
                if (list2.next != null) {
                    list2 = list2.next;
                } else if (list1 != null) {
                    curr.next = list1;
                    curr = curr.next;
                    return head;
                } else {
                    return head;
                }
            }
        }
        return head;
    }

    public ListNode reverseLinkedLists(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode before_left = dummy;
        for (int i = 0; i < left - 1; i++) {
            before_left = before_left.next;
        }
        ListNode tail = before_left.next;
        ListNode curr = tail;
        ListNode prev = null;
        for (int i = right; i >= left; i--) {
            ListNode next_node = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next_node;
        }
        before_left.next = prev;
        tail.next = curr;
        return dummy.next;
    }

    public static void main(String[] args) {
        MergeLinkedLists m = new MergeLinkedLists();
        ListNode l1 = new ListNode(1);
        l1.next = new ListNode(2);
        l1.next.next = new ListNode(3);
        l1.next.next.next = new ListNode(4);
        l1.next.next.next.next = new ListNode(5);
        System.out.println("ReverseLinkedLists Test 1 - Here is the result of reversing l1: ");
        ListNode res = m.reverseLinkedLists(l1, 2, 4);
        for (ListNode node = res; node != null; node = node.next) {
            if (node.next != null) System.out.print(node.val + "->");
            else System.out.println(node.val);
        }
        // do a test for one list empty and the other not
        ListNode list1 = new ListNode(1);
        list1.next = new ListNode(2);
        list1.next.next = new ListNode(3);

        ListNode list2 = new ListNode(1);
        list2.next = new ListNode(3);
        list2.next.next = new ListNode(4);

        ListNode result = m.mergeTowLists(list1, list2);
        System.out.print("Test 1 - expected: 1->1->2->3->3->4, actual: ");
        for (ListNode node = result; node != null; node = node.next) {
            if (node.next != null) System.out.print(node.val + "->");
            else System.out.println(node.val);
        }
        list1 = null;
        list2 = new ListNode(1);
        list2.next = new ListNode(3);
        list2.next.next = new ListNode(4);
        result = m.mergeTowLists(list1, list2);
        System.out.print("Test 2 - expected: 1->3->4, actual: ");
        for (ListNode node = result; node != null; node = node.next) {
            if (node.next != null) System.out.print(node.val + "->");
            else System.out.println(node.val);
        }
        list1 = new ListNode(1);
        list1.next = new ListNode(2);
        list1.next.next = new ListNode(4);
        list2 = new ListNode(1);
        list2.next = new ListNode(3);
        list2.next.next = new ListNode(4);
        result = m.mergeTowLists(list1, list2);
        System.out.print("Test 3 - expected: 1->1->2->3->4, actual: ");
        for (ListNode node = result; node != null; node = node.next) {
            if (node.next != null) System.out.print(node.val + "->");
            else System.out.println(node.val);
        }
    }

    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

}
