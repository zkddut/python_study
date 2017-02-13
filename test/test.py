class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums:
            return res
        max_pos = 2**len(nums)
        binary_format = '{0:0'+str(len(nums))+'b}'
        for i in range(max_pos):
            bin_sel = binary_format.format(i)
            tmp_res = []
            for j in range(len(bin_sel)):
                if str(bin_sel[j]) == '1':
                    tmp_res.append(nums[j])
            res.append(tmp_res)
        return res

a = Solution()
print (a.subsets([1,2,3]))
