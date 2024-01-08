---
layout: post
title: 938. Range Sum of BST
nav_order: 938
parent: Algorithms
grand_parent: LeetCode
---

# 938. [Range Sum of BST] (https://leetcode.com/problems/range-sum-of-bst/)
Easy
{: .label .label-green }


### Python Solution


```python
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
   
        if not root: # if root is null / base case
            return 0 
        if root.val>high: # if root value is greater than high
            return self.rangeSumBST(root.left, low, high)
        if root.val<low:
            return self.rangeSumBST(root.right, low, high)
        
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) # it means it is in the range of low and high, so we add it to the sum and call the function for the left and right nodes.
```
### Explanation
<div class = 'code-example' >
Read the comments in the code.
</div>

