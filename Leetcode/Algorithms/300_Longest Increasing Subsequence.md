---
layout: post
title: 300. Longest Increasing Subsequence
parent: Algorithms
grand_parent: LeetCode
nav_order: 300
---

# 300. [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
Medium
{: .label .label-purple }


### Python Solution


```python
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums):

        sub = []
        for num in nums:
            i = bisect_left(sub, num) # find the right position to insert num
            if i == len(sub): # check if we are at right position or not. If yes, append num to sub. else, replace the value at i with num
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)
```

### Explanation
<div class = 'code-example' >
here bisect_left is used, to find the right position to insert num. bisect left uses binary search to find the right position. it works in left to right. as all the number in sub is in incresing order and right place, so it is will be the best case and time complexity will be O(nlogn).
</div>