from tkinter import *
from tkinter import simpledialog
from ..SharedUI import *


class StudentUI(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.dispaynames = Button(self, text="Display All Names", command=self.displayAllNames, height=1,
                                  width=13).place(x=17, y=35)
        self.findnames = Button(self, text="Find Names", command=self.displayName, height=1,
                                width=13).place(x=17, y=65)
        self.AddNames = Button(self, text="Add A Name", command=self.AddName, height=1, width=13).place(
            x=17, y=95)
        self.deletname = Button(self, text="Delete A Name", command=self.Dname, height=1,
                                width=13).place(x=17, y=155)
        self.quite = Button(self, text="Quit", command=self.destroy, height=1, width=13).place(x=17, y=185)

        self.text = Text(self, width=40, height=25, wrap=WORD)
        self.text.place(x=125, y=35)
        self.text.place(width=320, height=400)
        self.text.config(state=DISABLED)

        S = Scrollbar(self)
        self.text.config(yscrollcommand=S.set)
        S.pack(side=RIGHT, fill=Y, in_=self.text)
        S.config(command=self.text.yview)

        self.geometry("450x450")
        self.title("Students")

        self.mainloop()

    def displayAllNames(self):
        output = ""
        for person in studentList:
            output += person.toString()
        self.text.config(state=NORMAL)
        self.text.insert(END, output)
        self.text.config(state=DISABLED)

    def displayName(self):
        name = simpledialog.askstring("Name", "please enter the name")
        found = False
        for person in studentList:
            if person.getName() == name:
                self.text.config(state=NORMAL)
                self.text.insert(END, person.toString() + "\n")
                self.text.config(state=DISABLED)
                found = True
        if found == False:
            self.text.config(state=NORMAL)
            self.text.insert(END, "sorry the Name " + name + " is not correct" + "\n")
            self.text.config(state=DISABLED)
        return

    def AddName(self):
        d = {}
        newname = simpledialog.askstring("Name", "please enter the name")
        newsurname = simpledialog.askstring("Surname", "please enter the surname")
        addStudent(newname, newsurname)
        self.text.config(state=NORMAL)
        self.text.insert(END, "WE have added " + newname + ' ' + newsurname + ' to the list!!! \n')
        self.text.config(state=DISABLED)

    def Dname(self):
        found = False
        name = simpledialog.askstring("Name", "enter the name of the student")
        surname = simpledialog.askstring("Surname", " enter the surname")
        for person in studentList:
            if person.getName() == name and person.getSurname() == surname:
                delStudent(name + " " + surname)
                found = True
                self.text.config(state=NORMAL)
                self.text.insert(END, "WE have deleted " + name + ' ' + surname + ' from the list!!! \n')
                self.text.config(state=DISABLED)
        if found == False:
            self.text.config(state=NORMAL)
            self.text.insert(END, "sorry the name not in the list \n")
            self.text.config(state=DISABLED)
