class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        results = 0
        
        # Continue until the number is fully reduced to 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            
            # Increment the step counter after every operation
            results += 1
            
        return results