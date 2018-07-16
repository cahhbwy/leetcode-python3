# coding:utf-8


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.lstrip()
        if len(s) == 0:
            return 0
        if s[0] == '+':
            i = 1
            flag = True
        elif s[0] == '-':
            i = 1
            flag = False
        else:
            i = 0
            flag = True
        t = ""
        while i < len(s) and s[i] in "0123456789":
            t += s[i]
            i += 1
        if len(t) == 0:
            return 0
        r = int(t) if flag else -int(t)
        if r < -2 ** 31:
            return -2 ** 31
        elif r > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return r


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi("2147483648"))
    print(solution.myAtoi("42"))
    print(solution.myAtoi("   -42"))
    print(solution.myAtoi("4193 with words"))
    print(solution.myAtoi("words and 987"))
    print(solution.myAtoi("-91283472332"))
