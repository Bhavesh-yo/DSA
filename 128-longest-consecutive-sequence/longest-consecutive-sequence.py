class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      from typing import List
    from typing import List

   
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                count = 1
                while num + count in num_set:
                    count += 1
                longest = max(longest, count)
        
        return longest