# LeetCode 412 - Fizz Buzz

## Problem Link
https://leetcode.com/problems/fizz-buzz/

## Problem Description
Given an integer `n`, return a string array `answer` (1-indexed) where:
- `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5
- `answer[i] == "Fizz"` if `i` is divisible by 3
- `answer[i] == "Buzz"` if `i` is divisible by 5
- `answer[i] == i` (as string) otherwise

## Solution Explanation
We iterate from 1 to n and check divisibility conditions in order of most restrictive first (15, then 3, then 5).

**Algorithm:**
1. Initialize empty list `answer`
2. For `i` from 1 to `n`:
   - If `i % 15 == 0`: append "FizzBuzz"
   - Else if `i % 3 == 0`: append "Fizz"
   - Else if `i % 5 == 0`: append "Buzz"
   - Else: append `str(i)`
3. Return `answer`

## Complexity Analysis
- **Time Complexity:** O(n) - Single loop from 1 to n
- **Space Complexity:** O(1) excluding output, O(n) including output

## Example
```python
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```