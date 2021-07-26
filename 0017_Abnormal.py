# print(5/0)  # 返回一个traceback

# ZeroDivisionError
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 使用异常避免崩溃
print("Give me two numbers, and I will divide them.")
print("Enter q to quit.")
while True:
    first_number = input("\nFirst Number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0.")
    else:
        print(f'\nConsequence = {answer}')

# FileNotFoundError
# 文本分析
filename = 'Swat_the_Fly_0017.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("The file doesn't exist.")
else:
    word = contents.split()  # split()方法以空格为分隔符将字符串拆分为多个部分，并将其存储在列表中
    num_word = len(word)
    print(f"The file has about {num_word} words.")
