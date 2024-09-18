from collections import defaultdict, Counter
from typing import Optional, List

from data.linked_list import ListNode


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums = sorted(nums)
        nums.sort()
        return nums[len(nums)//2]


num = [3,2,3]
solution = Solution()
print(solution.majorityElement(num))
