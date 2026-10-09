# LeetCode 1893 - Check if All the Integers in a Range Are Covered

## Problem Link
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

## Problem Description
You are given a 2D integer array `ranges` and two integers `left` and `right`. Each `ranges[i] = [start_i, end_i]` represents an inclusive interval. Return `true` if each integer in the inclusive range `[left, right]` is covered by at least one interval in `ranges`. Otherwise, return `false`.

## Solution Explanation
We create a set of all integers covered by the intervals, then check if every integer from `left` to `right` exists in the set.

**Algorithm:**
1. Create empty set `covered_numbers`
2. For each `[start, end]` in `ranges`:
   - Add all integers from `start` to `end` to the set
3. For each integer from `left` to `right`:
   - If not in set, return `False`
4. Return `True`

## Complexity Analysis
- **Time Complexity:** O(m * k + n) where m = number of ranges, k = average range length, n = right - left + 1
- **Space Complexity:** O(m * k) - Set stores all covered integers

## Example
```python
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Integers 2,3,4,5 are all covered by the ranges.
```