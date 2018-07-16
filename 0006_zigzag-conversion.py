# coding:utf-8


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        r = [[] for _ in range(numRows)]
        for i, c in enumerate(s):
            r[(numRows - 1) - abs((numRows - 1) - i % (2 * (numRows - 1)))].append(c)
        return "".join(["".join(t) for t in r])


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3))
    print(solution.convert("PAYPALISHIRING", 4))
