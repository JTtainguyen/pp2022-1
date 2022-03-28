class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def get_student_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def set_student_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob

    def displayStudentInformation(self):
        print("Student Id: %d, Student name: %s, Student dob: %s" % (self.id, self.name, self.dob))


class Course:
    def __init__(self, courseId, courseName):
        self.courseId = courseId
        self.courseName = courseName

    def get_course_id(self):
        return self.courseId

    def get_course_name(self):
        return self.courseName

    def set_course_name(self, courseName):
        self.courseName = courseName

    def set_course_id(self, courseId):
        self.courseId = courseId

    def displayCourseInformation(self):
        print("CourseId: {}, Course name: {}".format(self.courseId, self.courseName))


class Mark:
    def __init__(self, studentId, courseId, grade):
        self.studentId = studentId
        self.courseId = courseId
        self.grade = grade

    def get_student_id(self):
        return self.studentId

    def get_course_id(self):
        return self.courseId

    def get_grade(self):
        return self.grade

    def set_student_id(self, studentId):
        self.studentId = studentId

    def set_course_id(self, courseId):
        self.courseId = courseId

    def set_grade(self, grade):
        self.grade = grade

    def displayStudentMark(self, studentName):
        print("Student Id: {}, Student Name: {}, Student Mark: {} ".format(self.studentId, studentName, self.grade))


def enterNumberOfStudents():
    numberOfStudents = int(input("Enter the number of students: \n"))
    return numberOfStudents


def enterStudentsInfo():
    studentId = int(input("Enter student Id \n"))
    studentName = input("Enter student name \n")
    studentDob = input("Enter student date of birth \n")
    return studentId, studentName, studentDob


def enterNumberOfCourses():
    numberOfCourses = int(input("Enter the number of courses \n"))
    return numberOfCourses


def enterCoursesInfo():
    courseId = int(input("Enter course Id \n"))
    courseName = input("Enter course name \n")
    return courseId, courseName


def showMarkInformationForSpecificCourse(courseName, students, courses, grades):
    courseId = 0
    for i in range(len(courses)):
        if (courses[i].get_course_name() == courseName):
            courseId = courses[i].get_course_id()
            print("CourseId: ", courseId)
            break

    for j in range(len(grades)):
        if int(grades[j].get_course_id()) == int(courseId):
            for k in range(len(students)):
                if int(students[k].get_student_id()) == int(grades[j].get_student_id()):
                    grades[j].displayStudentMark(students[k].get_name())
                    break


if __name__ == "__main__":
    students = []
    courses = []
    grades = []
    numberOfStudents = enterNumberOfStudents()
    for i in range(0, numberOfStudents):
        studentId, studentName, studentDob = enterStudentsInfo()
        student = Student(studentId, studentName, studentDob)
        students.append(student)

    numberOfCourses = enterNumberOfCourses()
    for i in range(0, numberOfCourses):
        courseId, courseName = enterCoursesInfo()
        course = Course(courseId, courseName)
        courses.append(course)

    choice = input("y for enter studentMark, n for not \n")
    while (choice == "y"):
        s = input("enter m for marks input other to cancel ")
        if (s == "m"):
            studentId = int(input("Enter student Id \n"))
            courseId = input("Enter courseId \n")
            mark = float(input("Enter student mark \n"))
            grade = Mark(studentId, courseId, mark)
            grades.append(grade)
        else:
            break

    print("Show Student Info: ")
    studentId = int(input("Enter student Id \n"))
    for i in range(0, len(students)):
        if (students[i].get_student_id() == studentId):
            students[i].displayStudentInformation()
            break

    print("Show Course Info: ")
    courseId = int(input("Enter course Id \n"))
    for i in range(0, len(courses)):
        if (courses[i].get_course_id() == courseId):
            courses[i].displayCourseInformation()
            break
    print("Show mark for specific course \n")
    courseName = input("Enter course name ")
    showMarkInformationForSpecificCourse(courseName, students, courses, grades)
