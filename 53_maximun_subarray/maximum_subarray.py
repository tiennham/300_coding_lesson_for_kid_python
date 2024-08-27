class Solution:
    def maxSubArray(self, nums: List[int]):
        total = nums[0]
        res = 0

        for n in nums:
            if total < 0:
                total = 0
            total += n
            res = max(res, total)

        return res


# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # expected: 6
# nums = [1]  # expected 1
nums = [5, 4, -1, 7, 8]  # expected 23
# nums = [1, 2]  # expected 3
# nums = [8, -19, 5, -4, 20]  # expected 21
# nums = [3, -2, -3, -3, 1, 3, 0]  # expected 4
# nums = [1, 1, -2]  # expected 2

# nums = [-99, -1, -2, -3, -4]
# from data import nums
import time
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
solution = Solution()
print(solution.maxSubArray(nums))
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))



