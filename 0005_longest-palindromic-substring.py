# coding:utf-8


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        result = ""
        while i < len(s):
            p = i
            q = i
            while q < len(s) and s[q] == s[p]:
                q += 1
                i += 1
            q -= 1
            i -= 1
            while p >= 0 and q < len(s) and s[p] == s[q]:
                p -= 1
                q += 1
            if len(result) < q - p - 1:
                result = s[p + 1:q]
            i += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("a"))
    print(solution.longestPalindrome("cbbd"))
