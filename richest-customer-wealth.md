# LeetCode 1672 - Richest Customer Wealth

## Problem Link
https://leetcode.com/problems/richest-customer-wealth/

## Problem Description
You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount of money the `i-th` customer has in the `j-th` bank. Return the wealth that the richest customer has.
A customer's wealth is the sum of money they have in all their bank accounts. The richest customer is the one with the maximum wealth.

## Solution Explanation
We iterate through each customer's accounts, calculate their total wealth using `sum()`, and track the maximum wealth found.

**Algorithm:**
1. Initialize `max_wealth = 0`
2. For each customer in accounts:
   - Calculate `current_wealth = sum(customer)`
   - If `current_wealth > max_wealth`, update `max_wealth`
3. Return `max_wealth`

## Complexity Analysis
- **Time Complexity:** O(m * n) - m customers, n accounts each
- **Space Complexity:** O(1) - Only stores one integer

## Example
```python
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation: 
1st customer wealth = 1+2+3 = 6
2nd customer wealth = 3+2+1 = 6
Richest wealth = 6
```