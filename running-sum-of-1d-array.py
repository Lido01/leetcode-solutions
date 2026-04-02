class Solution(object):
    def runningSum(self, nums):
        """
        Time Complexity: O(n) - iterate through the list exactly once.
        Space Complexity: O(n) - create a new list to store the results.
        """
        results = []
        current_sum = 0
        
        for num in nums:
            current_sum += num
            results.append(current_sum)
            
        return results