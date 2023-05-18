class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            nonlocal permutations
            if start == len(nums):
                permutations.append(nums[:])
                return
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        permutations = []
        backtrack(0)
        return permutations
