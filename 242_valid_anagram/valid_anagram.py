class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_lst = [char for char in s]
        t_lst = [char for char in t]
        if len(s_lst) != len(t_lst):
            return False
        s_lst.sort()
        t_lst.sort()
        for i in range(len(s_lst)):
            if s_lst[i] != t_lst[i]:
                return False
        return True


class Solution2:
    class Solution(object):
        def isAnagram(self, s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            s_lst = [char for char in s]
            t_lst = [char for char in t]
            if len(s_lst) != len(t_lst):
                return False
            s_lst.sort()
            t_lst.sort()
            for i in range(len(s_lst)):
                if s_lst[i] != t_lst[i]:
                    return False
            return True