intution:
=>first we have to observe to reverse an array we just need to chnage the pointers 
=>keep the last pointer to first node of an ll.
=>and first node link adress to 2nd and to 3rd repeat same process.
=>for this we need a temp pointer while do swapping adress of the nodes.
time complexity :O(n)
space complexity:O(1)
==============================================================================================================================================================================
code:
def reverse(self,head):
  curr=head
  prev=None
  while curr!=None:
    temp=curr.next 
    curr.next=None 
    prev=current
    current=temp 
  return prev
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
opyimized approach:
------------------
1.HOW CAN WE SOLVE THIS PROBLEM BY O(1) SPACE AND O(N) TIME COMPLEXITY.
2.PALINDROME MEANS HALF OF THE FIRST PART EQUAL TO SECOND HALF OF AFTER REVERSING THE SECOND HALF
3.SO SIMPLY WE CAN REVERSE THE SECOND HALF LINKED LIST AND CHECK IT WITH FIRST PART
4.OK WE GOT BUT HOW TO FIND THE MID OF THE LL BY SIMPLY USING TORTOISE TECHNIQUE FAST AND SLOW POINTER 
5.BY USING THAT FIND MID AND REVRSE THE SECOND HALF THE ARRAY 
6.CHECK IT WITH FIRST HALF OF THE ARRAY
7.IF BOTH ARE EQUAL THEN RETURN TRUE 
-----------------------------------------------------------------------------CODE----------------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
    
      fast=head
      slow=head
      while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
          break 
      # revrse second part of an array
      # remmber one trick when our u try to find revrse of an ll
       # just remmber prev,curr,temp
       curr=slow
        prev=None
        while curr:
          temp=curr.next 
          curr.next=prev
          prev=curr
          curr=temp
        # and take two pointers first is head of ll
        # and second is head of second part of ll
        slow=head
        fast=prev 
        while slow and fast:
          if slow.val!=fast.val:
            return False
          slow=slow.next
          fast=fast.next
      return True 
-----------------------------------------------------------------------------------------------------

          

