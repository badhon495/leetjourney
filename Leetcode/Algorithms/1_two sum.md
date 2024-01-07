---
layout: post
title: 1. Two Sum
nav_order: 1
parent: Algorithms
grand_parent: LeetCode
---

# 1. [Two Sum](https://leetcode.com/problems/two-sum/)
Easy
{: .label .label-green }


### Python Solution


```python
class Solution(object):
    def twoSum(self, nums, target):
        new_arr = []  # took new array to store index
        for i in range(len(nums)+1):
            # subtracted target with nums[i] to find the other number
            find = target - nums[i]
            if find in nums[i+1:]:  # checked if the other number is in the array
                new_arr.append(i)  # added the index of the first number
                # found the index of the other number
                new_idx = nums[i+1:].index(find)
                # added the index of the other number
                new_arr.append(new_idx+i+1)
                return new_arr
```
### Explanation
<div class = 'code-example' >
it can be done without using built-in index function. just append the substructed number on the new array and after each iteration check if the number is in the new array. if it is, then return the index of the number and the index of the substructed number.
</div>