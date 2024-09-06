from typing import Optional

from data.linked_list import ListNode
from data.tree_node import TreeNode


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, is_balance = self.heightCal(root)
        return is_balance

    def heightCal(self, root):
        if root is None:
            return 0, True
        left_height, is_balance = self.heightCal(root.left)
        if not is_balance:
            return -99, False

        right_height, is_balance = self.heightCal(root.right)
        if not is_balance:
            return -99, False

        if abs(left_height - right_height) <= 1:
            return max(left_height, right_height) + 1, True
        else:
            return -99, False


# l1 = [3, 9, 20, None, None, 15, 7]  # true


# l1 = [1, 2, 2, 3, 3, None, None, 4, 4]  # false
# l1 = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]  # false
l1 = [1, 2]  # true
root = TreeNode.build_tree_from_list(l1)

TreeNode.print_tree(root)

solution = Solution()
print(solution.isBalanced(root))
