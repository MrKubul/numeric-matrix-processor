import sys


class Matrix:
    def __init__(self):
        self.start()

    def handle_input(self, user_input):
        if user_input == '1':
            self.add_matrices()
            return
        elif user_input == '2':
            self.multiply_matrices_const()
            return
        elif user_input == '3':
            self.multiply_matrices()
            return
        elif user_input == '4':
            self.transpose_matrix()
            return
        elif user_input == '5':
            self.create_single_matrix()
            print('The result is:\n')
            print(self.calculate_determinant(self.matrix1))
            return
        elif user_input == '6':
            self.inverse_matrix()
        elif user_input == '0':
            sys.exit()

    def inverse_matrix(self):
        self.create_single_matrix()
        det = self.calculate_determinant(self.matrix1)
        if det == 0:
            print("This matrix doesn't have an inverse.")
            return
        else:
            print('The result is:\n')
            result_matrix = [row[:] for row in self.matrix1]
            for row in range(int(self.row_1)):
                for col in range(int(self.col_1)):
                    copy_matrix = [row[:] for row in self.matrix1]
                    copy_matrix.pop(row)
                    for j in range(int(self.row_1) - 1):
                        copy_matrix[j].pop(col)
                    x = (-1) ** (row + 1 + col + 1) * self.calculate_determinant(copy_matrix)
                    result_matrix[row][col] = x
            copy2_matrix = [row[:] for row in result_matrix]
            for row in range(len(result_matrix)):
                for i in range(len(result_matrix[0])):
                    result_matrix[i][row] = copy2_matrix[row][i]
            str_result = ""
            for rows_ in range(int(self.row_1)):
                for cols_ in range(int(self.col_1)):
                    part = (result_matrix[rows_][cols_] * (1 / det))
                    str_result += str(round(part, 4)) + " "
                print(str_result.strip())
                str_result = ""

    def calculate_determinant(self, matrix1):
        if len(matrix1) != len(matrix1[0]):
            print('ERROR, matrix needs to be square matrix')
            return
        elif len(matrix1) == 1:
            return (matrix1[0][0])
        elif len(matrix1) == 2:
            det = (matrix1[0][0] * matrix1[1][1]) - (matrix1[1][0] * matrix1[0][1])
            return det
        else:
            total = 0
            for j in range(len(matrix1[0])):
                copy_matrix = [row[:] for row in matrix1]
                copy_matrix.pop(0)
                for row in range(len(matrix1) - 1):
                    copy_matrix[row].pop(j)
                if ((j + 1) + 1) % 2 == 0:
                    total += matrix1[0][j] * self.calculate_determinant(copy_matrix)
                else:
                    total -= matrix1[0][j] * self.calculate_determinant(copy_matrix)
            return total

    def transpose_matrix(self):
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        choice = input('Your choice')
        if choice == '1':
            self.main_swap()
            return
        elif choice == '2':
            self.side_swap()
            return
        elif choice == '3':
            self.vertical()
            return
        elif choice == '4':
            self.horizontal()
            return

    def main_swap(self):
        self.create_single_matrix()
        copy_matrix = [row[:] for row in self.matrix1]
        for row in range(int(self.row_1)):
            for i in range(int(self.col_1)):
                self.matrix1[i][row] = copy_matrix[row][i]
        print('The result is:')
        str_result = ''
        for row in range(int(self.row_1)):
            for i in range(int(self.col_1)):
                str_result += str(self.matrix1[row][i]) + ' '
            print(str_result.strip())
            str_result = ""

    def side_swap(self):
        self.create_single_matrix()
        empty_matrix = [[] for _ in range(int(self.row_1))]
        for row in range(int(self.row_1)):
            for i in range(int(self.col_1)):
                empty_matrix[int(self.row_1) - row - 1].insert(0, self.matrix1[i][row])
        print('The result is:')
        str_result = ''
        for row in range(int(self.row_1)):
            for i in range(int(self.col_1)):
                str_result += str(empty_matrix[row][i]) + ' '
            print(str_result.strip())
            str_result = ""

    def horizontal(self):
        self.create_single_matrix()
        print('The result is:')
        self.matrix1.reverse()
        str_result = ''
        for row in range(int(self.row_1)):
            for i in range(int(self.col_1)):
                str_result += str(self.matrix1[row][i]) + ' '
            print(str_result.strip())
            str_result = ""

    def vertical(self):
        self.create_single_matrix()
        for row in range(int(self.row_1)):
            self.matrix1[row].reverse()
        print('The result is:')
        str_result = ''
        for row in range(int(self.row_1)):
            for i in range(int(self.col_1)):
                str_result += str(self.matrix1[row][i]) + ' '
            print(str_result.strip())
            str_result = ""


    def create_matrices(self):
        print('Enter size of first matrix:')
        self.row_1, self.col_1 = input().split()
        self.matrix1 = []
        self.read_matrix(self.matrix1, self.row_1)

        print('Enter size of second matrix:')
        self.row_2, self.col_2 = input().split()
        self.matrix2 = []
        self.read_matrix(self.matrix2, self.row_2)

    def print_menu(self):
        print('1. Add matrices')
        print('2. Multiply matrix by a constant')
        print('3. Multiply matrices')
        print('4. Transpose matrix')
        print('5. Calculate a determinant')
        print('6. Inverse matrix')
        print('0. Exit')

    def start(self):
        while True:
            self.print_menu()
            user_input = input()
            self.handle_input(user_input)

    def read_matrix(self, matrixY, rows):
        print('Enter matrix:')
        for row in range(int(rows)):
            actual_row = [int(n) if n.isdigit() else float(n) for n in input().split(' ')]
            matrixY.append(actual_row)

    def add_matrices(self):
        self.create_matrices()
        if self.row_1 == self.row_2 and self.col_1 == self.col_2:
            str_result = ""
            for rows_ in range(int(self.row_1)):
                for cols_ in range(int(self.col_1)):
                    str_result += str(self.matrix1[rows_][cols_] + self.matrix2[rows_][cols_]) + " "
                print(str_result.strip())
                str_result = ""
        else:
            print("ERROR")

    def create_single_matrix(self):
        print('Enter size of matrix:')
        self.row_1, self.col_1 = input().split()
        self.matrix1 = []
        self.read_matrix(self.matrix1, self.row_1)

    def multiply_matrices_const(self):
        self.create_single_matrix()
        print('Enter constant:')
        constant1 = input()
        if constant1.isdigit():
            constant1 = int(constant1)
        else:
            constant1 = float(constant1)
        str_result = ""
        for rows_ in range(int(self.row_1)):
            for cols_ in range(int(self.col_1)):
                str_result += str(self.matrix1[rows_][cols_] * constant1) + " "
            print(str_result.strip())
            str_result = ""

    def multiply_matrices(self):
        self.create_matrices()
        if self.col_1 == self.row_2:
            str_result = ""
            for rows_ in range(int(self.row_1)):
                for cols_ in range(int(self.col_2)):
                    sub_result = 0
                    for z in range(int(self.col_1)):
                        sub_result += self.matrix1[rows_][z] * self.matrix2[z][cols_]
                    str_result += str(sub_result) + " "
                print(str_result.strip())
                str_result = ""
        else:
            print("ERROR")


mtrx = Matrix()