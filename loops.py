# while loops

number = 20
while number <= 25:
    print(number)
    number +=1

# decrement

num = 30
while num >= 25:
    print(num)
    num -=1

    # for loops
languages =["java","C", "python"]
for x in languages:
    print(x)

    # for range
    for z in range (30, 40):
        print(z)

        for y in range (1, 10, 2):
            print(y)


def students(firstname,course, age):
    print(firstname,course, age)

students("glory","datascience","27")
students("mark","Software","20")
students("MUsa","IT","23")

# built-in libray

y = max (40, 30, 59, 34,60)
print(y)

x = min (50,30,50,45)
print(x)
