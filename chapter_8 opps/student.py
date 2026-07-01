class student:

    def __init__(self, fullname):
         self.name = fullname
         print("adding a new student")
    
    def welcome(self):
         print("welcome student")

s1 = student("harsh")
print(s1.name)
s1.welcome()
