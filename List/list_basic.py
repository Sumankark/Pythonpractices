# name = ["John", "Ram", "Sita", "Krishna"]
# print(name)
# print(name[0])
# print(name[1:3])

# ------Exercise-------
# numbers = [3, 2, 5, 1, 29, 84]
# max_number = numbers[0]
# for i in numbers:
#     if i > max_number:
#         max_number =i
# print("Max number is ", max_number)

# ------ 2D List ------
# matrix = [[2, 3, 4], [1, 2, 3], [3, 2, 1]]
# print(matrix[2][1])
# for row in matrix:
#     for item in row:
#         print(item)


# -----List Method------
numbers = [5, 2, 7, 7, 3, 4, 7, 2]
# numbers.append(13)
# numbers.insert(2, 23)
# numbers.remove(3)
# numbers.clear()
# numbers.pop()
# numbers.sort()
# numbers.reverse()
# number1 = numbers.copy()
# print(number1)
# numbers.sort()
# print(numbers.count(7))
# print(1 in numbers)
# print(numbers.index(7))
# print(numbers)

# ----- To remove repeat number ------
new_number = []
for i in numbers:
    if i not in new_number:
        new_number.append(i)
print(new_number)