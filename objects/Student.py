class Student:
    def __init__(self, name, surname, num):
        self.myName = name
        self.mySurname = surname
        if "s" not in num and len(str(num)) < 5:
            temp = str(num)
            while len(temp) < 5:
                temp = "0" + temp
            temp = "s" + temp
            self.myNum = temp
        else:
            self.myNum = num

    def getName(self):
        return self.myName

    def getSurname(self):
        return self.mySurname

    def getFull(self):
        return self.myName + " " + self.mySurname

    def getNum(self):
        return self.myNum

    def setName(self, name):
        self.myName = name

    def setSurname(self, surname):
        self.mySurname = surname

    def setNum(self, num):
        self.myNum = num

    def toString(self):
        return self.myNum + " | " + self.getFull() + "\n"

    def writeData(self):
        return self.myNum + "," + self.myName + "," + self.mySurname + ","
