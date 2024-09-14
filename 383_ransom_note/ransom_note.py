from collections import defaultdict, Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for letter in ransomNote:
            if letter not in magazine:
                return False
            else:
                magazine.replace(letter, "", 1)

        return True

    def my_canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_letter_count = defaultdict(int)
        for r_letter in ransomNote:
            if r_letter in r_letter_count:
                r_letter_count[r_letter] += 1
            else:
                r_letter_count[r_letter] = 1

        m_letter_count = defaultdict(int)
        for m_letter in magazine:
            if m_letter in m_letter_count:
                m_letter_count[m_letter] += 1
            else:
                m_letter_count[m_letter] = 1

        if len(r_letter_count.keys()) > len(m_letter_count.keys()):
            return False

        for key, val in r_letter_count.items():
            if m_letter_count[key] < val:
                return False

        return True


r = "aa"
m = "aab"
solution = Solution()
print(solution.canConstruct(r, m))
