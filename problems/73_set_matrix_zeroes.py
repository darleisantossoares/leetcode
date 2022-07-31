class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        def update_rows(row):
            for i, item in enumerate(matrix[row]):
                matrix[row][i] = 0


        def update_columns(col):
            for i, row in enumerate(matrix):
                matrix[i][col] = 0

        positions = list()

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    positions.append([i,j])


        for position in positions:

            r, c = position[0], position[1]

            update_rows(r)
            update_columns(c)
