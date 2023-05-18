class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, curr_sum, chosen):
            if curr_sum == target:
                result.append(list(chosen))
                return
            
            if curr_sum > target:
                return
            
            for i in range(start, len(candidates)):
                chosen.append(candidates[i])
                backtrack(i, curr_sum + candidates[i], chosen)
                chosen.pop()
        
        result = []
        candidates.sort()
        backtrack(0, 0, [])
        return result
