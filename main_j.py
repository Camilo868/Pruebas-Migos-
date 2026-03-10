###System for record students and notes

##Story 1 - students record
print("-"*20, "Welcome to the system of ", "-"*20)

students = []

number_students = int(input("Enter the number of students to record: "))

for n in range(number_students):
    name = input("Enter the name: ")
    last_name = input("Enter the last name: ")

students.append({
    "name": name,
    "last_name": last_name
})

for i, list in enumerate(students):
    print(f"{i+1}. student: {list['name']} {list['last_name']}")

##Story 2