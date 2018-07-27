# First solution, takes awhile because it actually gets all the diagonals
class Solution(object): 
    def isToeplitzMatrix(self, matrix):
        """
        :type self.matrix: List[List[int]]
        :rtype: bool
        """
        self.matrix = matrix
        diagonals = []
        if len(self.matrix) == 0:
            return False
        if len(self.matrix[0]) == 0:
            return False
        if len(self.matrix) == 1:
            return True
        if len(self.matrix[0]) == 1:
            return True
        num_rows = len(self.matrix)
        num_cols = len(self.matrix[1])

        # Get lower half (num_rows - 1 diagonals)
        for i in range(1, num_rows): # number of diagonals
            diagonal = []
            x = 0
            y = num_rows - i
            while x < num_cols and y < num_rows:
                diagonal.append(self.matrix[y][x])
                x += 1
                y += 1
            diagonals.append(diagonal)

        # Get upper half
        for j in range(0, num_cols): # number of diagonals
            diagonal = []
            x = j
            y = 0
            while x < num_cols and y < num_rows:
                diagonal.append(self.matrix[y][x])
                x += 1
                y += 1
            diagonals.append(diagonal)

        for diag in diagonals:
            check = diag[0]
            for i in diag:
                if i != check:
                    return False
        return True