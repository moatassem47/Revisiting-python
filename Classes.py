class Student():
    def __init__(self,name, ID, age):
        self.name = name
        self.ID = ID
        self.age = age
        self.mail = name.lower() + "." + str(ID) + "@gmail.com"


    def getinfo(self):
     print(f"student name is {self.name} and id is {self.ID} and his age is {self.age}")
     print(f"studeent's email is: {self.mail}")

    def UpdateData(self,NewName=None, NewID=None):
       if NewName:
          self.name = NewName
       if NewID:
          self.ID = NewID
        


Student1 = Student("ahmed", 111, 20)

Student1.UpdateData("moatassem", 112) #it doesn't update the email for some reason???

Student1.getinfo()
