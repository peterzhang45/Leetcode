class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for x in set(nums1):
            ans += [x] * min(nums1.count(x), nums2.count(x))
        return ans
