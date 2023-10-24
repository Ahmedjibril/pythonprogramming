# datatype

numbers = 20  # int
seconds = 7.04  # float
text = "hellow_man"  # string

isponitrointeresting = True  # boolean

# store multiple values in a single variables

cars = ["Toyota", "nissan", "vw"]  # list can be changed the value

fruits = ("banana", "apple", "mango")  # turple cannot change the value
countries = {"kenya", "nigeria", "uganda"}  # set -unordered and unchangeable

Details = {
    "firstname": "ahmed",
    "age": "29",
    "course": "web development"
}

print(seconds)
print(text)
print(isponitrointeresting)
print(cars)
print(fruits)
print(countries)
print(Details)
# determine data type

print(type(numbers))
print(type(Details))
print(type(countries))

#typecasting ---converting one data type to another

print(float(numbers))
print(int(seconds))