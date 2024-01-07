---
layout: post
title: 49. Group Anagrams
nav_order: 49
parent: Algorithms
grand_parent: LeetCode
---

# 49. [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
Medium
{: .label .label-purple }


### Python Solution


```python 
class Solution:
    def groupAnagrams(self, strs):
        container = {}
        for word in strs:
            sorted_word = str(''.join(sorted(word))) # soring the word and converting it to string
            if sorted_word not in container.keys(): # if the sorted word is not in the container, add it to the container and because of that we are able to group the anagrams
                container[sorted_word] = [word]
            else:
                container[sorted_word].append(word)

        return container.values()
```

### Explanation
<div class = 'code-example' >
read the fucking comments
</div>