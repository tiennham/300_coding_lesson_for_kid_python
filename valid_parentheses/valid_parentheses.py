# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        op_pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        o_stack = []
        for c in s:
            if c not in op_pairs.keys() and c not in op_pairs.values():
                continue

            if c in op_pairs.keys():
                o_stack.append(c)

            if c in op_pairs.values():
                if not o_stack:
                    return False
                last_o = o_stack.pop()
                if op_pairs[last_o] != c:
                    return False

        if o_stack:
            return False

        return True


solution = Solution()
s = "(((fasf[fafsdfasf{dffwrwegt}ertvrv]rvrcwer))"
print(solution.isValid(s))  # False

s = "((fasf[fafsdfasf{dffwrwegt}ertvrv]rvrcwer))"
print(solution.isValid(s))  # True

s = "((fasf[fafsdfasf{dffwrwegt}ertvrv]rvrcwer))]"
print(solution.isValid(s))  # False

