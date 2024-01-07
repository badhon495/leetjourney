---
layout: post
title: 347. Top K Frequent Elements
parent: Algorithms
grand_parent: LeetCode
has_children: false
nav_order: 300
---

# 347. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
Medium
{: .label .label-purple }


### Python Solution


```python
class Solution:
    def topKFrequent(self, nums, k):
        container = [[] for i in range(len(nums)+1)] #doing bucket sort
        real = []
        for i in (set(nums)):
            container[nums.count(i)].append(i) # appending the count of the number to the container

        for i in range(len(nums), -1, -1): # iterating from the end of the container as we want the most frequent numbers
            if container[i] != [] and k > 0:
                real.extend(container[i]) # extending the real array with the numbers in the container
                k -= len(container[i]) # subtracting the length of the container from k because we want the top k frequent numbers
        return real
```

### Explanation
<div class = 'code-example' >
here we are using bucket sort. we are creating a container with the length of the nums array. then we are appending the count of the number to the container. then we are iterating from the end of the container as we want the most frequent numbers. then we are extending the real array with the numbers in the container. then we are subtracting the length of the container from k because we want the top k frequent numbers.
</div>
