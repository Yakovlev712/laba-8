
size = int(input("Введите размер квадрата: "))
square = []

for row_number in range(size):
    row = list(map(int, input().split()))
    square.append(row)

first_row_sum = sum(square[0])
is_magic = True

for row_number in range(size):
    row_sum = sum(square[row_number])

    if row_sum != first_row_sum:
        is_magic = False

for column_number in range(size):
    column_sum = 0

    for row_number in range(size):
        column_sum += square[row_number][column_number]

    if column_sum != first_row_sum:
        is_magic = False

all_numbers = []

for row in square:
    for number in row:
        all_numbers.append(number)

if sorted(all_numbers) != list(range(1, size * size + 1)):
    is_magic = False

if is_magic:
    print("Магический квадрат")
else:
    print("Не магический квадрат")
