from collections import defaultdict, Counter
from typing import Optional, List

from data.linked_list import ListNode
from data.tree_node import TreeNode
from data.utils import generate_random_integers


class Solution:
    def swap(self, nums: List[int], a: int, b: int):
        nums[a], nums[b] = nums[b], nums[a]
        return nums

    def selection_sort(self, nums: List[int]):
        for i in range(len(nums)):
            min_pos = i
            for j in range(i+1, len(nums)):
                if nums[j] > nums[min_pos]:
                    min_pos = j

            self.swap(nums, i, min_pos)
        return nums


values = generate_random_integers(25)
print(values)
solution = Solution()
print(solution.selection_sort(values))
