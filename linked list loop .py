intution:
---------------------------------------------------------------------------------------------------------------------------------------------------------------
141. Linked List Cycle
Easy
12.7K
1.1K
Companies
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
--------------------------------------------------------------------------------------------------------------------------------------------------------------
solution:
=>first taking empty list and storing all ele in that
=>if a node repeats more than once then we can say ll is forming a loop and return True 
=>else:retur false
time complexity:O(n)
space complexity:O(n)
=================================================================*CODE*===================================================================================================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d=[]
        while head:
            if head not in d:
                d.append(head)
            else:
                return True 
            head=head.next
        return False
========================================================================================================================================================================
2.optimized approach:
to decrease space complexity we use another approach:
=>in this solution we have to take constraints 
constraints:
The number of the nodes in the list is in the range [0, 104].
-10**5 <= Node.val <= 10**5
pos is -1 or a valid index in the linked-list.
=> we can say the value of each node is in btw -+10**5.
=>so by each time we can assign a number which greater than 10**5 and check it with next node if it has loop so repetition it comes to begining of ll and checks if the val we assigned sam eor not.
time complexity:O(n)
space complexity:O(1)
-------------------------------------------------------------------***CODE***--------------------------------------------------------------------------------------------------------------------
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val==10**6:
              return True
            head.val=10**6
            head=head.next
        return False
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3.optimized approach without changin the input
time complexity:O(n)
space complexity:O(1)
tortoise technique:
here we have to take two pointers slow and fast
slow is one step forward
fast is two steps forward 
example slow and fast two persons they r running faster runs if it is a loop he will meet slow where fast makes two rounds and slower will be one.
------------------------------------************code***********---------------------------------------------------------------------------------------------------------
User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        slow=head
        faster=head
        while slow and faster and faster.next:
            slow=slow.next 
            faster=faster.next.next 
            if slow==faster:
                return True 
        return False
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
