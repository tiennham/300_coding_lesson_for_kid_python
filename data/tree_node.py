from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
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

    @staticmethod
    def print_tree(root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.val))
            if root.left is not None or root.right is not None:
                if root.left:
                    TreeNode.print_tree(root.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if root.right:
                    TreeNode.print_tree(root.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


