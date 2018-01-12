from .Sharedlib import *


def addStudent(name, surname):
    num = genStuNum()
    studentList.append(Student(name, surname, num))
    stuNumList.append(num)


def delStudent(name):
    student = checkStudent(name)
    studentList.remove(student)
    for item in courseList:
        if student in item.getStudents():
            item.delStudent(student)
    for item in groupList:
        if student in item.getStudents():
            item.delStudent(student)


def addTeacher(name, surname):
    num = genTeachNum()
    teacherList.append(Teacher(name, surname, num))
    teachNumList.append(num)


def delTeacher(name):
    teacher = checkTeacher(name)
    teacherList.remove(teacher)
    for item in courseList:
        if item.getTeacher() == teacher:
            item.setTeacher(None)
    for item in groupList:
        if item.getTeacher() == teacher:
            item.setTeacher(None)


def addCourse(name, teacherName, studentList):
    teacher = checkTeacher(teacherName)
    students = convertStudents(studentList)
    courseList.append(Course(name, teacher, students))


def delCourse(name):
    course = checkCourse(name)
    courseList.remove(course)


def addGroup(name, courseName, teacherName, studentList):
    course = checkCourse(courseName)
    teacher = checkTeacher(teacherName)
    students = convertStudents(studentList)
    groupList.append(Group(name, course, teacher, students))


def delGroup(name):
    group = checkGroup(name)
    groupList.remove(group)


def addGrade(studentName, courseName,desc,grade):
    student = checkStudent(studentName)
    course = checkCourse(courseName)
    gradeList.append(Grade(student, course,desc, grade))


def delGrade(string):
    grade = checkGrade(string)
    gradeList.remove(grade)


def addCourseStudent(courseName, studentName):
    course = checkCourse(courseName)
    student = checkStudent(studentName)
    if student not in course.getStudents():
        course.addStudent(student)


def delCourseStudent(courseName, studentName):
    course = checkCourse(courseName)
    student = checkStudent(studentName)
    if student in course.getStudents():
        course.delGrade(student)


def addGroupStudent(groupName, studentName):
    group = checkGroup(groupName)
    student = checkStudent(studentName)
    if student not in group.getStudents():
        group.addStudent(student)


def delGroupStudent(groupName, studentName):
    group = checkGroup(groupName)
    student = checkStudent(studentName)
    if student in group.getStudents():
        group.delGrade(student)


def setCourseTeacher(courseName, teacherName):
    course = checkCourse(courseName)
    teacher = checkTeacher(teacherName)
    course.setTeacher(teacher)


def setGroupCourse(groupName, courseName):
    group = checkGroup(groupName)
    course = checkCourse(courseName)
    group.setCourse(course)


def setGroupTeacher(groupName, teacherName):
    group = checkGroup(groupName)
    teacher = checkTeacher(teacherName)
    group.setTeacher(teacher)


def convertStudents(student):
    students = []
    for person in studentList:
        for name in student:
            if name == person.getFull():
                students.append(person)
    return students

def setClassDate(groupName,time,day):
    group = checkGroup(groupName)
    group.setTime(time)
    group.setDay(day)
