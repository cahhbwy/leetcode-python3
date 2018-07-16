# coding:utf-8
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not -2 ** 31 <= x <= 2 ** 31 - 1:
            return 0
        s = str(x)
        if s[0] not in "0123456789":
            r = int(s[0] + "".join(reversed(s[1:])))
        else:
            r = int("".join(reversed(s)))
        if not -2 ** 31 <= r <= 2 ** 31 - 1:
            return 0
        else:
            return r


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(123))
    print(solution.reverse(-123))
    print(solution.reverse(120))
    print(solution.reverse(1534236469))
