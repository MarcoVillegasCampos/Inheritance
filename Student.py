
from Person import Person


class Student(Person):

    def __init__(self, fN, lN, age, id ):
        super().__init__(fN, lN, age)
        self.identifier=id
    
    def __init__(self):
        super().__init__("N/A", "N/A", -1)
        self.identifier=-1
        





    def printInfo(self):# from a parent class
        print("Printing from Student")
        print(f"First name: {super().firstName} Last name: {self.lastName}Identifier: {self.identifier}")


    def printStudenInfo (self):
        #super().printInfo()
        #print("Printing from Student")
        self.printInfo() # only 
        super().printInfo()
        #print(f"First name: {super().firstName} Last name: {self.lastName}Identifier: {self.identifier}")