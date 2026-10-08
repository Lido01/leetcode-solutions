class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        people = list(range(1, n + 1))
        next_index = 0
        while len(people) > 1:
            next_index = (next_index + k -1) % len(people)
            people.pop(next_index)
        return people[0]