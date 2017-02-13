class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (len(nums) <= 1):
            return False
        nums_dic = {}
        for i in range(len(nums)):
            if ((target - nums[i]) in nums_dic):
                return [nums_dic[target - nums[i]], i]
            else:
                nums_dic[nums[i]] = i
 
a = Solution()
nums = [3,2,4]
target = 6
print a.twoSum(nums,target)
