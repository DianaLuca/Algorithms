import random
import sys
import os

print("\n>>>>>>>>> Hello World! <<<<<<<<<<<\n")

name = "Derek"
print (name)

# Numbers Strings Lists Tuples Dictionaries
'''
Algrithmic operators:
+ - * / % ** //
'''

print ('5 + 2 = ', 5+2)
print ("5 - 2 = ", 5-2)
print ("5 * 2 = ", 5+2)
print ("5 / 2 = ", 5/2.0)
print ("5 % 2 = ", 5 % 2)
print ("5 ** 2 = ", 5**2)
print ("5 // 2 = ", 5//2.0)

quote = "\"Always remember you are unique"
multi_line_quote = '''just
like everyone else'''

print ("%s %s %s" % ('\nI like the quote:', quote, multi_line_quote))

print('\n>>>>>>>>>>> LISTS <<<<<<<<<<<\n')

grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                'Bananas']

print ('First Item:', grocery_list[0])
grocery_list[0] = "Green Juice"
print ('First Item:', grocery_list[0])
print (grocery_list[1:3])

other_events = ['Wash Car', 'Pick Up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]

print (to_do_list,end=" ")
print (to_do_list[1][1])

grocery_list.append('Onions')
print (grocery_list)

grocery_list.insert(1, 'Pickle')
print (grocery_list)

grocery_list.remove("Pickle")
grocery_list.sort()
print (grocery_list)
print ('grocery_list length: ', len(grocery_list))

del grocery_list[4]
print ('grocery_list length: ', len(grocery_list))

print (to_do_list)

to_do_list2 = other_events + grocery_list
print (to_do_list2)

print (len(to_do_list2))
print (max(to_do_list2))
print (min(to_do_list2))

pi_tuple = (1, 3, 2, 5, 4)
new_list_tuple = list(pi_tuple)
new_tuple = tuple(new_list_tuple)
print (pi_tuple, end=" ")
print (new_list_tuple,end=" ")
print (new_tuple, end=" ")

print('\n>>>>>>>>>>> DICTIONARIES <<<<<<<<<<<\n')
my_dict = {
    'key1' : 523,
    'key2' : 231,
    'key3' : 214
}
print (my_dict, end=" ")
print (my_dict['key1'])
print (min(my_dict.keys()))
print (min(my_dict.values()))
del my_dict['key1']
print (my_dict)

my_dict['key3'] = 0
print (len(my_dict))
print (my_dict.keys())
print (my_dict.values())

'''
Conditionals:
if else elif
> >= < <= == !=
'''

age = 30
if age >= 21:
    print ("You can drive a car")
else:
    print ("You are not allowed to drive cause you are not old enough")

'''
Logical operators:
and or not
'''

if (age >= 1 and age <= 18):
    print ("you get a birthday")
elif (age == 21 or age >= 65):
    print ("you get a bday")
elif not (age == 30):
    print ("you don't get a bday")
else:
    print ("you get a bday party yeah")

'''Loops
'''

for x in range(0, 10):
    print (x)

print ("\n")

print ("grocery list: ",grocery_list)
for y in grocery_list:
    print (y)

for x in [10,20,30,40]:
    print (x)

print ("\n")

dd_list = [[10, 20, 30], [100, 200, 300], [1000, 2000, 3000]]
for y in range(0, 3):
    for z in range(0, 3):
        print (dd_list[y][z],end=" ")
    print(end="\n")

'''
while loops
when you have no idea how many times you'll run through the loop
'''
print('\n>>>>>>>>>>> WHILE and RANDOM <<<<<<<<<<<\n')

random_num = random.randrange(0, 100)
print ("\nPrint while random_num is equal to 15")
while random_num != 15:
    print (random_num,end=" ")
    random_num = random.randrange(0, 100)

print ("\nAnd finally: ",random_num)

'''
iterate over a loop with while
'''

i = 0

while i <= 20:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        break
    else:
        i += 1
        continue
    i += 1

'''Functions'''
print('\n>>>>>>>>>>> FUNCTIONS <<<<<<<<<<<\n')


def calculate_sum(num1, num2):
    sum_num = num1 + num2
    return sum_num

print("add 1 + 2 =",calculate_sum(1, 2))
sum_of_nrs = calculate_sum(3, 4)
print("calculate_sum(3,4) =",sum_of_nrs)

print('\n>>>>>>>>>>> INPUT from the USER <<<<<<<<<<<\n')
print("What is your name? ")
#name = sys.stdin.readline()
print("Hello", name)

print ("What's your spouse name? ")
#spouse_name = input()
#print ("Name: {}".format(spouse_name))

print('\n>>>>>>>>>>> Strings <<<<<<<<<<<\n')
long_string = "i'll catch you if you fall - The Floor"
print(long_string)
print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4] + " be there")

print("%c is my %s letter and my number %d number is %.5f"
      %("x", "favourite", 1, 1.53))

print(long_string.capitalize())
print(long_string.find("Floor"))

print(long_string.isalnum())
print(long_string.isalpha())

print(long_string.replace("Floor", "Ground"))

print(long_string.strip()) #strip() - removes white spaces from the beginning and the end
quote_list = long_string.split(" ")
print(quote_list)

print('\n>>>>>>>>>>> FILE I/O input, output <<<<<<<<<<<\n')
print("Create a file test.txt:")
test_file = open("test.txt", "wb")
print(test_file.mode)
print(test_file.name)

print("\nWrite something in file:")
test_file.write(bytes("Write me to the file\n", 'UTF-8'))
test_file.close()

print("\nRead from file:")
test_file = open("test.txt", "r+")

text_in_file = test_file.read()
print(text_in_file)

print("\n>>>>>>>>>>>> OOP: Objects: CLASS <<<<<<<<<<<\n")

class Animal(object):
    __name = None #""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)

cat = Animal("Whiskers", 33, 10, "Meow")
print(cat.toString())

print("\n>>>>>>>>>>>> OOP: INHERITANCE <<<<<<<<<<<\n")

class Dog(Animal):
    __owner = None

    def __init__(self, owner, name, height, weight, sound):
        Animal.__init__(self, name, height, weight, sound)
        self.__owner = owner

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{}. His owner is {}".format(
                  Animal.toString(self),
                  self.__owner)

    def multiple_sounds(self, how_many=None):
        if(how_many is None):
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

spot = Dog("Derek", "Spot", 53, 27, "Ruff")
#print (spot.__dict__)

print(spot.toString())