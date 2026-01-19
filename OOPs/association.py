"""Teacher–Student association example."""


class Student:
    """Represents a student."""

    def __init__(self, name, total_marks):
        """Initialize a Student instance."""
        self.name = name
        self.total_marks = total_marks


class Teacher:
    """Represents a teacher."""

    def __init__(self, teacher_id, name):
        """Initialize a Teacher instance."""
        self.teacher_id = teacher_id
        self.name = name
        self.students = []

    def add_student(self, student):
        """Associate a student with the teacher."""
        self.students.append(student)

    def get_student_marks(self, student_name):
        """Return total marks of a student using name."""
        for student in self.students:
            if student.name == student_name:
                return student.total_marks
        return None

    def delete_student(self, student_name):
        """Delete a student using name."""
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                return True
        return False

    def sort_students_by_marks(self):
        """Sort students by total marks (ascending)."""
        self.students.sort(key=lambda student: student.total_marks)

    def sort_students_by_marks_desc(self):
        """Sort students by total marks (descending)."""
        self.students.sort(
            key=lambda student: student.total_marks,
            reverse=True
        )

    def grade_students(self):
        """Grade students based on their marks."""
        for student in self.students:
            if student.total_marks >= 70:
                print(f"{student.name} got Distinction")
            elif student.total_marks >= 45:
                print(f"{student.name} got First class")
            elif student.total_marks >= 35:
                print(f"{student.name} got Second class")
            else:
                print(f"{student.name} has failed")

    def display_students(self):
        """Display all students."""
        for student in self.students:
            print(student.name, student.total_marks)

    def delete_students_below_marks(self, min_marks):
        """Delete students with total marks below the given threshold."""
        self.students = [
            student for student in self.students
            if student.total_marks >= min_marks
        ]


def main():
    """Create students, associate them with a teacher"""
    student1 = Student("Narayani", 100)
    student2 = Student("Kavya", 56)
    student3 = Student("Kala", 45)
    student4 = Student("Hari", 70)
    student5 = Student("test", 40)
    student6 = Student("rain", 23)

    teacher = Teacher(123, "Tech1")
    teacher.add_student(student1)
    teacher.add_student(student2)
    teacher.add_student(student3)
    teacher.add_student(student4)
    teacher.add_student(student5)
    teacher.add_student(student6)

    print("---- Grades ----")
    teacher.grade_students()

    print("\nTotal number of students:", len(teacher.students))

    print("\n---- Sorted by marks (descending) ----")
    teacher.sort_students_by_marks_desc()
    teacher.display_students()

    print("\n---- Sorted by marks (ascending) ----")
    teacher.sort_students_by_marks()
    teacher.display_students()

    print("\n---- Get marks for Hari ----")
    marks = teacher.get_student_marks("Hari")
    print("Marks:", marks if marks is not None else "Student not found")

    print("\n---- Delete Hari ----")
    if teacher.delete_student("Hari"):
        print("Student deleted")
    else:
        print("Student not found")

    print("\n---- Final student list ----")
    teacher.display_students()

    teacher.delete_students_below_marks(40)

    print("\n---- Final student list ----")
    teacher.display_students()


if __name__ == "__main__":
    main()
