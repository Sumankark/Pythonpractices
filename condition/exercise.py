weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit == "l" or unit == "L":
    weight_kg = weight * 0.45
    print(f"You are {weight_kg} kilos")
elif unit == "k" or unit =="K":
    weight_lb = weight / 0.45
    print(f"You are {weight_lb} pounds")
else:
    print("The unit is not exist.")

