from Person import Person
from Student import Student


personMichael= Person("Michael", "Miller", 30)
studentMaria= Student("Maria", "Sanchez", 28, 12345)

personMichael.printInfo()
studentMaria.printInfo()

studentMaria.printStudentInfo()
noNameStudent=Student()

noNameStudent.printStudentInfo()
