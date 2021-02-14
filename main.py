import random

MIN_NUMBER = 1
MAX_NUMBER = 10
NUMBERS_OF_QUESTION= 4

def ask_question():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.randint(0, 1)
    operation_str = "+"
    if operation == 1:
        operation_str = "*"
    response_str = input(f"Calculate {a} {operation_str} {b} = ")
    response_int = int(response_str)
    calculus = a+b
    if operation == 1:
        calculus = a*b
    if response_int == calculus:
        return True

    return  False

nb_pts = 0
for i in range(0, NUMBERS_OF_QUESTION):
    print(f"Question n {i+1} on {NUMBERS_OF_QUESTION}: ")
    if ask_question():
        print("Correct")
        nb_pts += 1
    else:
        print("Nope")
    print()

print(f"You've got {nb_pts} / {NUMBERS_OF_QUESTION} pts")

average = int(NUMBERS_OF_QUESTION/2)

if nb_pts == NUMBERS_OF_QUESTION:
    print("EXCellent")
elif nb_pts == 0:
    print("go back to elementary school bro")

elif nb_pts > average:
    print("Not too bad")
else:
    print("Do it better next time")