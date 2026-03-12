####System for record students and grades

##Story 1 - students record
print("-"*20, "Welcome to the system of ", "-"*20)

students = []

while True:
    print("\n ", "-"*65,"")
    print("\n1. Add student and subjects" \
    "\n2. Show the student")
    print("\n ", "-"*65,"")
    option = int(input("Choose a option: "))
    try:
        if option == 1:
            number_students = int(input("Enter the number of students to record: "))

            for n in range(number_students):
                print("\n ", "-"*65,"")
                full_name = input("\nEnter the fullname: ")
                subjects = []
                grades = []
                number_subjects = int(input("\nEnter the number of subjects: "))
            
                for m in range(number_subjects):
                    subject = input("\nAdd the subject: ")
                    grade = float(input("Enter de grade of subject: "))
                    print("\n ", "-"*65,"")

                    subjects.append(subject)
                    grades.append(grade)
            students.append({
                "fullname": full_name,
                "subjects": subjects,
                "grades": grades
                        })
        elif option == 2:
            for i, list in enumerate(students):
                print(f"\n{i+1}. Student: {list['fullname']}")
                for sub in range(len(list["subjects"])):
                    print(f"Subject: {list['subjects'][sub]} - Grade: {list['grades'][sub]}")
    except ValueError:
        print ("\nEnter a number int")              

##Story 2 - record of subjects and grades

    # elif option == 2:
    #     number_subjects = int(input("Enter the number of subjects: "))

    #     for c in students:
    #         for m in range(number_subjects):
    #             subject = input("Add the subject: ")

    #         subjects.append({
    #             "subject": subject,
    #             "grade": {}
    #         })
    #     for i, sub in enumerate(subjects):
    #         print(f"{i+1}. student {sub['subject']} grade {sub['grade']}")


    # elif option == 3:
    #     for id, n in enumerate(students):
    #         print(f"{id+1}. student {n['fullname']}: ")
    #         for m in subjects:
    #             print(f"{m["subjest"]}")



        # for e in (students):
        #     for m in 