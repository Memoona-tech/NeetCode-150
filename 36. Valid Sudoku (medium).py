# SOLUTION 1
# ------------------ O(1) TC ----------- O(1) SC --------

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        for (int i = 0; i < 9; i++) {

            for (int j = 0; j < 9; j++) {

                if (board[i][j] == '.')
                    continue;

                char current = board[i][j];

                // Check Row
                for (int col = 0; col < 9; col++) {

                    if (col != j && board[i][col] == current)
                        return false;
                }

                // Check Column
                for (int row = 0; row < 9; row++) {

                    if (row != i && board[row][j] == current)
                        return false;
                }

                // Check 3x3 Box
                int startRow = (i / 3) * 3;
                int startCol = (j / 3) * 3;

                for (int r = startRow; r < startRow + 3; r++) {

                    for (int c = startCol; c < startCol + 3; c++) {

                        if ((r != i || c != j) &&
                            board[r][c] == current)
                            return false;
                    }
                }
            }
        }

        return true;
    }
};


# SOLUTION 2 (Optimized)
# ------------------ O(1) TC ----------- O(1) SC --------

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)] ):

                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[( r//3 , c//3 )].add(board[r][c])
        return True
