number = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]

for row in number:
    print(row)


for row in number:
    for col in row:
        print(col, end=" ")
    print()

# This code defines a 2D array (list of lists) called `number` and then iterates through it to print its contents.
# The first loop prints each row as a list, while the second loop prints each element in the 2D array on the same line, separated by spaces.
# The second loop uses `end=" "` to ensure that elements in the same row are printed on the same line, and `print()` at the end of the inner loop moves to the next line after printing all elements of a row.
# The output will show the structure of the 2D array in two different formats.
# The first output will be:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# [10, 11, 12]
# The second output will be:
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# This code demonstrates how to work with a 2D array in Python, iterating through its rows and columns to print the values.