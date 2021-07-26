# An easy function
# 函数可以多次调用
def greet(username):  # username 形参
    print("Hello, " + username + '.')


greet('SYB')


# 传递实参
# 1.位置实参
def describe_pet(animal_type, pet_name):
    print('I have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')


describe_pet('hamster', 'harry')
# 2.关键字实参
describe_pet(pet_name='pepper', animal_type='cat')


# 3.默认值
def describe_pet_1(pet_name, animal_type='dog'):  # 有默认值的参数放在最后
    print('I have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')


describe_pet_1('syb')


# Demos
# 1.
def make_shirt(size, note='I love python.'):
    print("The shirt is " + str(size) + ' and notes: ' + note)


# 2.
def describe_city(city, country='China'):
    print(city.title() + ' is in ' + country)


# 返回值 return
# 可选的实参 可以通过指定默认值为''

# 传递任意数量的实参
# 任意数量的实参必须放在最后
# 1. * -- 元组
def make_pizza(*toppings):
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)


make_pizza('pepperoni')
make_pizza('mushroom', 'green pepper', 'extra cheese')


# 2. ** -- 字典
def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Cai', 'Shanyu', location='Shantou', age=20)
print(user_profile)
