"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""
import copy
class Solution:
    @staticmethod
    def rotate(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #matrix1=[[None] * len(matrix)] * len(matrix)
        matrix1=copy.deepcopy(matrix)
        print(matrix1)
        #print(len(matrix))
        length=len(matrix)
        col=0
        newRow=0
        while(col<length):
            row = length - 1
            newCol=0
            while(row>-1):
                matrix1[newRow][newCol]=matrix[row][col]
                row=row-1
                newCol=newCol+1
            col=col+1
            newRow=newRow+1
        for i in range(length):
            j=0
            for j in range(length):
                matrix[i][j]=matrix1[i][j]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
Solution.rotate(matrix)