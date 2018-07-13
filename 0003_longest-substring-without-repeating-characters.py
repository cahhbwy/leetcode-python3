# coding:utf-8
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p, q = 0, 0
        t = set()
        r = len(t)
        while q < len(s):
            if s[q] in t:
                while s[p] != s[q]:
                    t.remove(s[p])
                    p += 1
                p += 1
            else:
                t.add(s[q])
            q += 1
            r = max(len(t), r)
        return r


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
