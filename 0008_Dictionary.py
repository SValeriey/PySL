# Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Add key-value into dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Create a null dictionary
alien_1 = {}
print(alien_1)
alien_1['color'] = 'red'
alien_1['points'] = 1
print(alien_1)

# Change the key-value
alien_1['color'] = 'gray'
print(alien_1)

# Delete the key-value
del alien_1['points']
print(alien_1)

# Demos
# 1. 使用一个字典存储一个熟人的信息包括名、姓、年龄和居住地 打印出来
friend = {'first_name': 'Yuyon', 'last_name': 'Xie', 'age': 21, 'city': 'ShanTou'}
print(friend['first_name'], friend['last_name'], friend['age'], friend['city'])

# Traverse the dictionary
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():  # .items() 将字典中键值对组成元组并存在列表中返回
    print("\nKey: " + key)
    print("Value: " + value)
print()

# Traverse all the keys -- .keys()
for keys in user_0.keys():
    print(keys, end=' ')
print()
for keys in user_0:  # 默认遍历key值
    print(keys, end=' ')
print()
# Traverse in order -- sorted()
for keys in sorted(user_0.keys()):
    print(keys, end=' ')
print()

# Traverse all the values -- .values()
for value in user_0.values():
    print(value, end=' ')
print()

# set() 找出独一无二的项
favourite = {'jen': 'python', 'sarah': 'c++', 'edward': "java", 'syb': 'c++'}
for value in set(favourite.values()):
    print(value, end=' ')
print()

# Nested(嵌套)
# 1. Dictionary in List
alien_0 = {'color': 'green', 'points': 3}
alien_1 = {'color': 'red', 'points': 2}
alien_2 = {'color': 'yellow', 'points': 1}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# 2. List in Dictionary
pizza = {'crust': 'thick', 'toppings': ['mushroom', 'extra cheese']}
print(pizza)
# 3. Dictionary in Dictionary
