# LeetCode 2460 - Apply Operations to an Array

## Problem Link
https://leetcode.com/problems/apply-operations-to-an-array/

## Problem Description
You are given a 0-indexed array `nums` of size `n` consisting of non-negative integers. Apply the following operations sequentially:
1. If `nums[i] == nums[i + 1]`, multiply `nums[i]` by 2 and set `nums[i + 1]` to 0
2. After all operations, shift all 0's to the end while maintaining relative order of non-zero elements

Return the resulting array.

## Solution Explanation
Two-pass approach:
1. **Apply operations:** Iterate through array, if adjacent elements are equal, double the first and zero the second
2. **Shift zeros:** Collect all non-zero elements, then append zeros at the end

**Algorithm:**
1. For i from 0 to n-2:
   - If `nums[i] == nums[i+1]`: `nums[i] *= 2`, `nums[i+1] = 0`
2. Create result list with non-zero elements
3. Append zeros to match original length
4. Return result

## Complexity Analysis
- **Time Complexity:** O(n) - Two passes through array
- **Space Complexity:** O(n) - Result array

## Example
```python
Input: nums = [1,2,2,1,1,0]
Output: [1,4,2,0,0,0]
Explanation:
Step 1: [1,4,0,2,0,0] (apply operations)
Step 2: [1,4,2,0,0,0] (shift zeros)
```