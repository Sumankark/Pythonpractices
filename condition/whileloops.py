# i = 1
# while i<=5:
#     print("*" * i)
#     i+=1
# print("done")

# ---Guess secret number exercise.----

# secret_number = 8
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry you failed.")



# -------Car game exercise-----
command = ""
started = False
while True:
    repeat = command
    command = input(">").lower()

    if command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car start...Ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already Stopped.")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""start - to start the car
stop - to stop a car
quit - to exit""")
    elif command == "quit":
        break
    else:
        print("I don't understand it... ")




