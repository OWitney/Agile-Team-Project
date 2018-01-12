from .SharedUI import *
from .admin import *


class LoginUI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Login")
        self.geometry("300x150")
        self.resizable(width=False, height=False)

        self.labelA = Label(self, text="Username")
        self.labelB = Label(self, text="Password")
        self.labelC = Label(self, text="Login")

        self.entryA = Entry(self)
        self.entryB = Entry(self, show="•")

        self.labelA.place(x=5, y=40)
        self.labelA.config(font=("Arial",11))
        self.labelA.place(width=75, height=30)

        self.labelB.place(x=5, y=70)
        self.labelB.config(font=("Arial",11))
        self.labelB.place(width=75, height=30)

        self.labelC.place(x=105, y=2)
        self.labelC.config(font=("Arial",18))
        self.labelC.place(width=100, height=30)

        self.entryA.place(x=90, y=42)
        self.entryA.place(width=175, height=25)

        self.entryB.place(x=90, y=72)
        self.entryB.place(width=175, height=25)

        self.button = Button(self, text="Login", command=lambda: self.login(None))
        self.button.place(x=125, y=105)
        self.button.place(width=60, height=30)
        self.bind("<Return>", self.login)
        self.mainloop()

    def login(self, event):
        username = self.entryA.get()
        password = self.entryB.get()
        valid = False

        for person in studentList:
            if username == person.getNum() and password == self.getPassword(person):
                valid = True
                self.destroy()

        for person in teacherList:
            if username == person.getNum() and password == self.getPassword(person):
                valid = True
                self.destroy()

        if username == "Admin" and password == "admin":
            valid = True
            self.destroy()
            AdminMenu()

        if not valid:
            messagebox.showerror("Invalid Input", "Incorrect information.\n Please try again.")


    def getPassword(self,person):
        password = person.getName()[0]
        password += person.getSurname()[0]
        return password.lower()