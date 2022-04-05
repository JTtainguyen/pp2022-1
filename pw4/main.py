from domain import *
from input import *
from output import *
import curses
import time
import math

def main(stdscr):
    menu = ['Add Student', 'Add Course', 'Add Mark', 'Show Student', 'Show Course', 'Show Mark', 'Student Average Gpa',
            'Sort Descending Order', 'Exit']

    students = []
    courses = []
    grades = []
    averageGpa = []
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row_idx = 0
    print_menu(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
            current_row_idx += 1
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 0:
            stdscr.clear()
            curses.echo()
            m = 0
            studentId, studentName, dob = add_students(stdscr)
            student = Student(studentId, studentName, dob)
            if (len(students) == 0):
                students.append(student)

            for j in range(len(students)):
                if (student == students[j]):
                    students[j] = student
                    m = 1
                    break
                if (m == 0):
                    students.append(student)
            stdscr.getch()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 1:
            stdscr.clear()
            curses.echo()
            m = 0
            courseId, courseName, noOfCredit = add_courses(stdscr)
            course = Course(courseId, courseName, noOfCredit)
            if (len(courses) == 0):
                courses.append(course)
            for j in range(len(courses)):
                if (course == courses[j]):
                    courses[j] = course
                    m = 1
                    break
                if (m == 0):
                    courses.append(course)
            stdscr.getch()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 2:
            stdscr.clear()
            curses.echo()
            m = 0
            studentId, courseId, mark = add_marks(stdscr)
            grade = Mark(studentId, courseId, mark)
            if (len(grades) == 0):
                grades.append(grade)
            for j in range(len(grades)):
                if (grades[j] == grade):
                    grades[j] = grade
                    m = 1
                    break
                if (m == 0):
                    grades.append(grade)
            stdscr.getch()
        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 3:
            stdscr.clear()
            curses.echo()
            studentId = add_student_id(stdscr)
            for i in range(0, len(students)):
                if (students[i].get_student_id() == studentId):
                    stdscr.addstr(6, 0,
                                  "StudentId: " + str(students[i].get_student_id()) + ", Student Name: " + students[
                                      i].get_name() + ", Date Of Birth: " + students[i].get_dob())
            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 4:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(2, 0, "Course ID")
            courseId = int(stdscr.getstr(3, 0).decode())
            for i in range(0, len(courses)):
                if (courses[i].get_course_id() == courseId):
                    stdscr.addstr(6, 0, "Course I: " + str(courses[i].get_course_id()) + ", Course name: " + courses[
                        i].get_course_name() + ", Credit: " + str(courses[i].get_course_credit()))
            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 5:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(2, 0, "Course Name")
            courseName = stdscr.getstr(3, 0).decode()
            showMarkInformationForSpecificCourse(courseName, students, courses, grades, stdscr)
            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 6:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(2, 0, "Student ID")
            studentId = int(stdscr.getstr(3, 0).decode())
            stdscr.addstr(5, 0, "Student average marks: ")
            averageMark = findStudentAverageMark(studentId, grades, courses)
            averageGpa.insert(len(averageGpa) - 1, [studentId, averageMark])
            stdscr.addstr(7, 0, str(averageMark))
            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 7:
            stdscr.clear()
            curses.echo()
            averageGpa.sort(key=lambda x: x[1], reverse=True)
            y = 2
            x = 0
            for i in range(len(averageGpa)):
                stdscr.addstr(y + i * 2, x, "StudentId: " + str(averageGpa[i][0]) + ", Student Average GPA: " +
                str(averageGpa[i][1]))

            stdscr.getch()

        elif (key == curses.KEY_ENTER or key in [10, 13]) and current_row_idx == 8:
            break

        print_menu(stdscr, current_row_idx)

        stdscr.refresh()
        
if __name__ == '__main__':
    curses.wrapper(main)
    
