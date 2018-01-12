from .Sharedlib import *


def newData():
    studentList.clear()
    teacherList.clear()
    courseList.clear()
    groupList.clear()
    gradeList.clear()
    stuNumList.clear()
    teachNumList.clear()


def loadAll():
    newData()
    loadStudents()
    loadTeachers()
    loadCourses()
    loadGroups()
    loadGrades()


def loadStudents():
    doc = open("files/students.csv")
    for line in doc:
        if line != "" and line != "\n":
            num = line.split(",")[0]
            name = line.split(",")[1]
            surname = line.split(",")[2].strip("\n")
            studentList.append(Student(name, surname, num))
            stuNumList.append(num.strip("s"))
    doc.close()


def loadTeachers():
    """
    Reads and converts the data from teachers.csv and adds them to
    the systems information storage.
    """
    doc = open("files/teachers.csv")
    for line in doc:
        if line != "" and line != "\n":
            num = line.split(",")[0]
            name = line.split(",")[1]
            surname = line.split(",")[2].strip("\n")
            teacherList.append(Teacher(name, surname, num))
            teachNumList.append(num.strip("t"))
    doc.close()


def loadCourses():
    doc = open("files/courses.csv")
    for line in doc:
        if line != "" and line != "\n":
            course = line.split(",")[0]
            teacher = checkTeacher(line.split(",")[1])
            students = getStudents(line, 2)
            courseList.append(Course(course, teacher, students))
    doc.close()


def loadGroups():
    doc = open("files/groups.csv")
    for line in doc:
        if line != "" and line != "\n":
            group = line.split(",")[0]
            teacher = checkTeacher(line.split(",")[1])
            course = checkCourse(line.split(",")[2])
            students = getCourseStudents(course, getStudents(line, 3))
            if course is not None:
                groupList.append(Group(group, course, teacher, students))
    doc.close()


def loadGrades():
    doc = open("files/grades.csv")
    for line in doc:
        if line != "" and line != "\n":
            student = checkStudent(line.split(",")[0])
            course = checkCourse(line.split(",")[1])
            desc = line.split(",")[2]
            grade = line.split(",")[3].strip("\n")
            if student is not None and course is not None:
                gradeList.append(Grade(student, course, desc, grade))


def saveAll():
    saveStudents()
    saveTeachers()
    saveCourses()
    saveGroups()
    saveGrades()


def saveStudents():
    doc = open("files/students.csv", "r+")
    doc.seek(0)
    for person in studentList:
        doc.write(person.writeData() + "\n")
    doc.truncate()
    doc.close()


def saveTeachers():
    doc = open("files/teachers.csv", "r+")
    doc.seek(0)
    for person in teacherList:
        doc.write(person.writeData() + "\n")
    doc.truncate()
    doc.close()


def saveCourses():
    doc = open("files/courses.csv", "r+")
    doc.seek(0)
    for item in courseList:
        doc.write(item.writeData() + "\n")
    doc.truncate()
    doc.close()


def saveGroups():
    doc = open("files/groups.csv", "r+")
    doc.seek(0)
    for item in groupList:
        doc.write(item.writeData() + "\n")
    doc.truncate()
    doc.close()


def saveGrades():
    doc = open("files/grades.csv", "r+")
    doc.seek(0)
    for item in gradeList:
        doc.write(item.writeData() + "\n")
    doc.truncate()
    doc.close()


def getStudents(line, start):
    students = []
    for i in range(start, len(line.split(","))):
        for person in studentList:
            if line.split(",")[i].strip("\n") == person.getFull():
                students.append(person)
    return students
