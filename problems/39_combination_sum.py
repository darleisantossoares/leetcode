class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        answer = list()

        def backtracking(position, temp_list):

            if sum(temp_list) == target:
                answer.append(temp_list.copy())
                return

            if sum(temp_list) > target:
                return

            for i in range(position, len(candidates)):
                temp_list.append(candidates[i])
                backtracking(i, temp_list)
                temp_list.pop()


        backtracking(0, [])
        return answer
