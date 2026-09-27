class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = set()

            for num in board[i]:
                if num == '.':
                    continue
                
                if num in seen:
                    return False
                
                seen.add(num)
        
        for j in range(len(board)):
            seen = set()

            for i in range(len(board)):
                num = board[i][j]

                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)

        for row_start in [0, 3, 6]:
            for col_start in [0, 3, 6]:
                seen = set()

                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        num = board[i][j]

                        if num == '.':
                            continue
                        
                        if num in seen:
                            return False
                        seen.add(num)
        
        return True
                   

