from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_lst = self.pre_order(root.left)
        right_lst = self.pos_order(root.right)

        return left_lst == right_lst

    def pre_order(self, root: Optional[TreeNode]):
        if not root:
            return [None]

        result = []
        result.extend(self.pre_order(root.left))
        result.extend(self.pre_order(root.right))
        result.append(root.val)
        return result

    def pos_order(self, root: Optional[TreeNode]):
        if not root:
            return [None]

        result = []
        result.extend(self.pos_order(root.right))
        result.extend(self.pos_order(root.left))
        result.append(root.val)
        return result


class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]):
        if not root:
            return True

        return self.isSame(root.left, root.right)

    def isSame(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        return self.isSame(left.left, right.right) and self.isSame(left.right, right.left)

# root = [1,2,2,null,3,null,3]

from collections import deque


def build_tree_from_list(values):
    if not values:
        return None

    # Create the root of the tree
    root = TreeNode(values[0])
    queue = deque([root])

    i = 1
    while i < len(values):
        current = queue.popleft()

        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)

        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)

        i += 1

    return root


def print_tree(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            print(node.val, end=' ')
            queue.append(node.left)
            queue.append(node.right)
        else:
            print("None", end=' ')
    print()


values = [1, 2, 2, None, 3, None, 3]
values = [1,2,2,3,4,4,3]
root = build_tree_from_list(values)

solution = Solution()
print(solution.isSymmetric(root))
# print(root)
# Print the tree to verify
# print_tree(root)

