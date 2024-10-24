class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} (ID: {self.student_id}) - Average Grade: {self.get_average():.2f}"


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        if not self.students:
            print("No students enrolled.")
            return
        for student in self.students:
            print(student)


def input_student():
    name = input("Enter the name of the student: ")
    student_id = input("Enter ID of the student: ")
    return Student(name, student_id)


def input_course():
    course_name = input("Enter course name: ")
    return Course(course_name)


# Example usage
course = input_course()
while True:
    student = input_student()
    course.add_student(student)
    more_students = input("Add another student? (yes/no): ").strip().lower()
    if more_students != 'yes':
        break

course.list_students()
