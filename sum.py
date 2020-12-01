class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # head1=l1
        # num1=list()
        # while head1:
        #     num1.append(str(head1.val))
        #     head1=head1.next
        # head2=l2
        # num2=list()
        # while head2:
        #     num2.append(str(head2.val))
        #     head2=head2.next

        # num1=int(''.join(num1[::-1]))
        # num2=int(''.join(num2[::-1]))

        # num=str(num1+num2)[::-1]

        # l3=ListNode(num[0])
        # head=l3
        # for i in range(1,len(num)):
        #     head.next=ListNode(num[i])
        #     head=head.next
        # return l3
        # 因为是逆序排列，所以可以直接从头向后加，有进位的就进位
        p1 = l1
        p2 = l2
        if not p1:
            return p2
        if not p2:
            return p1
        if p1.val+p2.val>9:
            flag=1
            num=p1.val+p2.val-10
        else:
            flag=0
            num=p1.val+p2.val
        l3=ListNode(num)
        p3=l3
        p1=p1.next
        p2=p2.next
        while p1 and p2:
            if p1.val+p2.val+flag>9:
                flag=1
                num=p1.val+p2.val+flag-10
            else:
                flag=0
                num=p1.val+p2.val+flag
            p3.next=ListNode(num)
            p3=p3.next
            p1=p1.next
            p2=p2.next
        if p1:
            p3.next=p1
        if p2:
            p3.next=p2
        return l3
