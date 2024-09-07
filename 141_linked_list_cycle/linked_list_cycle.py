class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_node = head
        fast_node = head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

            if slow_node == fast_node:
                return True

        return False

    def my_has_cycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        checked_nodes = []
        current = head.next
        while current:
            if current in checked_nodes:
                return True
            checked_nodes.append(current)
            current = current.next

        return False

    def my_hasCycle_2(self, head: Optional[ListNode]) -> bool:
        # next_lst = []
        current_node = head
        while current_node:
            if current_node.val is None:
                return True
            temp_node = current_node
            current_node = current_node.next
            temp_node.val = None

        return False
