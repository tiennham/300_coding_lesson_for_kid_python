from collections import defaultdict, Counter
from typing import Optional, List

from data.linked_list import ListNode
from data.tree_node import TreeNode
from data.utils import generate_random_integers


class Solution:
    def swap(self, nums: List[int], a: int, b: int):
        nums[a], nums[b] = nums[b], nums[a]
        return nums

    def merge_sort(self, nums: List[int]):
        if len(nums) == 1:
            return nums

        middle = (len(nums)//2)

        left_lst = nums[:middle]
        left_merged_lst = self.merge_sort(left_lst)

        right_lst = nums[middle:]
        right_merged_lst = self.merge_sort(right_lst)

        merged_lst = self.merge_lst(left_merged_lst, right_merged_lst)
        return merged_lst

    def merge_lst(self, lst_a, lst_b):
        merged_lst = []
        i = j = 0
        while i < len(lst_a) and j < len(lst_b):
            smallest = lst_a[i]
            if smallest < lst_b[j]:
                i += 1
            else:
                smallest = lst_b[j]
                j += 1
            merged_lst.append(smallest)

        merged_lst.extend(lst_b[j:])
        merged_lst.extend(lst_a[i:])

        return merged_lst



values = generate_random_integers(15)
print(values)
solution = Solution()
print(solution.merge_sort(values))
