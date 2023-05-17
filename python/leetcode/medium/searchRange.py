class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def binary_search_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right
        
        # find any occurrence of the target using binary search
        index = bisect.bisect_left(nums, target)
        if index == len(nums) or nums[index] != target:
            return [-1, -1]
        
        # find the first and last occurrence using binary search
        left = binary_search_left(nums[:index], target)
        right = binary_search_right(nums[index:], target) + index
        return [left, right]
