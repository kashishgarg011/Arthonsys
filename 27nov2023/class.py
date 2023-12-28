#1. Class Creation: Create a Python class `Student` with attributes like `name`, `age`, and `grade`. Include a method to display student information.

class Student:
     StudnetName="Kashish Garg"
     StudentAge=22
     StudentGrade="A"
     def Display():
         print("Student Name:" , str(Student.StudnetName) +
               "\n Student Age:" , str(Student.StudentAge) +
               "\n Student Grade:" , str(Student.StudentGrade))


print("Student Information:")
Student.Display()