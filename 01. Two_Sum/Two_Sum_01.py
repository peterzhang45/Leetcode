class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_list_len = len(nums)
        for i in range(0,my_list_len):
            m = target - nums[i]
            if m in nums:
                q = nums.index(m)
                if i != q:
                    break
        return[i, q]
