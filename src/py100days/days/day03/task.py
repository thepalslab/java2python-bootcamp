# src/py100days/days/day03/task.py
def run() -> None:
    print("Day 3: Beginner - Control Flow and Logical Operators")

    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    if height >= 120:
        print("You can ride the rollercoaster!")
        age = int(input("What is your age? "))

        if age < 12:
            print("Please pay $15")
            ticket = 15
        elif age <= 18:
            print("Please pay $20")
            ticket = 20
        elif 45 <= age <= 55:
            print("Everything is going to be OK. We are giving you free ride")
            ticket = 0
        else:
            print("Please pay $10")
            ticket = 10

        want_photo = input("Do you want your photo taken? Type Y for Yes or N for No: ")
        if want_photo == "Y":
            ticket += 3

        print(f"The total bill is $${ticket}")
    else:
        print("Sorry you have to grow taller to ride the rollercoaster")

    print(10 % 3)
    print(10 // 3)
    print(10 / 3)

    number_to_check = int(input("What is the number you want to check? "))

    if number_to_check % 2 == 0:
        print("The number is even!")
    else:
        print("The number is odd!")

    weight = 850
    height = 1.85

    bmi = weight / (height ** 2)

    # 🚨 Do not modify the values above
    # Write your code below 👇

    if bmi >= 25:
        print("overweight")
    elif 18.5 <= bmi < 25:
        print("normal weight")
    else:
        print("underweight")

    print("Welcome to python Pizza Deliveries")
    size = input("What size pizza do you want? S, M, or L: ")

    total_bill = 0
    if size == "S":
        print("Please pay $10")
        total_bill += 10
    elif size == "M":
        print("Please pay $20")
        total_bill += 20
    elif size == "L":
        print("Please pay $30")
        total_bill += 30
    else:
        print("Pizza size is not supported")

    pepperoni = input("Do you want pepperoni on your pizza? (Y/N): ?: ")
    if pepperoni == "Y":
        print("It will cost you extra $10")
        total_bill += 10

    extra_cheese = input("Do you want extra cheese? (Y/N): ")
    if extra_cheese == "Y":
        print("It will cost you extra $20")
        total_bill += 20

    print("Your total bill is $" + str(total_bill))

def project() -> None:
    print("Welcome to Treasure Island. Your mission is to find the treasure.")
    command = input("left or right?")
    if command != "left":
        print("Fall into a hole. Game Over.")
    else:
        command = input("swim or wait?")
        if command != "wait":
            print("Attacked by trout. Game Over.")
        else:
            command = input("Which door: Red/Blue/Yellow/AnythingElse?")
            if command == "Red":
                print("Burned by fire. Game Over.")
            elif command == "Blue":
                print("Eaten by beasts. Game Over.")
            elif command == "Yellow":
                print("You Win!")
            else:
                print("Game Over.")


if __name__ == "__main__":
    project()
