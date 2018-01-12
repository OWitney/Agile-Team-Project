class Course:
    def __init__(self, name, teacher, students):
        self.myName = name
        self.myTeacher = teacher
        if not students:
            self.myStudents = []
        else:
            self.myStudents = students

    def getName(self):
        return self.myName

    def getTeacher(self):
        return self.myTeacher

    def getStudents(self):
        return self.myStudents

    def setName(self, name):
        self.myName = name

    def setTeacher(self, teacher):
        self.myTeacher = teacher

    def addStudent(self, student):
        if not self.myStudents:
            self.myStudents.append(student)
        elif student not in self.myStudents:
            self.myStudents.append(student)

    def delStudent(self, student):
        if student in self.myStudents:
            self.myStudents.remove(student)

    def toString(self):
        if self.myTeacher is None:
            output = self.myName + "\n Teacher:\n  Students:"
        else:
            output = self.myName + "\n Teacher: " + self.myTeacher.toString() + "  Students:\n"

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

        if self.myStudents:
            for i in range(0, len(self.myStudents)):
                output += self.myStudents[i].getFull() + ","
        return output
