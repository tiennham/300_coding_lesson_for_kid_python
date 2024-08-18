class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alpha_chars = [char for char in s if char.isalnum()]

        for idx in range(round(len(alpha_chars) / 2)):
            if alpha_chars[idx] != alpha_chars[len(alpha_chars) - 1 - idx]:
                return False

        return True



