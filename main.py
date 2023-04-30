import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        """Combining Two Lists"""
        if nums1 == False:
            nums1 = []
        if nums2 == False:
            nums2 = []
        data = nums1 + nums2
        new_data = sorted(np.array(data))

        """Searching Median"""
        length = len(new_data)
        if length % 2 == 1:
            print(new_data[int((length + 1)/2)-1])
        elif length % 2 == 0:
            half = int(length/2)
            even = (new_data[half-1]+new_data[half])/2
            print(even)
        
conduct = Solution()
conduct.findMedianSortedArrays([1,2,3], [4,5,6])