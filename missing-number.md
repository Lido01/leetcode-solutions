# LeetCode 268 - Missing Number

## Problem Link
https://leetcode.com/problems/missing-number/

## Problem Description
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

## Solution Explanation
We use a hash set (dictionary) to store all numbers from the input array for O(1) lookup. Then we iterate through the range `[0, n]` and return the first number not found in the set.

**Algorithm:**
1. Create a dictionary `num_dict` with all numbers from `nums` as keys
2. Iterate `i` from 0 to `len(nums)` (inclusive)
3. If `i` not in `num_dict`, return `i`
4. If all found, return `len(nums)` (edge case)

## Complexity Analysis
- **Time Complexity:** O(n) - One pass to build dict, one pass to check range
- **Space Complexity:** O(n) - Dictionary stores n elements

## Example
```python
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3, range is [0,3]. Missing number is 2.
```