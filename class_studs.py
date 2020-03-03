class Humans:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.class_ = student #default value?

def grades(score1, score2, score3):
    a = score1
    b = score2
    c = score3
    a = input(int("Enter score 1 of 3: "))
    b = input(int("Enter score 2 of 3: "))
    c = input(int("Enter score 3 of 3: "))
    grades = a + b + c
    return grades

print ("Your ave. score is: " (a+b+c)/3)