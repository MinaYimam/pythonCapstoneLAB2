#Part 3: Student dataclass

# Type in the dataclass code from the slides/video. You would have done this before class.

# Add one more field: gpa, a float.

# Write a main function to create some example Student objects with some example names, college_id and GPA values.
#
# Verify you can read the name, college ID and GPA for an example student.

# Verify when you print an example student, the GPA is included.

# Add some comments in your code to compare the dataclass version to the "traditional" version.

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: int
    gpa: float

def main():
    studentN = input('what is you name? ')
    studentid = input('what is your star id? ')
    gpa = input('what is your GPA')
    student = (studentN, studentid, gpa)
    print(f'Student nama, id, and GPA is {student}')

main()


