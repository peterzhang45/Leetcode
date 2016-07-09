class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pool = []
        size = len(nums)
        for i in range(size):
            if nums[i] not in pool:
                if nums.count(nums[i]) > n / 2:
                    return num[i]
                pool.append(num[i])
