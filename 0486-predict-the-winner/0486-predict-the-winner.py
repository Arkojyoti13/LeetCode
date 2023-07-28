class Solution:
    def PredictTheWinner(self, arr: list[int]) -> bool:
        
        @lru_cache(20)
        def reduce_tree(arr_tuple, player_1_bool):
            arr = list(arr_tuple)
            if len(arr) == 1:
                return arr[0] if player_1_bool else -arr[0]

            if player_1_bool:
                x = arr[0]+reduce_tree(tuple(arr[1::]), False)
                y = arr[-1]+reduce_tree(tuple(arr[0:-1]), False)
                return max(x, y)
            else:
                x = -arr[0]+reduce_tree(tuple(arr[1::]), True)
                y = -arr[-1]+reduce_tree(tuple(arr[0:-1]), True)
                return min(x, y)


        return(reduce_tree(tuple(arr), True)>=0)