class Matrix:
    def __init__(self, data, sort_enabled=True):
        self.data = data
        self.sort_enabled = sort_enabled

    def calculate_length(self, sequence):
        count = 0
        for _ in sequence:
            count += 1
        return count

    def bubble_sort_decorator(func):
        def wrapper(self, *args, **kwargs):
            if self.sort_enabled:
                for i in range(self.calculate_length(self.data)):
                    for j in range(self.calculate_length(self.data[i]) - 1):
                        for k in range(self.calculate_length(self.data[i]) - j - 1):
                            if self.data[i][k] > self.data[i][k + 1]:
                                self.data[i][k], self.data[i][k + 1] = self.data[i][k + 1], self.data[i][k]
            return func(self, *args, **kwargs)
        return wrapper

    @bubble_sort_decorator
    def sort_rows(self):
        pass

    def find_min_in_columns(self):
        rows = self.calculate_length(self.data)
        cols = self.calculate_length(self.data[0])

        min_elements = []
        for col in range(cols):
            min_val = self.data[0][col]
            for row in range(1, rows):
                if self.data[row][col] < min_val:
                    min_val = self.data[row][col]
            min_elements.append(min_val)
        return min_elements

    def calculate_product(self, min_elements):
        product = 1
        for elem in min_elements:
            product *= elem
        return product

    def to_string(self):
        min_elements = self.find_min_in_columns()
        product = self.calculate_product(min_elements)

        result = "Відсортована матриця:\n"
        for row in self.data:
            result += f"{row}\n"
        result += f"\nМінімальні елементи у кожному стовпці: {min_elements}"
        result += f"\n\nДобуток мінімальних елементів: {product}"
        return result

    def __str__(self):
        result = "Матриця:\n"
        for row in self.data:
            result += " ".join(map(str, row)) + "\n"
        return result

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            print()
            return None
        if self.calculate_length(self.data) != self.calculate_length(other.data) or \
           self.calculate_length(self.data[0]) != self.calculate_length(other.data[0]):
            print()
            return None

        result = []
        for i in range(self.calculate_length(self.data)):
            new_row = []
            for j in range(self.calculate_length(self.data[i])):
                new_row.append(self.data[i][j] * other.data[i][j]) 
            result.append(new_row)
        return Matrix(result, sort_enabled=self.sort_enabled)


matrix_data1 = [
    [34, -8, 27],
    [-5, 23, 45],
    [13, -12, 34],
]

matrix_data2 = [
    [1, 2, 1],
    [1, 2, 1],
    [2, 1, 1],
]

matrix1 = Matrix(matrix_data1, sort_enabled=True)
matrix2 = Matrix(matrix_data2, sort_enabled=True)

result_matrices = matrix1 * matrix2
print(result_matrices)

matrix = Matrix(matrix_data1, sort_enabled=True)
matrix.sort_rows()
print(matrix.to_string())

unsorted_matrix = Matrix(matrix_data1, sort_enabled=False)
unsorted_matrix.sort_rows()
print(unsorted_matrix.to_string())
