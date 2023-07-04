intuiton:
find given a ll is palindrome or not
brute force:
-------------------
=>take an empty array and add each ele in to the list 
=>and reverse the array and compare it with new array
=>if both same are return true else return fasle
time complexity:O(n)+O(n)
space complexity:O(n)
------------------------------------------------------------code-----------------------------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack=[]
        while head:
           stack.append(head.val)
           head=head.next
        if stack==stack[::-1]:
            return True 
        else:return False 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        
