# Comment:

# Example: count the 'a' in the name
name = input()
for i in name:
    pass  # todo
# Indention:
# متغیرها فقط در اسکوپ خودشون و اسکوپ های داخلی تر معتبر هستند
name2 = input()
b = 0
for i in name2:
    if i == 'a':
        b += 1
        print(b)
    print(b)
print(b)


# Input & Print:

# دستور input ذاتا از کاربر یک رشته را میگیرد.

name = input("Enter your name")

# برای اینکه مقدار ورودی کاربر عدد باشد از دستور int استفاده میکنیم.

age = int(input("How old are you?"))
print(name, age)
print(f"my name is {name}\n i am {age}")

# Variable & naming:
# انواع نامگذاری:
# camelCase: zahraAzimi --> javascript
# PascalCase: ZahraAzimi --> python: oop(define classes), Django
# snake_case: zahra_azimi --> python: variable, function
# ..........: zahra-azimi --> html & variable in javascript
name = input()
age = int(input())
mom_age = int(input())

# True & False:

# درست --> True
# غلط --> False
# True --> 1
# False --> 0

# Operators (calc,compare,add-in-self,and, or, not, in, is):

# عملگر ریاضی
ashkan_age = 30
zahra_age = 35
print(ashkan_age + zahra_age)
print(ashkan_age - zahra_age)
print(ashkan_age * zahra_age)
print(ashkan_age ** zahra_age)
print(ashkan_age / zahra_age)
print(ashkan_age // zahra_age)
print(ashkan_age % zahra_age)

# عملگرهای مقایسه‌ای
ashkan_age = 30
zahra_age = 35
print(ashkan_age == zahra_age)
print(ashkan_age >= zahra_age)
print(ashkan_age <= zahra_age)
print(ashkan_age != zahra_age)
print(ashkan_age > zahra_age)
print(ashkan_age < zahra_age)

# عملگر ذخیره در خود

ashkan_age = 30
ashkan_age += 10
print(ashkan_age)
ashkan_age -= 10
print(ashkan_age)
ashkan_age = [1, 2, 4]
zahra_age = [1, 2, 4]
print(ashkan_age is zahra_age)

