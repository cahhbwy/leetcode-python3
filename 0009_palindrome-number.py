# coding:utf-8


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        p = x
        t = 0
        while p > 0:
            t = t * 10 + p % 10
            p = p // 10
        return x == t


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(121))
