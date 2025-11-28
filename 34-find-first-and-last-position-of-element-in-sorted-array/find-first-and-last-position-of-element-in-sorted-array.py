class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
     from typing import List

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_leftmost():
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def find_rightmost():
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left - 1
        
        left = find_leftmost()
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        
        right = find_rightmost()
        return [left, right]