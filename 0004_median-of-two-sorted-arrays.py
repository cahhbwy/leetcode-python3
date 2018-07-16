# coding:utf-8
class Solution:
    def __init__(self):
        self.odd = True

    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums1) == 0:
            if self.odd:
                return nums2[k] / 1
            else:
                return (nums2[k] + nums2[k + 1]) / 2
        if k == 0:
            if self.odd:
                return min(nums1[0], nums2[0]) / 1
            else:
                self.odd = True
                return (min(nums1[0], nums2[0]) + self.findKth(nums1, nums2, 1)) / 2
        d = min(len(nums1) - 1, (k - 1) // 2)
        if nums1[d] < nums2[d]:
            return self.findKth(nums1[d + 1:], nums2, k - d - 1)
        else:
            return self.findKth(nums1, nums2[d + 1:], k - d - 1)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.odd = True if (len(nums1) + len(nums2)) % 2 == 1 else False
        return self.findKth(nums1, nums2, (len(nums1) + len(nums2) - 1) // 2)


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 6]
    nums2 = [3, 4, 7, 8]
    print(solution.findMedianSortedArrays(nums1, nums2))
