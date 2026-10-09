# LeetCode 2 - Add Two Numbers

## Problem Link
https://leetcode.com/problems/add-two-numbers/

## Problem Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit. Add the two numbers and return the sum as a linked list.

## Solution Explanation
We simulate the addition process digit by digit, maintaining a carry. We create a new linked list for the result.

**Algorithm:**
1. Create dummy head node and `current` pointer
2. Initialize `carry = 0`
3. While `l1` or `l2` or `carry` exists:
   - Get values from current nodes (0 if None)
   - Calculate `total = x + y + carry`
   - Create new node with `digit = total % 10`
   - Update `carry = total // 10`
   - Advance pointers
4. Return `dummy.next`

## Complexity Analysis
- **Time Complexity:** O(max(m, n)) - m, n are lengths of lists
- **Space Complexity:** O(max(m, n)) - Result list length

## Example
```python
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
```