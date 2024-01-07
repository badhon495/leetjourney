---
layout: post
title: 2610. Convert an Array Into a 2D Array With Conditions
parent: Algorithms
grand_parent: LeetCode
has_children: false
nav_order: 2610
---

# 2610. [Convert an Array Into a 2D Array With Conditions](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/)
Medium
{: .label .label-purple }




### Python Solution

```python
from copy import deepcopy as copy # importing it for deep copy

class Solution(object):
    def findMatrix(self, nums):
        container = []
        while len(nums) != 0:
            temp = copy(nums) # deep copy of nums
            new_arr = []
            for i in nums:
                if i not in new_arr:
                    new_arr.append(i) # appending the number to the new array
                    temp.remove(i) # removing the number from the temp array
                else:
                    continue

            container.append(new_arr)
            nums = temp # assigning temp to nums
        return container
```

#### Explanation
<div class = 'code-example' >
this not the best solution. it can be done in a better way. but this is what i came up with.
</div>