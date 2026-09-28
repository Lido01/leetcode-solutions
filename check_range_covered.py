class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        # Create a set to store all integers covered by the ranges
        covered_numbers = set()
        
        # Loop through each interval and add its numbers to the set
        for start, end in ranges:
            for num in range(start, end + 1):
                covered_numbers.add(num)
                
        # Check if every integer from left to right is present in the set
        for target in range(left, right + 1):
            if target not in covered_numbers:
                return False
                
        return True
