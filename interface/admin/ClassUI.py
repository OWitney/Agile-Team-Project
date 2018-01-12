from ..SharedUI import *


class ClassUI(Frame):
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

        self.frame.place(x=200, y=75, width=400, height=450)

        self.display.place(width=408, height=450)
        self.display.config(font=("Courier", 9), state=DISABLED, yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.display.yview)

    def makeButtons(self):
        self.buttonA = Button(self, text="Get Class Info", command=self.findGroup)
        self.buttonB = Button(self, text="Add New Class", command=self.addGroupA)
        self.buttonC = Button(self, text="Delete Class", command=self.delGroup)

        self.buttonA.place(x=200, y=40, width=125, height=25)
        self.buttonB.place(x=338, y=40, width=125, height=25)
        self.buttonC.place(x=476, y=40, width=125, height=25)

        self.buttonD = Button(self, text="Cancel", command=self.cancel)
        self.buttonE = Button(self, text="Update Lists", command=self.updateList)

        self.buttonD.place(x=551, y=535, width=50, height=24)
        self.buttonE.place(x=25, y=535, width=150, height=25)

        self.buttonF = Button(self, text="Set Class Course", command=self.setClassCourse)
        self.buttonG = Button(self, text="Set Class Teacher", command=self.setTeacher)
        self.buttonH = Button(self, text="Add Class Student", command=self.addGroupStudent)
        self.buttonI = Button(self, text="Delete Class Student", command=self.delGroupStudent)

        self.buttonF.place(x=625, y=40, width=150, height=25)
        self.buttonG.place(x=625, y=140, width=150, height=25)
        self.buttonH.place(x=625, y=240, width=150, height=25)
        self.buttonI.place(x=625, y=340, width=150, height=25)

    def makeInput(self):
        self.input = Entry(self)
        self.input.place(x=200, y=535, width=340, height=24)

    def makeList(self):
        self.frame = Frame(self)
        self.listbox = Listbox(self.frame, exportselection=False)
        self.scrollbar = Scrollbar(self.frame)

        self.varA = StringVar()
        self.varA.set("Select Course")
        self.courseList = []
        if courseList:
            for item in courseList:
                self.courseList.append(item.getName())
        else:
            self.courseList.append(None)
        self.optionmenuA = OptionMenu(self, self.varA, *self.courseList)
        self.optionmenuA.place(x=625, y=80, width=150, height=25)

        self.varB = StringVar()
        self.varB.set("Select Teacher")
        self.teacherList = []
        if teacherList:
            for person in teacherList:
                self.teacherList.append(person.getFull())
        else:
            self.teacherList.append(None)
        self.optionmenuB = OptionMenu(self, self.varB, *self.teacherList)
        self.optionmenuB.place(x=625, y=180, width=150, height=25)

        self.varC = StringVar()
        self.varC.set("Select Student")
        self.studentList = []
        if studentList:
            for person in studentList:
                self.studentList.append(person.getFull())
        else:
            self.studentList.append(None)
        self.optionmenuC = OptionMenu(self, self.varC, *self.studentList)
        self.optionmenuC.place(x=625, y=280, width=150, height=25)

        self.varD = StringVar()
        self.varD.set("Select Student")
        self.courseStuList = []
        self.courseStuList.append(None)
        self.optionmenuD = OptionMenu(self, self.varD, *self.courseStuList)
        self.optionmenuD.place(x=625, y=380, width=150, height=25)

        self.optionmenuB.place(x=625, y=180, width=150, height=25)
        self.frame.place(x=25, y=40, width=150, height=485)
        self.listbox.place(width=133, height=485)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", self.onSelect)

    def updateList(self):
        self.listbox.delete(0, END)
        i = 0
        for item in groupList:
            self.listbox.insert(END, item.getName())
            if i % 2 != 0:
                self.listbox.itemconfig(i, bg="#EDEDED")
            i += 1

        self.optionmenuA["menu"].delete(0, END)
        self.varA.set("Select Course")
        for item in courseList:
            self.optionmenuA["menu"].add_command(label=item.getName(),
                                                 command=lambda value=item: self.varA.set(value.getName()))

        self.optionmenuB["menu"].delete(0, END)
        self.varB.set("Select Teacher")
        for person in teacherList:
            self.optionmenuB["menu"].add_command(label=person.getFull(),
                                                 command=lambda value=person: self.varB.set(value.getFull()))

        self.optionmenuC["menu"].delete(0, END)
        self.varC.set("Select Student")
        for person in studentList:
            self.optionmenuC["menu"].add_command(label=person.getFull(),
                                                 command=lambda value=person: self.varC.set(value.getFull()))

        self.onSelect(None)

    def onSelect(self, event):
        try:
            name = self.listbox.get(self.listbox.curselection())
            item = checkGroup(name)
            self.optionmenuD["menu"].delete(0, END)
            self.varD.set("Select Student")
            for person in item.getStudents():
                self.optionmenuD["menu"].add_command(label=person.getFull(),
                                                     command=lambda value=person: self.varD.set(value.getFull()))
        except TclError:
            self.optionmenuD["menu"].delete(0, END)
            self.varD.set("Select Student")

    def setTeacher(self):
        self.display.config(state=NORMAL)
        try:

            tempA = self.listbox.get(self.listbox.curselection())
            tempB = self.varB.get()
            item = checkGroup(tempA)
            person = checkTeacher(tempB)
            if item is not None and person is not None:
                self.display.insert(END, tempB + " is now in charge of " + tempA + ".\n\n")
                item.setTeacher(person)
            else:
                self.display.insert(END, "Invalid Selection detected.\n\n")
        except TclError:
            self.display.insert(END, "Invalid Selection detected.\n\n")
        self.display.config(state=DISABLED)

    def addGroupStudent(self):
        self.display.config(state=NORMAL)
        try:

            tempA = self.listbox.get(self.listbox.curselection())
            tempB = self.varC.get()
            item = checkGroup(tempA)
            person = checkStudent(tempB)
            if item is not None and person is not None:
                if not item.getStudents():
                    self.display.insert(END, tempB + " is now taking " + tempA + ".\n\n")
                    item.addStudent(person)
                elif person in item.getStudents():
                    self.display.insert(END, tempB + " is already taking " + tempA + ".\n\n")
                else:
                    self.display.insert(END, tempB + " is now taking " + tempA + ".\n\n")
                    item.addStudent(person)
            else:
                self.display.insert(END, "Invalid Selection detected.\n\n")
        except TclError:
            self.display.insert(END, "Invalid Selection detected.\n\n")
        self.display.config(state=DISABLED)
        self.onSelect(None)

    def delGroupStudent(self):
        self.display.config(state=NORMAL)
        try:

            tempA = self.listbox.get(self.listbox.curselection())
            tempB = self.varD.get()
            item = checkGroup(tempA)
            person = checkStudent(tempB)
            if item is not None and person is not None:
                self.display.insert(END, tempB + " is no longer taking " + tempA + ".\n")
                item.delStudent(person)
            else:
                self.display.insert(END, "Invalid Selection detected.\n")
        except TclError:
            self.display.insert(END, "Invalid Selection detected.\n\n")
        self.display.config(state=DISABLED)
        self.onSelect(None)

    def findGroup(self):
        self.display.config(state=NORMAL)
        try:
            temp = self.listbox.get(self.listbox.curselection())
            item = checkGroup(temp)
            self.display.insert(END, item.toString() + "\n\n")
        except TclError:
            self.display.insert(END, "INVALID: Issue with Selection.\n\n")
        self.display.config(state=DISABLED)
        self.display.see(END)

    def delGroup(self):
        self.display.config(state=NORMAL)
        try:
            temp = self.listbox.get(self.listbox.curselection())
            delGroup(temp)
            self.display.insert(END, "Class: " + temp + " removed from the system.\n")
        except TclError:
            self.display.insert(END, "INVALID: Issue with Selection.\n\n")
        self.display.config(state=DISABLED)
        self.display.see(END)
        self.updateList()

    def addGroupA(self):
        self.display.config(state=NORMAL)
        self.display.insert(END, "Enter Name of Class:\n")
        self.display.config(state=DISABLED)
        self.input.bind("<Return>", self.addGroupB)
        self.display.see(END)

    def addGroupB(self, event):
        self.input.unbind("<Return>")
        name = self.input.get()
        self.input.delete(0, END)
        self.display.config(state=NORMAL)
        if not name.isspace() and not name == "":
            groupList.append(Group(name, None, None, None))
            self.display.insert(END, name + "\n")
            self.display.insert(END, "Class " + name + " has been added to the system.\n\n")
        else:
            self.display.insert(END, "INVALID: Invalid input detected!\n\n")
        self.display.config(state=DISABLED)
        self.display.see(END)
        self.updateList()

    def setClassCourse(self):
        self.display.config(state=NORMAL)
        try:
            tempA = self.listbox.get(self.listbox.curselection())
            tempB = self.varA.get()
            item = checkGroup(tempA)
            course = checkCourse(tempB)
            item.setCourse(course)
        except TclError:
            self.display.insert(END, "INVALID: Issue with Selection.\n\n")
        self.display.config(state=DISABLED)
        self.display.see(END)


    def cancel(self):
        self.input.delete(0, END)
        self.input.unbind("<Return>")
        self.display.config(state=NORMAL)
        self.display.insert(END, "\nTask Canceled\n\n")
        self.display.config(state=DISABLED)
        self.display.see(END)
        self.listbox.selection_clear(0, END)
