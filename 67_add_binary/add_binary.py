from collections import defaultdict, Counter
from typing import Optional, List

from data.linked_list import ListNode


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        zero_len = abs(len(a) - len(b))
        str_zero = "0" * zero_len
        if len(a) < len(b):
            a = str_zero + a
        else:
            b = str_zero + b

        str_len = len(a)
        carry = "0"
        result_str = ''

        for i in range(str_len - 1, -1, -1):
            if a[i] == b[i]:
                if a[i] == "0":
                    carry = "0"
                else:
                    carry = "1"
                result_str = carry + result_str
            else:
                if carry == "0":
                    result_str = "1" + result_str
                else:
                    result_str = "0" + result_str

        return result_str if carry == "0" else carry + result_str



a = "11"
b = "1"
solution = Solution()
print(solution.addBinary(a, b))
