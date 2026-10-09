# LeetCode 1342 - Number of Steps to Reduce a Number to Zero

## Problem Link
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

## Problem Description
Given an integer `num`, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

## Solution Explanation
We use a while loop to repeatedly apply the operations until the number becomes 0, counting each step.

**Algorithm:**
1. Initialize `steps = 0`
2. While `num > 0`:
   - If `num` is even: `num = num / 2`
   - Else: `num = num - 1`
   - Increment `steps`
3. Return `steps`

## Complexity Analysis
- **Time Complexity:** O(log n) - Number reduces by at least half every two steps
- **Space Complexity:** O(1) - Constant extra space

## Example
```python
Input: num = 14
Output: 6
Explanation:
Step 1) 14 is even -> 14 / 2 = 7
Step 2) 7 is odd -> 7 - 1 = 6
Step 3) 6 is even -> 6 / 2 = 3
Step 4) 3 is odd -> 3 - 1 = 2
Step 5) 2 is even -> 2 / 2 = 1
Step 6) 1 is odd -> 1 - 1 = 0
```