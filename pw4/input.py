import math

def showMarkInformationForSpecificCourse(courseName, students, courses, grades, stdscr):
    courseId = ""
    studentName = ""
    studentGrade = ""
    x = 0
    y = 5
    num = 0
    for i in range(len(courses)):
    	#Use course name to get course ID
        if courses[i].get_course_name() == courseName:
            courseId = courses[i].get_course_id()
            break

    for j in range(len(grades)):
        if int(grades[j].get_course_id()) == int(courseId):
            for k in range(len(students)):
                if int(students[k].get_student_id()) == int(grades[j].get_student_id()):
                    stdscr.addstr(y + num, x, "Student Name: " + str(students[k].get_name()) + ', Student grade: ' + str(
                        grades[j].get_grade()))
                    num += 2
                    break


def findStudentAverageMark(studentId, marks, courses):
    studentGrades = []
    studentCredit = []
    totalCredit = 0
    totalMark = 0

    for i in range(len(marks)):
        if int(marks[i].get_student_id()) == int(studentId):
            studentGrades.insert(len(studentGrades) - 1, marks[i].get_grade())
            for j in range(len(courses)):
                if (int(courses[j].get_course_id()) == int(marks[i].get_course_id())):
                    studentCredit.insert(len(studentCredit) - 1, int(courses[j].get_course_credit()))
                    break
        else:
            continue
    for i in range(len(studentGrades)):
        totalMark += studentGrades[i] * studentCredit[i]
    for i in range(len(studentCredit)):
        totalCredit += int(studentCredit[i])
    averageGpa = totalMark / totalCredit
    return averageGpa
    
def add_students(stdscr):
    stdscr.addstr(2, 0, "ID")
    studentId = int(float(stdscr.getstr(3, 0).decode()))
    stdscr.addstr(4, 0, "Name")
    studentName = stdscr.getstr(5, 0).decode()
    stdscr.addstr(6, 0, 'Date Of Birth')
    dob = stdscr.getstr(7, 0).decode()
    return studentId, studentName, dob

def add_courses(stdscr):
    stdscr.addstr(2, 0, "ID")
    courseId = int(stdscr.getstr(3, 0).decode())
    stdscr.addstr(4, 0, "Name")
    courseName = stdscr.getstr(5, 0).decode()
    stdscr.addstr(6, 0, 'Number Of Credit')
    noOfCredit = int(stdscr.getstr(7, 0).decode())
    return courseId, courseName, noOfCredit
    
def add_marks(stdscr):
    stdscr.addstr(2, 0, "StudentId")
    studentId = stdscr.getstr(3, 0).decode()
    stdscr.addstr(4, 0, "Course ID")
    courseId = stdscr.getstr(5, 0).decode()
    stdscr.addstr(6, 0, 'Mark')
    mark = float(stdscr.getstr(7, 0).decode())
    mark = math.floor(mark)
    return studentId, courseId, mark
    
def add_student_id(stdscr):
    stdscr.addstr(2, 0, "Student ID")
    studentId = int(stdscr.getstr(3, 0).decode())
    return studentId
    
    
