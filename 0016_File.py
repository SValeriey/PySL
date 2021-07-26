# 打开并读取文件
with open('pi_0016.txt') as file_object:  # open()接受参数：文件名 将对象存储在后续变量中
    contents = file_object.read()  # read()方法读取文件内容 / 到达文件末尾时返回一个空字符串
    print(contents)
print()

# with 关键字在不需要访问文件后将其关闭 不需要调用close()
# with读取的内容只能在 with 代码块内使用
# 可以使用文件路径 win系统用 \ （反斜杠）

# 逐行读取文件内容 使用for循环
filename = 'pi_0016.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())  # rstrip() 方法消除空行
print()
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# 使用文件内容
pi_string = ''
for line in lines:
    pi_string += line.rstrip() + ' '
print(pi_string)
print(len(pi_string))  # len()返回字符串长度

# 写入文件
filename = 'empty_0016.txt'
# 1. w 写入模式
with open(filename, 'w') as file_object:  # 指定'w'写入文件，文件已存在会先清空文件
    file_object.write("Hello world!\nHello Python!\n")  # 需要使用换行符
# 2. a 附加模式 不覆盖原本内容
with open(filename, 'a') as file_object:
    file_object.write("Hello c plus plus!")

# Demos:
# 1. 用while循环询问用户，将结果写入文件
a = 'a'
filename = 'reason_0016.txt'
while a != 'q':
    reason = input("Why do you like programming?\n")
    with open(filename, 'a') as file_object:
        file_object.write(str(reason) + '\n')
    a = input("Enter q to quit, or continue.")

