INTUTION:
1.FIRST TAKE TWO NODES ONE AS ODD AND OTHER AS EVEN 
2.ADD FIRST NODE FROM LL INTO THE ODD NODE
3.SECOND NODE INTO THE EVEN .
4.TAKE A VARAIBLE COUNTER AS C=2 
5.AFTER TAKE THE HEADS OF TWO EVEN AND ODD IN AN SEPARATE VARAIBLE BECOZ WHILE TRAVERSING LL WE LOSS THE POSITION OF HEADS OF TWO NODES
6.AND BECOME DIFFICULT TO ATTACH TWO ODD AND EVEN LL S
SPACE COMPLEXITY:O(N)
TIME COMPLEXITY:O(N)
---------------------------------CODE-------------------------------------------------------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None or head.next.next==None:
            return head
        oddptr=ListNode(head.val)
        evenptr=ListNode(head.next.val)
        odd=oddptr
        even=evenptr
        odd_head=odd
        even_head=even
        c=2 
        ptr=head.next.next 
        while ptr:
            c+=1 
            if c%2==0:
                n=ListNode(ptr.val)
                even.next=n
                even=even.next
            else:
                n=ListNode(ptr.val)
                odd.next=n
                odd=odd.next 
            if ptr.next ==None:
                odd.next=even_head
            ptr=ptr.next 
        return odd_head
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------
HOW TO GET SOL BY WITH SPACE COMPLEXITY :O(1)
