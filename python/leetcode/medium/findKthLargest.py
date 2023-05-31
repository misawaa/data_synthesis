class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[0]
        left = []
        right = []
        equal = []
        
        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                equal.append(num)
        
        if k <= len(left):
            return self.findKthLargest(left, k)
        elif k > len(left) + len(equal):
            return self.findKthLargest(right, k - len(left) - len(equal))
        else:
            return equal[0]
