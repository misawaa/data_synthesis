class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure that nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        # Initialize variables for binary search
        left, right = 0, m
        # Loop until a valid partition is found
        while left <= right:
            # Calculate the partition indices for both arrays
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
            # Handle edge cases where one partition is empty
            max_left1 = nums1[partition1-1] if partition1 > 0 else float('-inf')
            min_right1 = nums1[partition1] if partition1 < m else float('inf')
            max_left2 = nums2[partition2-1] if partition2 > 0 else float('-inf')
            min_right2 = nums2[partition2] if partition2 < n else float('inf')
            # Check if the partitions are valid
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Calculate the median based on the length of the merged array
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                # The partition in nums1 is too big, so move the right boundary to the left
                right = partition1 - 1
            else:
                # The partition in nums1 is too small, so move the left boundary to the right
                left = partition1 + 1
