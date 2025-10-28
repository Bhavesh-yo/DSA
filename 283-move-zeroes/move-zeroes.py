class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        if len(nums) == 0:  
            return  
        
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1
        
        if i == len(nums):
            return
        
        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                nums[j] = 0
                i += 1
            j += 1