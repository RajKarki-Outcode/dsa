# age = int(input("Enter your age: "))

# if age < 18:
#     print(f"Not eligible \nYou will be eligible  {18 - age} years")
# elif age >= 18 and age < 60:
#     print("Eligible to vote")
# else:
#     print("Senior Citizen")

rows = int(input("Enter the number of rows: "))
for i in range(1, rows +1):
    print('*' * i)
    