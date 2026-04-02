class Solution(object):
    def maximumWealth(self, accounts):
        """
        Time Complexity: O(m * n) - where m is rows and n is columns.
        Space Complexity: O(1) - store one integer (max_wealth).
        """
        max_wealth = 0
        
        for customer in accounts:
            # sum(customer) adds up all bank balances for one person
            current_wealth = sum(customer)
            
            # Update max_wealth if this person is richer
            if current_wealth > max_wealth:
                max_wealth = current_wealth
                
        return max_wealth