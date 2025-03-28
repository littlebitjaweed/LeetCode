class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        while head and head.val == val:
            head = head.next

        slow = head
        while slow and slow.next:
            if slow.next.val == val:
                slow.next = slow.next.next     
            else:
                slow = slow.next 
        
        return head
