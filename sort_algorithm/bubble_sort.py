from collections import defaultdict, Counter
from typing import Optional, List

from data.linked_list import ListNode
from data.tree_node import TreeNode
from data.utils import generate_random_integers


class Solution:
    def swap(self, nums: List[int], a: int, b: int):
        nums[a], nums[b] = nums[b], nums[a]
        return nums

    def bubble_sort(self, nums: List[int]):
        for i in range(len(nums)):
            for j in range(len(nums) - (i+1)):
                if nums[j] > nums[j+1]:
                    self.swap(nums, j, j+1)

        return nums


values = generate_random_integers(25)
print(values)
solution = Solution()
print(solution.bubble_sort(values))
