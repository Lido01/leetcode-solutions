# LeetCode 1480 - Running Sum of 1d Array

## Problem Link
https://leetcode.com/problems/running-sum-of-1d-array/

## Problem Description
Given an array `nums`, return the running sum of `nums`.
The running sum of an array is `runningSum[i] = sum(nums[0]...nums[i])`.

## Solution Explanation
We iterate through the array once, maintaining a running total (`current_sum`). For each element, we add it to the running total and append the result to our output array.

**Algorithm:**
1. Initialize an empty `results` list and `current_sum = 0`
2. For each number in `nums`:
   - Add the number to `current_sum`
   - Append `current_sum` to `results`
3. Return `results`

## Complexity Analysis
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(n) - Output array stores n elements

## Example
```python
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is [1, 1+2, 1+2+3, 1+2+3+4]
```