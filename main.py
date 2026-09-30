file_name = "My Shopping List Manager"

shopping_file = open(file_name, "w")
shopping_file.write("Shopping List\n")
shopping_file.write("1. Milk\n")
shopping_file.write("2. Bread\n")
shopping_file.close()

print("\n===== Shopping List ===== ")
shopping_file = open(file_name, "r")
content = shopping_file.read()
print(content)
shopping_file.close()

shopping_file = open(file_name, "a")
shopping_file.write('5. Rice\n')
shopping_file.write("6. Butter\n")
shopping_file.close()
print("2 items added successfully! ")

shopping_file = open(file_name)
updated_content = shopping_file.read()
print("\n===== Updated Shopping List =====\n", updated_content)

shopping_file.close()

shopping_file = open(file_name)
print("\n ===== Reading Shopping List Line by Line =====")

line_number = 1

for line in shopping_file:
    print("Line", line_number, ":", line.strip())
    line_number = line_number + 1

shopping_file.close()