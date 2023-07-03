intution :
=> given a loop of linked list find where loop starts 
approach:
1.first find is ll is loop or not
2.if it is looped ll
3.then start again from and check
=========================*CODE*=============================================================================================================
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head
        while  fast and fast.next:
            slow=slow.next 
            fast=fast.next.next 
            if slow==fast:
                slow=head 
                while slow!=fast:
                    slow=slow.next 
                    fast=fast.next
                return slow
        return None
-----------------------------------------------------------------------------------------------------------------------------------------
