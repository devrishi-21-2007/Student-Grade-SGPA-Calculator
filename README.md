# Student Grade & SGPA Calculator


## Project Overview

The Student Grade & SGPA Calculator is a simple Python-based program that takes a student's name, registration number, and marks in four subjects as input.

The program calculates the grade, grade point, total marks, average marks, total credits, total credit points, and SGPA of the student.

It also handles cases where a student is absent or enters invalid marks.

This project is designed as a beginner-level Python project to demonstrate the use of functions, conditional statements, loops, lists, input/output, and basic calculations.

## Features

1. Takes student name and registration number as input.

2. Accepts marks for multiple subjects.

3. Automatically calculates grades and grade points.

4. Handles Absent students.

5. Detects invalid marks and incorrect input.

6. Calculates total marks and average marks.

7. Calculates subject-wise credit points.

8. Calculates the final SGPA automatically.

9. Displays a clear subject-wise result.

10. Uses functions and loops for organized code.

11. Simple and beginner-friendly command-line interface.

12. Easy to modify for adding more subjects or changing the grading system.


## Technology Used

1. Python 3: Used as the main programming language to develop the Student Grade & SGPA Calculator.

2. VS Code: Used for writing, editing, and running the Python code.

3. Conditional Statements: if, elif, and else are used to assign grades based on marks.

4. Functions: Functions such as get_grade() and student_info() are used to organize the program.

5. Lists & Tuples: Used to store subject names, marks, and credit information.

6. Loops: A for loop is used to process each subject efficiently.

7. Exception Handling: try-except is used to handle incorrect or non-numeric input.

8. Input/Output: input() is used to collect student details and marks, while print() displays the result.

9. Arithmetic Operations: Used for calculating total marks, average marks, credit points, and SGPA.

10. No External Libraries: The project uses basic Python features and does not require additional packages.


## Steps to Run the Program

Step 1: Install Python

Make sure Python 3 is installed on your computer.

You can check it by opening Command Prompt or Terminal and running:

python --version

or:

python3 --version

Step 2: Save the Program

Copy the Python code into a file and save it as:

student_grade_calculator.py

Step 3: Open Terminal / Command Prompt

Go to the folder where the Python file is saved.

Step 4: Run the Program

Use:

python student_grade_calculator.py

If your system uses python3, run:

python3 student_grade_calculator.py

Step 5: Enter the Required Information

The program will ask for:

Enter your name:

Enter your Registration number:

Enter MAT1003 marks:

Enter CSE1021 marks:

Enter ENG1004 marks:

Enter CHY1006 marks:

Enter the required information and the program will display the result.


## Instructions for Testing

The program can be tested using different types of inputs to check whether all parts of the program work correctly.

1. Normal Marks

Input:

Name: Rahul

Registration Number: 24ABC1234

MAT1003: 95

CSE1021: 85

ENG1004: 75

CHY1006: 65

Expected Result:

MAT1003 → S → 10

CSE1021 → A → 9

ENG1004 → B → 8

CHY1006 → C → 7

Total Marks → 320

Average Marks → 80

SGPA → 8.6

2. Student is Absent

Enter:

MAT1003: absent

The program should display:

Marks: 0

Grade: N (Absent)

Grade Point: 0


The subject should contribute 0 credit points to the SGPA.

3. Failed Subject

Enter a mark below 40, for example:

MAT1003: 35

Expected result:

Marks: 35

Grade: F

Grade Point: 0

4. Invalid Marks

Enter a mark greater than 100:

MAT1003: 105

Expected result:

Invalid marks entered!

Similarly, entering a negative mark such as:

MAT1003: -5

should also result in:

Invalid marks entered!

5. Invalid Text Input

Enter something other than a number or "absent":

MAT1003: abc

Expected result:

Invalid marks entered!

6. SGPA Calculation

The program calculates SGPA using the following formula:

SGPA = Total Credit Points / Total Credits

The credit points for each subject are calculated as:

Credit Points = Subject Credits × Grade Point

For example, if a subject has:

Credits = 4

Grade Point = 9

then:

Credit Points = 4 × 9 = 36


7. Subjects and Credits

```text
Subject Code	          Credits
MAT1003	                     4
CSE1021         	         4
ENG1004         	         2
CHY1006         	         2
Total	                     12
```

8. Project Structure

The project contains one Python file:

```text
Student-Grade-Calculator/
│
└── student_grade_calculator.py
```

The main functions used are:

get_grade()

This function receives the marks and returns:

Marks

Grade

Grade Point

student_info()

This function:

Displays student information

Processes all subjects

Calculates total marks

Calculates average marks

Calculates credit points

Calculates SGPA

Displays the final result
