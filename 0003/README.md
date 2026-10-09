# LeetCode 1823 - Find the Winner of the Circular Game

## Problem Link
https://leetcode.com/problems/find-the-winner-of-the-circular-game/

## Problem Description
There are `n` friends sitting in a circle numbered from 1 to n. Starting from the 1st friend, count `k` friends clockwise and remove the k-th friend. Continue counting from the next friend and repeat until one friend remains. Return the winner.

## Solution Explanation
Simulate the game using a list. Maintain a `next_index` pointer. In each round, calculate the index to remove using `(next_index + k - 1) % len(people)`, remove that person, and continue from that position.

**Algorithm:**
1. Create list `people = [1, 2, ..., n]`
2. Initialize `next_index = 0`
3. While more than 1 person remains:
   - `next_index = (next_index + k - 1) % len(people)`
   - Remove `people[next_index]`
4. Return the last remaining person

## Complexity Analysis
- **Time Complexity:** O(n²) - n rounds, each pop is O(n) in worst case
- **Space Complexity:** O(n) - List stores n people

## Example
```python
Input: n = 5, k = 2
Output: 3
Explanation: 
Round 1: Remove 2 -> [1,3,4,5]
Round 2: Remove 4 -> [1,3,5]
Round 3: Remove 1 -> [3,5]
Round 4: Remove 5 -> [3]
Winner: 3
```