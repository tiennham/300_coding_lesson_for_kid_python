from collections import defaultdict, Counter
from typing import Optional, List

from data.linked_list import ListNode


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1

            if j >= 0:
                carry += int(b[j])
                j -= 1

            s.append(str(carry % 2))
            carry //= 2

        return "".join(reversed(s))

    def learn_1_addBinary(self, a: str, b: str) -> str:
        res = int(a, 2) + int(b, 2)
        print(res)
        return str(bin(res)[2:])


class MySolution:
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
                result_str = carry + result_str
                if a[i] == "0":
                    carry = "0"
                else:
                    carry = "1"
            else:
                if carry == "0":
                    result_str = "1" + result_str
                else:
                    result_str = "0" + result_str

        return result_str if carry == "0" else carry + result_str


a = "1010"
b = "1011"
solution = Solution()
print(solution.addBinary(a, b))
