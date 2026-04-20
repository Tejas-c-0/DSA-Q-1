# Two Sum

## Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

---

## Approach
- Use a HashMap (dictionary) to store visited elements.
- For each element `x`, compute `target - x`.
- Check if the complement exists in the map.
- If yes → return indices.
- Else → store current element.

---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Key Insight
Instead of checking all pairs, we reduce search using a hashmap.
This is known as the **complement pattern**.

---

## Code
```python
def twoSum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return[]
  
