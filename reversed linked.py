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
