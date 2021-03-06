from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


class GUI:
    def __init__(self, f, g, h):
        self._root = Tk()
        self.loginWindow(f, g)
        self.logOut(h)

    def loginWindow(self, f, g):
        self._root.title("Tinder")
        self._root.minsize(400, 600)
        self._root.configure(background="#ff4e50")

        self._label1 = Label(self._root, text="Tinder", bg="#ffedbc")
        self._label1.configure(fg="#120D1A", font=("Constantia", 21, "bold"))
        self._label1.pack(pady=(30, 30))

        self._label2 = Label(self._root, text="E-mail:", bg="#dae2f8")
        self._label2.configure(font=("Constantia", 13))
        self._label2.pack(pady=(20, 5))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(0, 20), ipady=7, ipadx=30)

        self._label3 = Label(self._root, text="Password:", bg="#dae2f8")
        self._label3.configure(font=("Constantia", 13))
        self._label3.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._loginBtn = Button(self._root, text="LOGIN", bg="#e2e2e2", font=("Constantia", 15, "bold"), width=10, height=0, command=lambda: f(self._emailInput.get(), self._passwordInput.get()))
        self._loginBtn.pack()

        self._label4 = Label(self._root, text="Not a member?")
        self._label4.configure(bg="#FFA201", font=("Constantia", 16,"italic"))
        self._label4.pack(pady=(60, 5))

        self._regBtn = Button(self._root, text="Register Here", bg="#e5e5be", width=11, command=lambda: self.regWindow(g))
        self._regBtn.pack()

        self._root.mainloop()

    def regWindow(self, g):
        self._root = Tk()

        self._root.minsize(400, 600)
        self._root.configure(background="#FE894B")

        self._label1 = Label(self._root, text="Tinder", bg="#FE894B")
        self._label1.configure(font=("Constantia", 21, "bold"))
        self._label1.pack(pady=(12, 30))

        self._label2 = Label(self._root, text="Name: ")
        self._label2.configure(font=("Constantia", 13))
        self._label2.pack(pady=(5, 5))

        self._nameInput = Entry(self._root)
        self._nameInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._label3 = Label(self._root, text="Email: ")
        self._label3.configure(font=("Constantia", 13))
        self._label3.pack(pady=(5, 5))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._label4 = Label(self._root, text="Password: ")
        self._label4.configure(font=("Constantia", 13))
        self._label4.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._label5 = Label(self._root, text="Age")
        self._label5.configure(font=("Constantia", 13))
        self._label5.pack(pady=(5, 5))

        self._ageInput = Entry(self._root)
        self._ageInput = Entry(self._root)
        self._ageInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._label6 = Label(self._root, text="Gender")
        self._label6.configure(font=("Constantia", 13))
        self._label6.pack(pady=(5, 5))

        self._genderInput = Entry(self._root)
        self._genderInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._label7 = Label(self._root, text="City")
        self._label7.configure(font=("Constantia", 13))
        self._label7.pack(pady=(5, 5))

        self._cityInput = Entry(self._root)
        self._cityInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._label8 = Label(self._root, text="Bio:")
        self._label8.configure(font=("Constantia", 13))
        self._label8.pack(pady=(5, 5))

        self._bioInput = Entry(self._root)
        self._bioInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._registerBtn = Button(self._root, text="Register", width=21, height=2, command=lambda: g(self._nameInput.get(), self._emailInput.get(), self._passwordInput.get(), self._ageInput.get(), self._genderInput.get(), self._cityInput.get(), self._bioInput.get()))
        self._registerBtn.pack()

        self._root.mainloop()

    def clearScreen(self):
        for i in self._root.pack_slaves():
            i.destroy()

    def clearScreen1(self):
        for i in self._root.grid_slaves():
            i.destroy()


    def headerMenu(self, other, data):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile", command=lambda: self.myProfile(data, mode=1))
        filemenu.add_command(label="View Profile", command=lambda: other.viewUsers(0))
        filemenu.add_command(label="Edit Profile", command=lambda: self.editWindow(data, other.editHandler))
        filemenu.add_command(label="LogOut", command=lambda: self.logOut(other.logoutHandler))

        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="View Proposals", command=lambda: self.clearScreen())
        helpmenu.add_command(label="View Requests", command=lambda: self.clearScreen())
        helpmenu.add_command(label="View Matches", command=lambda: self.clearScreen())

    def logOut(self, h):
        self.clearScreen()
        self.clearScreen1()
        function = lambda: h(self)
        self.printMessage1("Logout", "Logout Successful", "info")
        self._root.destroy()
        self._root.mainloop()
        return self.__init__()


    def myProfile(self, data, mode=1):
        self.clearScreen()

        imageUrl = "image/wallpaper2you_167064.jpg"

        load = Image.open(imageUrl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack()

        self.label1 = Label(self._root, text="Name: ")
        self.label1.configure(font=("Constantia", 18))
        self.label1.pack()

        name = data[0][1]
        self.label2 = Label(self._root, text=name, bg="#FE894B")
        self.label2.configure(font=("Constantia", 18))
        self.label2.pack()

        self.label3 = Label(self._root, text="Age: ")
        self.label3.configure(font=("Constantia", 18))
        self.label3.pack()

        age = str(data[0][4])
        self.label4 = Label(self._root, text=age, bg="#FE894B")
        self.label4.configure(font=("Constantia", 18))
        self.label4.pack()

        self.label5 = Label(self._root, text="Not interested in: ")
        self.label5.configure(font=("Constantia", 18))
        self.label5.pack()

        gender = data[0][5]
        self.label6 = Label(self._root, text=gender, bg="#FE894B")
        self.label6.configure(font=("Constantia", 18))
        self.label6.pack()

        if mode == 1:
            return self.myProfile


    def mainWindow(self, other, data, mode, num=0):
        self.clearScreen()
        self.headerMenu(other, data)

        imageUrl = "image/wallpaper2you_167064.jpg"

        load = Image.open(imageUrl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack()

        self.label1 = Label(self._root, text="Name: ")
        self.label1.configure(font=("Constantia", 18))
        self.label1.pack(pady=(5,5))

        name = data[0][1]
        self.label2 = Label(self._root, text=name, bg="#FE894B")
        self.label2.configure(font=("Constantia", 18))
        self.label2.pack(pady=(5,5))

        self.label3 = Label(self._root, text="Age: ")
        self.label3.configure(font=("Constantia", 18))
        self.label3.pack()

        age = str(data[0][4])
        self.label4 = Label(self._root, text=age, bg="#FE894B")
        self.label4.configure(font=("Constantia", 18))
        self.label4.pack(pady=(5,5))

        self.label5 = Label(self._root, text="Not interested in: ")
        self.label5.configure(font=("Constantia", 18))
        self.label5.pack(pady=(5,5))

        gender = data[0][5]
        self.label6 = Label(self._root, text=gender, bg="#FE894B")
        self.label6.configure(font=("Constantia", 18))
        self.label6.pack(pady=(5,5))

        if mode == 2:
            frame = Frame(self._root)
            frame.pack(pady=(30, 5))
            btn1 = Button(frame, text="Previous", fg="#000000", bg="#ffedbc", command=lambda: other.viewUsers(num - 1))
            btn1.pack(side=LEFT,padx=(0,10))
            btn2 = Button(frame, text="Propose", fg="#000000", bg="#FC7003", command=lambda: other.propose(data[0][0]))
            btn2.pack(side=LEFT)
            btn3 = Button(frame, text="Next", fg="#000000", bg="#ffedbc", command=lambda: other.viewUsers(num + 1))
            btn3.pack(side=LEFT,padx=(10,0))


    def editWindow(self, data, g):
        self.clearScreen()
        self.headerMenu(self, data)

        self._root.minsize(400, 600)
        self._root.configure(background="#FF5733")
        #self._root.selection_clear()

        self._label1 = Label(self._root, text="Tinder", bg="#FF5733")
        self._label1.configure(font=("Constantia", 21, "bold"))
        self._label1.pack(pady=(12, 30))

        self._label2 = Label(self._root, text="Edit Name: ")
        self._label2.configure(font=("Constantia", 13))
        self._label2.pack(pady=(5, 5))

        self._nameInput = Entry(self._root)
        self._nameInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._label4 = Label(self._root, text="Change Password: ")
        self._label4.configure(font=("Constantia", 13))
        self._label4.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._label5 = Label(self._root, text="Update Age")
        self._label5.configure(font=("Constantia", 13))
        self._label5.pack(pady=(5, 5))

        self._ageInput = Entry(self._root)
        self._ageInput = Entry(self._root)
        self._ageInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._label6 = Label(self._root, text="Change Gender")
        self._label6.configure(font=("Constantia", 13))
        self._label6.pack(pady=(5, 5))

        self._genderInput = Entry(self._root)
        self._genderInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._label7 = Label(self._root, text="Edit City")
        self._label7.configure(font=("Constantia", 13))
        self._label7.pack(pady=(5, 5))

        self._cityInput = Entry(self._root)
        self._cityInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self._label8 = Label(self._root, text="Edit Bio:")
        self._label8.configure(font=("Constantia", 13))
        self._label8.pack(pady=(5, 5))

        self._bioInput = Entry(self._root)
        self._bioInput.pack(pady=(0, 21), ipady=7, ipadx=30)

        self.editBtn = Button(self._root, text="Update Profile", width=21, height=2, command=lambda: g(self._nameInput.get(), self._passwordInput.get(), self._ageInput.get(), self._genderInput.get(), self._cityInput.get(), self._bioInput.get()))
        self.editBtn.pack()

        self._root.mainloop()

    def printMessage(self, title, message):
        messagebox.showerror(title, message)

    def printMessage1(self, title, message, messageboxImage):
        messagebox._show(title, message, messageboxImage)

