class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        first_min_prev = 0
        first_min_prev_j = -1
        second_min_prev = 0
        second_min_prev_j = -1

        for i in range(len(grid)-1,-1,-1):
            first_min_cur = None
            second_min_cur = None
            first_min_cur_j = -1
            second_min_cur_j = -1

            for j in range(len(grid[0])):

                if j == first_min_prev_j:

                    item = grid[i][j] + second_min_prev

                    if first_min_cur is None:

                        first_min_cur = item
                        first_min_cur_j = j

                    elif first_min_cur > item:

                        second_min_cur = first_min_cur
                        second_min_cur_j = first_min_cur_j
                        first_min_cur = item
                        first_min_cur_j = j

                    elif second_min_cur is None or second_min_cur > item:
                        second_min_cur = item
                        second_min_cur_j = j

                else:

                    item = grid[i][j] + first_min_prev

                    if first_min_cur is None:

                        first_min_cur = item
                        first_min_cur_j = j

                    elif first_min_cur > item:

                        second_min_cur = first_min_cur
                        second_min_cur_j = first_min_cur_j
                        first_min_cur = item
                        first_min_cur_j = j

                    elif second_min_cur is None or second_min_cur > item:

                        second_min_cur = item
                        second_min_cur_j = j
                
            first_min_prev = first_min_cur
            second_min_prev = second_min_cur
            first_min_prev_j = first_min_cur_j
            second_min_prev_j = second_min_cur_j
        
        return first_min_prev