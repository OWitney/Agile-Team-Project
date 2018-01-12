from objects import *

studentList = []
teacherList = []
courseList = []
groupList = []
gradeList = []

stuNumList = []
teachNumList = []


def checkStudent(name):
    for person in studentList:
        if person.getFull() == name:
            return person


def checkTeacher(name):
    for person in teacherList:
        if person.getFull() == name:
            return person


def checkCourse(name):
    for item in courseList:
        if item.getName() == name:
            return item


def checkGroup(name):
    for item in groupList:
        if item.getName() == name:
            return item


def checkGrade(grade):
    for item in gradeList:
        if item.getAssignment() == grade:
            return item


def getCourseStudents(course, students):
    courseStudents = course.getStudents()
    for person in students:
        if person not in courseStudents:
            students.remove(person)
    return students


def checkStuNum(num):
    if num in stuNumList:
        return False
    else:
        return True


def checkTeachNum(num):
    if num in teachNumList:
        return False
    else:
        return True


def genStuNum():
    if len(stuNumList) == 0:
        return "1"
    return str(int(stuNumList[-1]) + 1)


def genTeachNum():
    if len(teachNumList) == 0:
        return "1"
    return str(int(teachNumList[-1]) + 1)

