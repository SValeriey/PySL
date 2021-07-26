class Car:
    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 指定默认值

    def get_descriptive_name(self):
        """简洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def update_odometer(self, mileage):
        """修改里程，禁止回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        """打印汽车行驶里程"""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 修改属性的值
# 1. 通过实例修改
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# 2. 通过方法修改
my_new_car.update_odometer(46)
my_new_car.read_odometer()
