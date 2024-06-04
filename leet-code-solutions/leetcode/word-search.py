class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #finding the first letter of the word to be searched for
        pos = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    pos.append((i,j))

        #do the searching algorithm using backtrack
        def search(h,v,k):
            if k == len(word):
                return True
            if h >= len(board) or v>=len(board[0]) or v<0 or h<0:
                return False
            if board[h][v] != word[k]:
                return False
            
            #marked
            board[h][v] = '#'
            
            #try every possible directions
            if search(h,v+1,k+1) or search(h,v-1,k+1) or search(h+1,v,k+1) or search(h-1,v,k+1):
                return True

            #unmarked
            board[h][v] = word[k]

        #try the search using the positions of tehe first letter
        for position in pos:
            if search(position[0],position[1],0):
                return True
        
        return False