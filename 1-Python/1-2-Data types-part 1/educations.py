# from random import random
import random

# int
# number -> integer, complex, float
number = 2
print(float(number))
# برای تولید عدد تصادفی از تابع random استفاده میکنیم.

random_1 = random.random()
random_2 = random.sample(range(100), 3)
random_3 = random.choices(['ali','ashkan','zahra','hamid','mahnaz','meysam','hana','hamin'], k=3)
print(random_3)

# str


name = 'ashkan'
family = 'hassani'
print(name + ' ' + family)

b = ''
for i in range(10):
    b += "ali "
print(b)

my_string = "Hello world!"
print(my_string.split()) # خروجی متد split یک لیست است.
print(my_string.split('o'))
print(my_string[::-1])
print(my_string.startswith('b'))
print(my_string.endswith('!'))

# list
mylist = ["apple", "banana", "cherry"]
print(len(mylist))
print(mylist[0:2])
mylist[1] = 'orange'
print(mylist)
mylist[mylist.index('cherry')] = 'salam'
print(mylist)
mylist.insert(1, ['strawberry', 'slam'])
print(mylist)
print(mylist[1][0])
list_1 = mylist[1]
print(list_1[0])

# dict
my_dict = {'name': 'zahra', 'family': 'azimi', 'age': 35, 'children': ['hana', 'hamin']}
my_dict2 = {
    'name': 'zahra',
    'family': 'azimi',
    'age': 35,
    'children': ['hana', 'hamin']
}
print(my_dict['children'][0])
for k, v in my_dict.items():
    print(f"{k}:{v}")
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
student_data = {
    'ashkan': {
        'id': 1,
        'age': 30,
    },
    'zahra': {
        'id': 2,
        'age': 35
    }
}
print(student_data['zahra']['age'])

# set
#  لیست است فقط مقادیر تکراری را نمیپذیرد
my_list = [1, 1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
my_set = {1, 2, 3, 4}
print(my_set)


# tuple
my_tuple = ('ashkan', 'zahra', 'ali')
print(my_tuple[0])

# Boolean
name = bool([1])
print(name)

