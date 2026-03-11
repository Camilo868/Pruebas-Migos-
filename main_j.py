###System for record students and notes

##Story 1 - students record
print("-"*20, "Welcome to the system of ", "-"*20)

students = []

while True:
    print("\n1. Add student" \
    "\n2. Add subject and grede" \
    "\n3. Show the student")
    print("\n ", "-"*65,"")
    option = int(input("Choose a option: "))
    
    if option == 1:
        number_students = int(input("Enter the number of students to record: "))

        for n in range(number_students):
            full_name = input("Enter the fullname: ")
            subject = None
            for c in students:
                subjects = []


                number_subjects = int(input("Enter the number of subjects: "))

                for m in range(number_subjects):
                    subject = input("Add the subject: ")
                    grade = float(input("Enter de grade of subject: "))

        students.append({
            "fullname": full_name,
            "subjects": subject,
                    })

        for i, list in enumerate(students):
            print(f"{i+1}. student {list['fullname']}")
            print (f"Subject: {list['subjects']}- grades: {list['grades']}")

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









