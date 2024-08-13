# Definition for singly-linked list.
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        temp1, temp2 = list1, list2
        head_node = ListNode(0)
        return_node = head_node
        while temp1 or temp2:
            if temp1 and temp2:
                if temp1.val < temp2.val:
                    head_node.next = ListNode(temp1.val)
                    temp1 = temp1.next
                else:
                    head_node.next = ListNode(temp2.val)
                    temp2 = temp2.next
            elif temp1:
                head_node.next = ListNode(temp1.val)
                temp1 = temp1.next
            else:
                head_node.next = ListNode(temp2.val)
                temp2 = temp2.next

            head_node = head_node.next

        return return_node.next


l1 = [1, 2, 4]
l1_node_1 = ListNode(1)
l1_node_2 = ListNode(2)
l1_node_4 = ListNode(4)
l1_node_1.next = l1_node_2
l1_node_2.next = l1_node_4

l2 = [1, 3, 4]
l2_node_1 = ListNode(1)
l2_node_3 = ListNode(3)
l2_node_4 = ListNode(4)
l2_node_1.next = l2_node_3
l2_node_3.next = l2_node_4

solution = Solution2()
merged_linkedlist: ListNode = solution.mergeTwoLists(l1_node_1, l2_node_1)

current_node = merged_linkedlist
list_str = []
while current_node:
    list_str.append(current_node.val)
    current_node = current_node.next

print(" => ".join(map(str, list_str)))
