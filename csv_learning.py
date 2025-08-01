import csv

students = [
    {"Name": "Haz", "Math": 90, "Science": 85, "English": 88},
    {"Name": "Ben", "Math": 70, "Science": 75, "English": 80},
    {"Name": "Sara", "Math": 95, "Science": 92, "English": 89},
]

with open("marksheet.csv", 'w',newline='') as file:
    fieldnames = ["Name", "Math", "Science", "English"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print("Marksheet CSV created successfully.")

with open("marksheet.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']}, Math: {row['Math']}, Science: {row['Science']}, English: {row['English']}")