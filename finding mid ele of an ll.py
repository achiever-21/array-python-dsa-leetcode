brute force
=>in linkend lis we have to find mid ele of linked list 
=>first count the no nodes in ll
=>after finding the mid ele return 
time complexity:O(n)+O(n//2)
space complexity:O(1)
===================================================***code***=================================================================================================================
def mid(self,head):
  temp=head 
  c=0
  while head:
    c+=1
    head=head.next 
  mid=c//2+1 
  i=0
  while i<m:
    head=head.next 
    i+=1 
  return head 
  ===========================================================================**CODE***==========================================================================================
  TORTOISE APPROACH:
  =>in this approach we use two pointers one slow and other fast pointer 
  =>at first slow and fast are at same head but after
  =>faster pointer :
    step 1.it is two steps forward then slow
    step2.it is three steps forwad the slow 
    step2.same repaets at last when fast and fast.next 
time:O(n)
space:O(1)
=================================================================code=====================================================================================================
def mid(self,head):
  slow=head
  fast=head 
  while fast and fast.next:
    fast=fast.next.next 
    slow=slow.next 
  return slow
    
    
