class Grade:
    def __init__(self, student, course, desc, grade):
        self.myStudent = student
        self.myCourse = course
        self.myDesc = desc
        self.myGrade = grade

    def getStudent(self):
        return self.myStudent

    def getCourse(self):
        return self.myCourse

    def getDesc(self):
        return self.myDesc

    def getGrade(self):
        return self.myGrade

    def setStudent(self, student):
        self.myStudent = student

    def setCourse(self, course):
        self.myCourse = course

    def setDesc(self, desc):
        self.myDesc = desc

    def setGrade(self, grade):
        self.myGrade = grade

    def toString(self):
        return self.myStudent.toString() + "Course: " + self.myCourse.getName() + "\n Desc: " + self.myDesc \
               + "\n  Grade: " + self.myGrade + "\n"

    def getAssignment(self):
        return self.myStudent.getFull() + " | " + self.myCourse.getName() + " | " + self.myDesc

    def writeData(self):
        return self.myStudent.getFull() + "," + self.myCourse.getName() + "," + self.myDesc \
               + "," + self.myGrade + ","
