from collections import defaultdict, Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:  # hmm, this way is look smarter but not good ad performance
        odd_letters = []
        palindrome_len = 0
        for c in s:
            if c in odd_letters:
                odd_letters.remove(c)
                palindrome_len += 2
            else:
                odd_letters.append(c)

        if odd_letters:
            palindrome_len += 1
        return palindrome_len



class MySolution:
    def longestPalindrome(self, s: str) -> int:
        letters_count = defaultdict(int)
        for letter in s:
            if letter not in letters_count:
                letters_count[letter] = 1
            else:
                letters_count[letter] += 1

        total_len = 0
        extra = False
        for key, val in letters_count.items():
            if val % 2 != 0:
                extra = True
                total_len += val-1
            else:
                total_len += val

        if extra:
            total_len += 1

        return total_len


s = "abccccdd"
solution = Solution()
print(solution.longestPalindrome(s))
