#2. Object Instantiation: Instantiate multiple `Student` objects and showcase their attributes and methods.

class Student:
     Address="Jaipur"
     name="Kashish Garg"
     Branch="MCA"
     College="IIIM"
     def Show(self):
         print("IIIM College Student information")
         print("Student Name:",self.name +
               "\nBranch Name:", self.Branch +
               "\nCollege Name:", self.College +
               "\nStudent Address:", self.Address)
a =Student()
a.Show()
b=Student()
b.Address="Dholpur"
b.Show()