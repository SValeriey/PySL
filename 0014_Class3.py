# 继承
# 一个类继承另一个类时，子类获得父类的所有属性和方法，子类可以定义自己的属性和方法
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """模拟电瓶车电瓶"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):  # 定义子类时，括号内指定父类的名称
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)  # super()将子类和父类关联
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


# 子类重写父类方法 -- 在子类中重新定义同名函数

# Demos:
# 1.冰淇淋小店
class Restaurant:
    def __init__(self, name, ttype):
        self.restaurant_name = name
        self.restaurant_type = ttype

    def describe_restaurant(self):
        print('The name is ' + self.restaurant_name)
        print('Its type is ' + self.restaurant_type)

    @staticmethod
    def open_restaurant():
        print('The restaurant is opening.')


class IceCreamStand(Restaurant):
    def __init__(self, name, type, flavors):
        super().__init__(name, type)
        flavors = ['haciendas', 'green bean']
