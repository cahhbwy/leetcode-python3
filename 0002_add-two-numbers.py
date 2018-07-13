# coding:utf-8
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a, b = l1, l2
        n = a.val + b.val
        a = a.next
        b = b.next
        r = ListNode(n % 10)
        p = r
        while a is not None or b is not None:
            if a is None:
                x = 0
            else:
                x = a.val
                a = a.next
            if b is None:
                y = 0
            else:
                y = b.val
                b = b.next
            if n >= 10:
                n = x + y + 1
            else:
                n = x + y
            p.next = ListNode(n % 10)
            p = p.next
        if n >= 10:
            p.next = ListNode(1)
        return r


if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    r = solution.addTwoNumbers(l1, l2)
    p = r
    while p.next is not None:
        print("{}->".format(p.val), end="")
        p = p.next
    print(p.val)
