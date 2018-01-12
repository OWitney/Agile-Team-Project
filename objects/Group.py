class Group:
    def __init__(self, name, course, teacher, students):
        self.myName = name
        self.myCourse = course
        self.myTeacher = teacher
        self.myStudents = students

    def getName(self):
        return self.myName

    def getCourse(self):
        return self.myCourse

    def getTeacher(self):
        return self.myTeacher

    def getStudents(self):
        return self.myStudents

    def setName(self, name):
        self.myName = name

    def setCourse(self, course):
        self.myCourse = course

    def setTeacher(self, teacher):
        self.myTeacher = teacher

    def setTime(self, time):
        self.myTime = time

    def getTime(self):
        return self.myTime

    def setDay(self,day):
        self.myDay = day

    def getDay(self,day):
        return self.myDay

    def addStudent(self, student):
        if not self.myStudents:
            self.myStudents.append(student)
        elif student not in self.myStudents:
            self.myStudents.append(student)

    def delStudent(self, student):
        if student in self.myStudents:
            self.myStudents.remove(student)

    def toString(self):
        if self.myCourse is None:
            output = self.myName + "\nCourse:\n"
        else:
            output = self.myName + "\nCourse: " + self.myCourse.getName() + "\n"

        if self.myTeacher is None:
            output += " Teacher:\n  Students:\n"
        else:
            output += " Teacher: " + self.myTeacher.toString() + "  Students:\n"

        if self.myStudents:
            for i in range(0, len(self.myStudents)):
                output += "   " + self.myStudents[i].toString()
        else:
            output += "\n"
        return output

    def writeData(self):
        if self.myTeacher is None:
            output = self.myName + ",,"
        else:
            output = self.myName + "," + self.myTeacher.getFull() + ","

        if self.myCourse is None:
            output += ","
        else:
            output += self.myCourse.getName() + ","

        if self.myStudents:
            for i in range(0, len(self.myStudents)):
                output += self.myStudents[i].getFull() + ","
        return output
