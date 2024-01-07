---
layout: post
title: 238. Product of Array Except Self
nav_order: 238
parent: Algorithms
grand_parent: LeetCode
---

# 238. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
Medium
{: .label .label-purple }


### Python Solution


```python
class Solution:
    def productExceptSelf(self, nums):
        product_arr = [0]*(len(nums)+1)

        tracker = 0

        for i in range(tracker):
            product_arr[tracker]*=i
        
        for j in range(tracker, len(nums)+1):
            product_arr[tracker]*=j

```

### Explanation
<div class = 'code-example' >
unfinished
</div>