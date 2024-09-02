class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_count = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[val_count] = nums[i]
                val_count+=1
            else:
                nums[i] = -1
        return val_count