---
layout: post
title: 2125. Number of Laser Beams in a Bank
parent: Algorithms
grand_parent: LeetCode
has_children: false
nav_order: 2125
---

# 2125. [Number of Laser Beams in a Bank](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/)
Medium
{: .label .label-purple }


### Python Solution

```python
class Solution(object):
    def numberOfBeams(self, bank):

        total = 0
        # count the number of 1s in the first element of the array
        prev_count = bank[0].count('1')

        for i in range(1, len(bank)):
            # count the number of 1s in the next element of the array
            new_count = bank[i].count('1')

            if new_count > 0:  # if the new count is greater than 0
                # multiply the previous count with the new count and add it to the total
                total += (prev_count*new_count)
                prev_count = new_count  # assign the new count to the previous count

        return total
```

### Explanation
<div class = 'code-example' >
here we are counting the number of 1s in the first element of the array. then we are iterating through the array and counting the number of 1s in the next element of the array. then we are multiplying the previous count with the new count and adding it to the total. then we are assigning the new count to the previous count.
</div>
