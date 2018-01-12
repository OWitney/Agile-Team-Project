from ..SharedUI import *

class CourseUI(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.geometry("700x500")

        self.button_1 = Button(self,text="List Courses",command=self.listCourses)
        self.button_1.place(x=100,y=10)
        self.button_1.place(width=100,height=30)

        self.button_2 = Button(self, text="Add Course", command=self.addCourse)
        self.button_2.place(x=210,y=10)
        self.button_2.place(width=100,height=30)

        self.button_3 = Button(self, text="Add Teacher", command=self.setTeacher)
        self.button_3.place(x=560,y=50)
        self.button_3.place(width=100,height=30)

        self.button_4 = Button(self, text="Add Student", command=self.addStudent)
        self.button_4.place(x=560,y=90)
        self.button_4.place(width=100,height=30)

        self.button_5 = Button(self, text="Delete Student", command=self.delStudent)
        self.button_5.place(x=560,y=130)
        self.button_5.place(width=100,height=30)

        self.text_1 = Text(self)
        self.text_1.place(x=100, y=40)
        self.text_1.place(width=450,height=400)

        self.scrollbar1 = Scrollbar(self)
        self.scrollbar1.pack(side=RIGHT, fill=Y, in_=self.text_1)
        self.scrollbar1.config(command=self.text_1.yview)
        self.text_1.config(yscrollcommand = self.scrollbar1.set)

        self.list = Listbox(self, exportselection=False)
        self.list.place(x=10,y=40)
        self.list.place(width=80,height=400)

        self.input=Entry(self)
        self.input.place(x=100,y=450)
        self.input.place(width=450,height=20)

        self.text_1.config(state=DISABLED)

        self.updateList()
        self.mainloop()

    def listCourses(self):
        self.text_1.config(state=NORMAL)
        for item in courseList:
            self.text_1.insert(END,item.toString())
        self.text_1.config(state=DISABLED)

    def addCourse(self):
        self.text_1.config(state=NORMAL)
        self.text_1.insert(END,"Enter course name: \n")
        self.text_1.config(state=DISABLED)
        self.input.bind("<Return>", self.getCourse)

    def getCourse(self, event):
        course = self.input.get()
        self.input.unbind("<Return>")
        courseList.append(Course(course, None, None))
        self.input.delete(0, END)
        self.updateList()

    def setTeacher(self):
        self.text_1.config(state=NORMAL)
        self.text_1.insert(END, "Enter teachers name: \n")
        self.text_1.config(state=DISABLED)
        tempA = self.list.get(self.list.curselection())
        self.input.bind("<Return>", lambda event,x=tempA: self.getTeacher(event,x))

    def getTeacher(self,event,course):
        teacher = self.input.get()
        self.input.unbind("<Return>")
        a = checkCourse(course)
        b = checkTeacher(teacher)
        if a is not None and b is not None:
            a.setTeacher(b)
        self.input.delete(0, END)

    def addStudent(self):
        self.text_1.config(state=NORMAL)
        self.text_1.insert(END, "Enter student name: \n")
        self.text_1.config(state=DISABLED)
        tempA = self.list.get(self.list.curselection())
        self.input.bind("<Return>", lambda event,x=tempA: self.getStudent(event,x))

    def getStudent(self,event,course):
        student = self.input.get()
        self.input.unbind("<Return>")
        a = checkCourse(course)
        b = checkStudent(student)
        if a is not None and b is not None:
            a.addStudent(b)
        self.input.delete(0, END)

    def delStudent(self):
        self.text_1.config(state=NORMAL)
        self.text_1.insert(END, "Enter student name: \n")
        self.text_1.config(state=DISABLED)
        tempA = self.list.get(self.list.curselection())
        self.input.bind("<Return>", lambda event,x=tempA: self.pickStudent(event,x))

    def pickStudent(self,event,course):
        student = self.input.get()
        self.input.unbind("<Return>")
        a = checkCourse(course)
        b = checkStudent(student)
        if a is not None and b is not None:
            a.delStudent(b)
        self.input.delete(0, END)

    def updateList(self):
        self.list.delete(0, END)
        for item in courseList:
            self.list.insert(END, item.getName())