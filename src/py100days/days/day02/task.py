def main():
    print("Hello from Day 02!")


print("Hello"[0])
print("Hello"[-1])
print("123" + "456")
print(123 + 456)
print(123.456)
print(True)
print(False)
print(734_529.678)
print(734529.678)

print(type(734529.678))
print(type(False))
print(type(123 + 456))

print(int("123") + int("456"))

int()
float()
bool()
str()

# name = input("What is your name? ")
# print("No of letters in your name is " + str(len(name)))

print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(2 ** 6)  # 2 to the power of 6

# BODMAS
print(3 * (3 + 3) / 3 - 3 ** 8)

bmi = 84 / 1.65 ** 2
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))

print(round(1.5))
print(round(1.6))

score = 10
height = 1.8
is_winning = True

print(f"Your score is: {score}, Your height is: {height}, Your winning is: {is_winning}")

print("Welcome to the tip calculator!")
total_bill = input("What is the total bill?")
tip = input("How much tip would you like to give 10, 12 or 15?")
total_people = input("How many people to split the bill?")

# per_person_amt = (float(total_bill) + (float(total_bill) * (int(tip) / 100))) / int(total_people)
per_person_amt = (float(total_bill) * (1 + int(tip) / 100)) / int(total_people)
print(f"Each person should pay: ${round(per_person_amt, 2)}")
