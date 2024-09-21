from collections import defaultdict, Counter
from typing import Optional, List

from data.linked_list import ListNode
from data.tree_node import TreeNode


class Solution:
    def swap(self, nums: List[int], a: int, b: int):
        nums[a], nums[b] = nums[b], nums[a]
        return nums

    def buble_sort(self, nums: List[int]):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] > nums[i]:
                    self.swap(nums, i, j)
        return nums


values = [99, 39, 90, 44, 77, 298, 775, 4, 6, 247]
solution = Solution()
print(solution.buble_sort(values))
