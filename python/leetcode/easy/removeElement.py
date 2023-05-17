class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize two pointers
        i = 0
        n = len(nums)

        # Iterate through the array
        while i < n:
            # If the current element equals val, replace it with the last element
            # and decrement n to exclude the last element from consideration
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                # If the current element does not equal val, increment i
                i += 1

        # Return the number of elements that are not equal to val
        return n
