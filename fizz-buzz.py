class Solution(object):
    def fizzBuzz(self, n):
        """
        Time Complexity: O(n)
        Space Complexity: O(1) (excluding the output list)
        """
        answer = []
        
        # start from 1 and go up to and including n
        for i in range(1, n + 1):
            # Check the most restrictive condition first (divisible by 15)
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                # Convert the integer to a string for the output
                answer.append(str(i))
                
        return answer