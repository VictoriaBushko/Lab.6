def bubble_sort(row):
    n = 0
    for _ in row:
        n += 1

    for i in range(n):
        for j in range(0, n - i - 1):
            if row[j] > row[j + 1]:
                row[j], row[j + 1] = row[j + 1], row[j]
    return row


def find_min_in_columns(matrix):
    rows = 0
    for _ in matrix:
        rows += 1

    cols = 0
    for _ in matrix[0]:
        cols += 1

    min_elements = []
    for col in range(cols):
        min_val = matrix[0][col]
        for row in range(1, rows):
            if matrix[row][col] < min_val:
                min_val = matrix[row][col]
        min_elements.append(min_val)
    return min_elements


def calculate_product(min_elements):
    product = 1
    for elem in min_elements:
        product *= elem
    return product


matrix = [
    [34, -8, 27, 7, 12],
    [-5, 23, 45, 67, -2],
    [13, -12, 34, -3, 25],
    [17, 56, -6, 17, 21],
    [0, 15, 4, 9, -14]
]

sorted_matrix = []
for row in matrix:
    row_copy = []
    for element in row:
        row_copy.append(element)
    sorted_matrix.append(bubble_sort(row_copy))

min_elements = find_min_in_columns(sorted_matrix)
product_of_min_elements = calculate_product(min_elements)

result = "Sorted matrix:\n"
for row in sorted_matrix:
    result += f"{row}\n"

result += f"\nMinimum elements in each column: {min_elements}\n"
result += f"\nProduct of minimum elements: {product_of_min_elements}\n"

print(result)