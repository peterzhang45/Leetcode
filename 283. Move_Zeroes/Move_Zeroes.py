class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            if nums[i] == 0:
                num.insert(len(nums), nums.pop())
