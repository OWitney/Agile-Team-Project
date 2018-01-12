from ..SharedUI import *


class GradeUI(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.focus_force()
        self.place(width=800, height=600)
        self.config(background="#D3E3E8")

        self.makeDisplay()
        self.makeButtons()
        self.makeInput()
        self.makeList()
        self.updateList()

    def makeDisplay(self):
        self.frame = Frame(self)
        self.display = Text(self.frame, wrap=WORD)
        self.scrollbar = Scrollbar(self.frame)

        self.frame.place(x=275, y=75, width=325, height=450)

        self.display.place(width=313, height=450)
        self.display.config(font=("Courier", 9), state=DISABLED, yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.display.yview)

    def makeButtons(self):
        self.buttonA = Button(self, text="Grade Info", command=self.getGrade)
        self.buttonB = Button(self, text="Edit Grade", command=self.editGradeA)
        self.buttonC = Button(self, text="Delete Grade", command=self.delGrade)

        self.buttonA.place(x=275, y=40, width=100, height=25)
        self.buttonB.place(x=390, y=40, width=100, height=25)
        self.buttonC.place(x=500, y=40, width=100, height=25)

        self.buttonD = Button(self, text="Cancel", command=self.cancel)
        self.buttonE = Button(self, text="Update Lists", command=self.updateList)

        self.buttonD.place(x=551, y=535, width=50, height=24)
        self.buttonE.place(x=25, y=535, width=225, height=25)

        self.buttonF = Button(self, text="Add New Grade", command=self.addGradeA)

        self.buttonF.place(x=625, y=40, width=150, height=25)

    def makeInput(self):
        self.input = Entry(self)
        self.input.place(x=275, y=535, width=265, height=24)

    def makeList(self):
        self.frameA = Frame(self)
        self.listboxA = Listbox(self.frameA, exportselection=False)
        self.scrollbarA = Scrollbar(self.frameA)

        self.varA = StringVar()
        self.varA.set("Select Course")
        self.courseList = []
        for item in courseList:
            self.courseList.append(item.getName())
        self.optionmenuA = OptionMenu(self, self.varA, *self.courseList)
        self.optionmenuA.place(x=625, y=80, width=150, height=25)

        self.varB = StringVar()
        self.varB.set("Select Student")
        self.studentList = []
        for person in studentList:
            self.studentList.append(person.getFull())
        self.optionmenuB = OptionMenu(self, self.varB, *self.studentList)
        self.optionmenuB.place(x=625, y=120, width=150, height=25)

        self.frameA.place(x=25, y=40, width=225, height=485)
        self.listboxA.place(width=208, height=485)
        self.scrollbarA.pack(side=RIGHT, fill=Y)
        self.scrollbarA.config(command=self.listboxA.yview)
        self.listboxA.config(yscrollcommand=self.scrollbarA.set)

    def updateList(self):
        self.listboxA.delete(0, END)
        i = 0
        for item in gradeList:
            self.listboxA.insert(END, item.getAssignment())
            if i % 2 != 0:
                self.listboxA.itemconfig(i, bg="#EDEDED")
            i += 1

        self.optionmenuA["menu"].delete(0, END)
        self.varA.set("Select Course")
        for item in courseList:
            self.optionmenuA["menu"].add_command(label=item.getName(),
                                                 command=lambda value=item: self.varA.set(value.getName()))

        self.optionmenuB["menu"].delete(0, END)
        self.varB.set("Select Student")
        for person in studentList:
            self.optionmenuB["menu"].add_command(label=person.getFull(),
                                                 command=lambda value=person: self.varB.set(value.getFull()))

    def getGrade(self):
        self.display.config(state=NORMAL)
        try:
            item = self.listboxA.get(self.listboxA.curselection())
            grade = checkGrade(item)
            self.display.insert(END, grade.toString() + "\n")
        except TclError:
            self.display.insert(END, "Error\n\n")
        self.display.config(state=DISABLED)
        self.display.see(END)

    def delGrade(self):
        self.display.config(state=NORMAL)
        try:
            temp = self.listboxA.get(self.listboxA.curselection())
            delGrade(temp)
            self.display.insert(END, "Grade removed.\n")
        except TclError:
            self.display.insert(END, "Invalid Selection detected.\n\n")
        self.display.config(state=DISABLED)
        self.display.see(END)
        self.updateList()

    def editGradeA(self):
        self.display.config(state=NORMAL)
        try:
            item = self.listboxA.get(self.listboxA.curselection())
            grade = checkGrade(item)
            self.input.bind("<Return>",lambda event,x=grade:self.editGradeB(event,x))
            self.display.insert(END,"Enter new value for this grade.\n")
        except TclError:
            self.display.insert(END, "Error\n\n")
        self.display.config(state=DISABLED)
        self.display.see(END)

    def editGradeB(self,event,grade):
        self.display.config(state=NORMAL)
        value = self.input.get()
        self.input.unbind("<Return>")
        self.input.delete(0,END)
        grade.setGrade(value)
        self.display.insert(END, "Grade value changed.\n")
        self.display.config(state=DISABLED)
        self.display.see(END)

    def addGradeA(self):
        self.display.config(state=NORMAL)
        try:
            tempA = self.varA.get()
            tempB = self.varB.get()
            item = checkCourse(tempA)
            person = checkStudent(tempB)
            if item is not None and person is not None:
                self.display.insert(END, "Enter Grade Description:\n")
                self.input.bind("<Return>",lambda event,x=tempA,y=tempB:self.addGradeB(event,x,y))
            else:
                self.display.insert(END, "Invalid Selection detected.\n\n")
        except TclError:
            self.display.insert(END, "Invalid Selection detected.\n\n")
        self.display.config(state=DISABLED)
        self.display.see(END)


    def addGradeB(self,event,item,person):
        self.display.config(state=NORMAL)
        desc = self.input.get()
        self.input.delete(0,END)
        self.display.insert(END,"Enter Grade Value:\n")
        self.input.bind("<Return>",lambda event,x=item,y=person,z=desc: self.addGradeC(event,x,y,z))
        self.display.config(state=DISABLED)
        self.display.see(END)

    def addGradeC(self,event,item,person,desc):
        self.display.config(state=NORMAL)
        grade = self.input.get()
        addGrade(person, item, desc, grade)
        self.display.config(state=DISABLED)
        self.input.unbind("<Return>")
        self.input.delete(0,END)
        self.display.insert(END,"Grade for " + person + " in " + item + " added.\n")
        self.display.config(state=DISABLED)
        self.display.see(END)
        self.updateList()

    def cancel(self):
        self.input.delete(0, END)
        self.input.unbind("<Return>")
        self.display.config(state=NORMAL)
        self.display.insert(END, "\nTask Canceled\n\n")
        self.display.config(state=DISABLED)
        self.display.see(END)
        self.listboxA.selection_clear(0, END)
