cars = ['audi', 'bmw', 'toyota', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

friend = 'xyy'
print(friend == 'yyj')  # False
print(friend == 'xyy')  # True

# !=
if friend != 'yyj':
    print("He is xyy.")

# Multi-Conditions
age = 20
hobby = 'running'
# 1. and
if age <= 21 and hobby == 'running':
    print("Yes.")
# 2. or
if age >= 20 or hobby == 'swimming':
    print("Yes.")
# 3. in, not in
hobbies = ['eating', 'running', 'reading']
print('studying' in hobbies)  # False
print('drinking')

# if-else(-else-...)
# if-elif-else
age = 20
if age < 10:
    price = 0
elif age < 20:
    price = 5
else:
    price = 10
print(f"You should pay {price} dollar.")

# Demos
# 1.
age = int(input("Enter his age:"))
if age < 2:
    print("He is a baby.")
elif age < 4:
    print("He is learning walking.")
elif age < 13:
    print("He is a child.")
elif age < 20:
    print("He is a teenager.")
elif age < 65:
    print("He is an adult.")
else:
    print("He is an old man.")
# 2.
for i in range(1, 10):
    print(i, end='')
    if i == 1:
        print('st', end=' ')
    elif i == 2:
        print('nd', end=' ')
    elif i == 3:
        print('rd', end=' ')
    else:
        print('th', end=' ')
