from ..SharedUI import *
from .StudentUI import *
from .TeacherUI import *
from .CourseUI import *
#from .ClassUI import *
#from .GradeUI import *



class AdminMenu(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Admin Menu")
        self.focus_force()
        self.geometry("300x350")
        self.resizable(width=False, height=False)

        self.makeButtons()

        self.mainloop()


    def makeButtons(self):
        self.buttonA = Button(self, text="Student Panel", command=self.openStudent)
        self.buttonB = Button(self, text="Teacher Panel", command=self.openTeacher)
        self.buttonC = Button(self, text="Course Panel", command=self.openCourse)
        self.buttonD = Button(self, text="Class Panel", command=self.openClass)
        self.buttonE = Button(self, text="Grade Panel", command=self.openGrade)
        self.buttonF = Button(self, text="Exit", command=self.quit)

        self.buttonA.place(x=75, y=50, width=150, height=35)
        self.buttonB.place(x=75, y=90, width=150, height=35)
        self.buttonC.place(x=75, y=130, width=150, height=35)
        self.buttonD.place(x=75, y=170, width=150, height=35)
        self.buttonE.place(x=75, y=210, width=150, height=35)
        self.buttonF.place(x=75, y=280, width=150, height=35)

    def openStudent(self):
        StudentUI()

    def openTeacher(self):
        TeacherUI()

    def openCourse(self):
        CourseUI()

    def openClass(self):
        pass

    def openGrade(self):
        pass
