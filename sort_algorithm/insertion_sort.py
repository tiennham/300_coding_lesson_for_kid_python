from collections import defaultdict, Counter
from typing import Optional, List

from data.linked_list import ListNode
from data.tree_node import TreeNode
from data.utils import generate_random_integers


class Solution:
    def swap(self, nums: List[int], a: int, b: int):
        nums[a], nums[b] = nums[b], nums[a]
        return nums

    def insertion_sort(self, nums: List[int]):
        for i in range(1, len(nums)):
            x = nums[i]
            pos = i - 1
            while pos >= 0 and nums[pos] >= x:
                nums[pos + 1] = nums[pos]
                pos -= 1
            nums[pos + 1] = x
        return nums


values = generate_random_integers()
print(values)
solution = Solution()
print(solution.insertion_sort(values))
