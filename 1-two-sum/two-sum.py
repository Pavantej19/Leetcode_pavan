class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i in range(len(nums)):
            num=nums[i]
            difference= target-num
            if difference in seen:
                return[seen[difference],i]
            seen[num]=i
sol=Solution()
result=sol.twoSum([2,7,11,15],9)
print(result)
        