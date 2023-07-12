Intuition
->we have to reverse the linkedlist of subparts where the no of nodes equal to k
->if the no of nodes is less than k then return same sublinkedlist
->first we divide solution into two parts by using recursion
1.first recursion part will do reverse the sub linked list
2.second recursion part will divide the linked list into sublinked list

Approach
->we have to reverse the linkedlist of subparts where the no of nodes equal to k
->if the no of nodes is less than k then return same sublinkedlist
->first we divide solution into two parts by using recursion
1.first recursion part will do reverse the sub linked list
2.second recursion part will divide the linked list into sublinked list
#firstrecursion part(reversing the linked list)
->take start and end of the linked list reverse the linked list
(read comments in code u can understand more detail how i reverse the linked list)
#second recursion

Complexity
Time complexity:
O(n)
Space complexity:
O(n/k)

Code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,start,end):
        #we have to add null to head.next 
        prev=None 
#curr=head 
#by each time changing their prev curr next positions 
#and changing the curr.next toprev pointer 
        curr=start 
        next=curr.next 
        while(prev!=end):
            curr.next=prev 
            prev=curr 
            curr=next
            if next!=None:
                next=curr.next 
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        while head==None or head.next==None and k==1:
            return head 
        c=1
        start=head
        end=head
    #dividing the linked list from head to at k th position 
        while c<=k-1:
            end=end.next 
            if end==None:
                return head 
            c+=1 
        nexthead=self.reverseKGroup(end.next,k)
        self.reverse(start,end)
        start.next=nexthead
        return end
        
        
            
        

                
