# 创建Dog类
class Dog:
    """模拟小狗的简单尝试"""
    """类中的函数称为方法"""

    def __init__(self, name, age):  # __init__() 方法在创建类时会自动运行，适合用于初始化属性
        """初始化属性name和age，self是指向类自己的参数"""
        self.name = name  # 属性 可以通过实例访问的变量
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + ' rolled over!')


my_dog = Dog('willie', 6)
# 访问属性 -- 句点表示法
print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + ' years old.')
# 调用方法 -- 句点表示法
my_dog.sit()
my_dog.roll_over()


# 可以为同一个类创建多个实例

# Demos
# 1.Restaurant
class Restaurant:
    def __init__(self, name, ttype):
        self.restaurant_name = name
        self.restaurant_type = ttype

    def describe_restaurant(self):
        print('The name is ' + self.restaurant_name)
        print('Its type is ' + self.restaurant_type)

    def open_restaurant(self):
        print('The restaurant is openning.')


restaurant = Restaurant('KFC', 'junk food')
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 2.User
class User:
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname

    def describe(self):
        print('The profile of user:')
        print('first name - ' + self.first_name)
        print('last name - ' + self.last_name)

    def greet_user(self):
        print('Welcome, ' + self.last_name + ' ' + self.first_name)


user = User('Cai', 'Shanyu')
user.describe()
user.greet_user()
