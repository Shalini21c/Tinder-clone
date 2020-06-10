import guihelper
import dbhelper

class Tinder(guihelper.GUI):
    def __init__(self):
        self._dbObject = dbhelper.DBHelper()
        super().__init__(self.loginHandler, self.regHandler, self.logoutHandler)
    def loginHandler(self,email,password):
        response = self._dbObject.search("email", email, "password", password, "users")
        if len(response) == 0:
            print("Invalid email/password")
        else:
            self.user_id = response[0][0]
            self.doLogin(response)

    def doLogin(self, data):
        self.mainWindow(self, data, mode=1)

    def viewUsers(self, num):
        data = []
        response = self._dbObject.searchOne('user_id', self.user_id, 'users', 'NOT LIKE')

        if num < 0:
            self.printMessage("ERROR","No users before this one")
        elif num > len(response)-1:
            self.printMessage("ERROR","No more users")
        else:
            x = response[num]
            data.append(x)
            self.mainWindow(self, data, mode=2, num=num)

    def regHandler(self, name, email, password, age, gender, city, bio):
        mydict = {'user_id': "NULL", 'fname': name, 'email': email, 'password': password, 'age': age, 'gender': gender, 'bg': 'avatar.jpg', 'city': city, 'bio': bio}
        flag = self._dbObject.insert(mydict, 'users')
        if flag == 0:
            print("Registration Failed")
        else:
            print("Registration Successful")


    def editHandler(self, name, password, age, gender, city, bio):
        flag = self._dbObject.update(name, password, age, gender, city, bio, "users", self.user_id)
        if flag == 0:
            print("Error in Profile Update")
        else:
            print("Update Successful")

    def propose(self, juliet):
        data = self._dbObject.search('romeo', self.user_id, 'juliet', juliet, 'proposals')
        if len(data) > 0:
            self.printMessage("Error", "Already proposal sent")
        else:
            mydict = {'proposals': 'NULL', 'romeo': self.user_id, 'juliet': juliet}
            response = self._dbObject.insert(mydict, "proposals")

            if response == 1:
                self.printMessage1("Successful", "Proposals sent successfully", "info")
            else:
                self.printMessage1("Proposal Failed", "Unsuccessful attempt!!!", "warning")


    def logoutHandler(self):
        self.logOut(self)



obj1=Tinder()


