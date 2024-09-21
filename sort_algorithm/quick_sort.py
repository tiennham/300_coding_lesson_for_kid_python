from collections import defaultdict, Counter
from typing import Optional, List

from data.linked_list import ListNode
from data.tree_node import TreeNode


class Solution:
    def swap(self, nums: List[int], a: int, b: int):
        nums[a], nums[b] = nums[b], nums[a]
        return nums

    def quick_sort(self, nums: List[int], left: int, right: int):
        l_side, r_side = left, right
        pivot = nums[(left + right) // 2]
        while l_side <= r_side:
            while nums[l_side] < pivot:
                l_side += 1

            while nums[r_side] > pivot:
                r_side -= 1

            if l_side <= r_side:
                self.swap(nums, l_side, r_side)
                l_side += 1
                r_side -= 1

        if left < r_side:
            self.quick_sort(nums, left, r_side)

        if right > l_side:
            self.quick_sort(nums, l_side, right)

        return nums


values = [1, 2, 102, 201, 111, 99, 3, 1, 7, 9, 33, 22, 7, 1, 0, 5, 89]
solution = Solution()
print(solution.quick_sort(values, 0, len(values) - 1))
