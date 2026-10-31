import gc

class Student:
    def __init__(self, name):
        self.name = name
        self.ref = None

gc.disable()

s1 = Student("Rahul")
s2 = Student("Amit")

s1.ref = s2
s2.ref = s1

print("Garbage collection before:", gc.collect())

del s1
del s2

print("Garbage collection after:", gc.collect())

gc.enable()

print("Garbage collection enabled.")
