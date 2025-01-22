# course1 = "let's learn python."
# course2 = 'python "easy to learn".'
# course3 = '''here we can use single quote(') and double quote(") inside it and also
# write in
# multiple lines.'''
#
# print(course1)
# print(course2)
# print(course3)

# # index
# print(course3[-1])
# print(course3[:4])
# print(course2[0:6])

# name = "Suman"
# print(name[1:-1])

# String formating
full_name = "i am Suman Karki"
first_name = "Suman"
last_name = "karki"
gender = "    male      "
print(gender)
print(gender.strip())
arr = full_name.split(" ")
print(arr)

print("_".join(arr))
print(f"{first_name} [{last_name}] is a coder")
print(len(first_name))
print(first_name.upper())
print(first_name.lower())
print(last_name.find("k"))
print(full_name.replace("I am", "My name is"))
print("Karki" in full_name)
print(full_name.title())
print(full_name.startswith("I"))
print(full_name.endswith("Karki"))