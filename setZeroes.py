# Runtime 0 ms | Beats 100%
# Memory 18.51 MB | Beats 37.48%
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()

        # Loop through each row and its elements
        for row_index in range(len(matrix)):
            for column_index in range(len(matrix[row_index])):

                # if its a zero, mark this column and row
                if matrix[row_index][column_index] == 0:
                    rows.add(row_index)
                    columns.add(column_index)

                    # Zero out predecessors
                    # Previous elements of the row
                    row_element_pointer = column_index
                    while row_element_pointer > 0:
                        row_element_pointer -= 1
                        matrix[row_index][row_element_pointer] = 0
                    # Previous elements of the column
                    column_element_pointer = row_index
                    while column_element_pointer > 0:
                        column_element_pointer -= 1
                        matrix[column_element_pointer][column_index] = 0
                
                # zero if this is a part of a zero'd column or row
                if (row_index in rows) or (column_index in columns):
                    matrix[row_index][column_index] = 0
        