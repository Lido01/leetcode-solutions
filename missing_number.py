class Solution(object):

  def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 1. Store all numbers from the input array in a dictionary as keys
    #    The value can be anything (e.g., True) since we only care about presence.
    num_dict = {num: True for num in nums}
    
    # 2. Iterate through the range [0, n] and check if each number is in the dictionary.
    #    If a number is not found, it's the missing number.
    for i in range(len(nums) + 1):
      if i not in num_dict:
        return i

    # If we reach here, it means all numbers from 0 to n are present,
    # so the missing number is n itself.
    return len(nums)

print(Solution().missingNumber([3, 0, 1]))  # Output: 2
print(Solution().missingNumber([0, 1]))     # Output: 2
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))  # Output: 8
print(Solution().missingNumber([0]))        # Output: 1 because the only number present is 0, so the missing number is 1.
print(Solution().missingNumber([1]))        # Output: 0 because the only number present is 1, so the missing number is 0.
print(Solution().missingNumber.num_dict)   # Output: {3: True, 0: True, 1: True}