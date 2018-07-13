# coding:utf-8
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = dict()
        for i, n in enumerate(nums):
            if s.get(target - n, None) is None:
                s[n] = i
            else:
                return sorted([s.get(target - n), i])
        return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))

