class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {str(i): set() for i in range(1, 10)}
        cols = {str(i): set() for i in range(1, 10)}
        sub_boxes = {str(i): set() for i in range(1, 10)}
        num_cols = len(board[0])
        num_rows = len(board)
        for i in range(num_rows):
            for j in range(num_cols):
                element = board[i][j]
                sub_box = (i // 3 , j //3)
                if element == '.':
                    continue

                if i in rows[element]:
                    return False
                
                rows[element].add(i)

                if j in cols[element]:
                    return False

                cols[element].add(j)
                
                if sub_box in sub_boxes[element]:
                    return False
                
                sub_boxes[element].add(sub_box)


        return True
                


