class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map.keys():
                return [i, num_map[complement]]
            num_map[nums[i]] = i

        return []


nums = [2, 7, 11, 15, 5, 22, 87, 56, -11]
target = -9
solution = Solution()
print(solution.twoSum(nums, target))
