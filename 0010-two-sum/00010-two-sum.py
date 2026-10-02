class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = defaultdict()

        for idx in range(len(nums)):
            if nums[idx] in diff:
                return [diff[nums[idx]], idx]
            
            diff[target - nums[idx]] = idx

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
