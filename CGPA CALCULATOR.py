def get_grade(mark):
    # If student is absent
    if isinstance(mark, str) and mark.lower() == "absent":
        return 0, "N", 0

    # Convert marks to integer
    try:
        mark = int(mark)
    except ValueError:
        return None, "Invalid", 0

    # Grade and Grade Point
    if 90 <= mark <= 100:
        return mark, "S", 10
    elif 80 <= mark < 90:
        return mark, "A", 9
    elif 70 <= mark < 80:
        return mark, "B", 8
    elif 60 <= mark < 70:
        return mark, "C", 7
    elif 50 <= mark < 60:
        return mark, "D", 6
    elif 40 <= mark < 50:
        return mark, "E", 5
    elif 0 <= mark < 40:
        return mark, "F", 0
    else:
        return None, "Invalid", 0


def student_info(name, reg_number, mark1, mark2, mark3, mark4):

    print("\n========== STUDENT INFORMATION ==========")
    print("Student Name:", name)
    print("Registration Number:", reg_number)

    # Subject details
    subjects = [
        ("MAT1003", mark1, 4),
        ("CSE1021", mark2, 4),
        ("ENG1004", mark3, 2),
        ("CHY1006", mark4, 2)
    ]

    total_marks = 0
    total_credits = 0
    total_credit_points = 0

    print("\n=============== RESULT ===============")

    for subject, mark, credit in subjects:

        marks, grade, grade_point = get_grade(mark)

        print("\nSubject:", subject)

        if grade == "N":
            print("Marks: 0")
            print("Grade: N (Absent)")
            print("Grade Point: 0")

        elif grade == "Invalid":
            print("Invalid marks entered!")

        else:
            print("Marks:", marks)
            print("Grade:", grade)
            print("Grade Point:", grade_point)

        # Calculate total marks
        if marks is not None:
            total_marks += marks

        # Calculate total credits
        total_credits += credit

        # Calculate total credit points
        total_credit_points += credit * grade_point

    # Average marks
    average = total_marks / len(subjects)

    # SGPA
    sgpa = total_credit_points / total_credits

    print("\n========================================")
    print("Total Marks:", total_marks)
    print("Average Marks:", round(average, 2))
    print("Total Credits:", total_credits)
    print("Total Credit Points:", total_credit_points)
    print("SGPA:", round(sgpa, 2))
    print("=========================================")


# Taking input from user
Name = input("Enter your name: ")
reg_number = input("Enter your Registration number: ")

Mark1 = input("Enter MAT1003 marks: ")
Mark2 = input("Enter CSE1021 marks: ")
Mark3 = input("Enter ENG1004 marks: ")
Mark4 = input("Enter CHY1006 marks: ")

# Calling function
student_info(Name, reg_number, Mark1, Mark2, Mark3, Mark4)