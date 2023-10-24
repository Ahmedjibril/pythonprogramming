Courses = ["MIT","cybersecurity", "datascience"]

print(Courses)

#Accessing an array element

print(Courses[1])
print(Courses[2])

#for loop

for course in Courses:
    print(course)

#adding array in an element
Courses.append("android development")
print(Courses)

#REMOVING ELEMENT

Courses.remove("android development")
print(Courses)