---
layout: post
title: 446. Arithmetic Slices II - Subsequence
nav_order: 446
parent: Algorithms
grand_parent: LeetCode
---

# 446. [Arithmetic Slices II - Subsequence] (https://leetcode.com/problems/arithmetic-slices-ii-subsequence/)
Easy
{: .label .label-red }


### Python Solution


```python
from collections import defaultdict 

class Solution:

    def numberOfArithmeticSlices(self, nums):

        n = len(nums)

        total_count = 0  

        dp = [defaultdict(int) for i in range(n)]

        for i in range(1, n):

            for j in range(i):

                diff = nums[i] - nums[j]

                dp[i][diff] += 1  

                if diff in dp[j]:

                    dp[i][diff] += dp[j][diff]

                    total_count += dp[j][diff]

        return total_count
```

### Explanation
<div class = 'code-example' >
here we are using dynamic programming. we are creating a dp array with the length of the nums array. then we are iterating through the array and calculating the difference between the numbers. then we are adding the difference to the dp array. then we are checking if the difference is in the dp array. if it is, then we are adding the difference to the dp array. then we are adding the difference to the total count.
just watch neetcode's video on youtube.
</div>