"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            nums={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0, ".":0}
            for j in range(9):
                if(nums[board[i][j]]==1):
                    return False
                elif(board[i][j]=="."):
                    continue
                else:
                    nums[board[i][j]]=1
        
        for i in range(9):
            nums={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0, ".":0}
            for j in range(9):
                if(nums[board[j][i]]==1):
                    return False
                elif(board[j][i]=="."):
                    continue
                else:
                    nums[board[j][i]]=1
        
        nums={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0, ".":0}
        for i in range(3):
            for j in range(3):
                if(nums[board[i][j]]==1):
                    return False
                elif(board[i][j]=="."):
                    continue
                else:
                    nums[board[i][j]]=1
            
        nums={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0, ".":0}
        for i in range(3,6,1):
            for j in range(3):
                if(nums[board[i][j]]==1):
                    return False
                elif(board[i][j]=="."):
                    continue
                else:
                    nums[board[i][j]]=1
                    
        nums={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0, ".":0}
        for i in range(6,9,1):
            for j in range(3):
                if(nums[board[i][j]]==1):
                    return False
                elif(board[i][j]=="."):
                    continue
                else:
                    nums[board[i][j]]=1
                    
        nums={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0, ".":0}
        for i in range(3):
            for j in range(3,6,1):
                if(nums[board[i][j]]==1):
                    return False
                elif(board[i][j]=="."):
                    continue
                else:
                    nums[board[i][j]]=1
                    
        nums={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0, ".":0}
        for i in range(3,6,1):
            for j in range(3,6,1):
                if(nums[board[i][j]]==1):
                    return False
                elif(board[i][j]=="."):
                    continue
                else:
                    nums[board[i][j]]=1
                    
        nums={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0, ".":0}
        for i in range(6,9,1):
            for j in range(3,6,1):
                if(nums[board[i][j]]==1):
                    return False
                elif(board[i][j]=="."):
                    continue
                else:
                    nums[board[i][j]]=1
                    
        nums={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0, ".":0}
        for i in range(3):
            for j in range(6,9,1):
                if(nums[board[i][j]]==1):
                    return False
                elif(board[i][j]=="."):
                    continue
                else:
                    nums[board[i][j]]=1
                    
        nums={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0, ".":0}
        for i in range(3,6,1):
            for j in range(6,9,1):
                if(nums[board[i][j]]==1):
                    return False
                elif(board[i][j]=="."):
                    continue
                else:
                    nums[board[i][j]]=1
                    
        nums={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0, ".":0}
        for i in range(6,9,1):
            for j in range(6,9,1):
                if(nums[board[i][j]]==1):
                    return False
                elif(board[i][j]=="."):
                    continue
                else:
                    nums[board[i][j]]=1
        
        return True