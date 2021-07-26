# JSON可以将简单的python数据结构存储到文件中 并且通用于其他编程语言
import json

# 存储数据 -- dump() 第一个参数为欲存储的数据 第二个参数为待存入的文件对象
numbers = [1, 2, 3, 4, 6]
filename = 'numbers_0018.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

# 读取数据 -- load() 参数为读取的文件对象
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

filename = 'username_0018.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name?\n")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We will remember you!")
else:
    print("Welcome back, " + username + "!")
