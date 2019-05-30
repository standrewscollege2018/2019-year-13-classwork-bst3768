print("hello world")
print(25)

first_name = "John"
last_name = "Smith"

print(first_name)
print("hello", first_name)

print("Hello {} {} ".format(first_name, last_name))

city_of_birth = input("Where were you born {}?".format(first_name))
print("i was also born in {}!".format(city_of_birth))

year_of_birth = int(input("what year were you born?"))

age = 2019 - year_of_birth
print("that makes you approximately {} year old".format(age))

my_list = ["bannanas", 25, True, "Golf"]

print(my_list[0])

my_list.append("table")
print(my_list)
my_list.insert(1, "Rinay")
my_list[1] = "shannon"
print(my_list)

del my_list[4]
print(my_list)

add = input ("what is your name?")
my_list.append(add)
print(my_list)