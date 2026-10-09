# LeetCode 1 - Two Sum

## Problem Link
https://leetcode.com/problems/two-sum/

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume exactly one solution exists, and you may not use the same element twice.

## Solution Explanation
The file contains two approaches:

### Approach 1: Hash Map (Optimal) - O(n)
Use a dictionary to store `target - num` as key and index as value. For each number, check if it exists in the dictionary.

**Algorithm:**
1. Initialize empty dict `diff`
2. For each index `idx` and value `num` in `nums`:
   - If `num` in `diff`: return `[diff[num], idx]`
   - Else: `diff[target - num] = idx`

### Approach 2: Brute Force - O(n²)
Check all pairs of indices.

**Algorithm:**
1. For each `i` from 0 to n-1:
   - For each `j` from i+1 to n-1:
     - If `nums[i] + nums[j] == target`: return `[i, j]`

## Complexity Analysis
- **Hash Map:** Time O(n), Space O(n)
- **Brute Force:** Time O(n²), Space O(1)

## Example
```python
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```