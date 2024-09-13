# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version == 2


class Solution:
    first_bad_ver = 0

    def firstBadVersion(self, n: int) -> int:
        self.find_first_bad_ver(0, n)
        return self.first_bad_ver

    def find_first_bad_ver(self, first, last):
        if first > last:
            return
        middle = int((first + last) / 2)
        is_bad = isBadVersion(middle)
        if is_bad:
            self.first_bad_ver = middle
            return self.find_first_bad_ver(first, middle - 1)
        else:
            return self.find_first_bad_ver(middle + 1, last)


n = 2
solution = Solution()
print(solution.firstBadVersion(n))
