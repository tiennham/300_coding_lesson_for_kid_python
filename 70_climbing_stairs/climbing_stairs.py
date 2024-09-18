from collections import defaultdict, Counter


class Solution:
    def climbStairs(self, n: int):
        return self.climbHelper(n, {})

    def climbHelper(self, n: int, memorize: dict[int, int]):
        if n == 0 or n == 1:
            return 1
        if n not in memorize:
            memorize[n] = self.climbHelper(n - 1, memorize) + self.climbHelper(n - 2, memorize)
        return memorize[n]


class Solution3:
    def climbStairs(self, n: int, path: list) -> int:
        path.append(n)
        if n == 0 or n == 1:
            if n == 1:
                path.append(0)
            str_path = ""
            for i in range(len(path)):
                if path[i] != 0 and i < len(path) - 1:
                    str_path += str(path[i] - path[i + 1])
            print(str_path)
            return 1
        path1 = path.copy()
        path2 = path.copy()
        return self.climbStairs(n-1, path1) + self.climbStairs(n-2, path2)


class Solution2:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        print(memo)
        return memo[n]


n = 7
solution = Solution()
# print(solution.climbStairs(n, []))
print(solution.climbStairs(n))

