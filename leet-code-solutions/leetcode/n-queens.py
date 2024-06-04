class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        cols = set()
        n_idx = set()
        p_idx = set()
        listo = []
        def boardo(row):
            if row >= n:
                board.append(listo.copy())
                return True
            letter = ["."]*n
            for col in range(n):
                if col in cols or row-col in n_idx or row+col in p_idx:
                    continue
                if col not in cols and row-col not in n_idx and row+col not in p_idx:
                    letter[col] = "Q"
                    cols.add(col)
                    n_idx.add(row-col)
                    p_idx.add(row+col)
                    listo.append("".join(letter))
                    boardo(row+1)
                    listo.pop()
                    cols.remove(col)
                    n_idx.remove(row-col)
                    p_idx.remove(row+col)
                    letter[col] = "."
        boardo(0)
        return board

                
