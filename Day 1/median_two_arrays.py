import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joined = sorted(nums1 + nums2)
        
        median_left = len(joined) // 2
        median_right = median_left
        
        if len(joined) % 2 == 0:
            median_left = math.floor(len(joined) / 2) - 1
            median_right = math.ceil(len(joined) / 2) 
            
            print(median_left, median_right)
            
        return (joined[median_left] + joined[median_right]) / 2

# Proud of this, first try!