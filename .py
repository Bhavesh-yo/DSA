from typing import List

def search(nums: List[int], target: int) -> int:
    """
    LeetCode 704: Binary Search
    Given an array of integers nums which is sorted in ascending order, 
    and an integer target, write a function to search target in nums. 
    If target exists, then return its index. Otherwise, return -1.
    
    You must write an algorithm with O(log n) runtime complexity.
    
    Args:
    nums: Sorted list of integers in ascending order
    target: Integer to search for
    
    Returns:
    Index of target if found, otherwise -1
    """
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Integer division to ensure mid is an int
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1