# About String
name = "ada lovelace"
print(name.title())  # Capitalize(大写) the first letter.
print(name.upper())  # Capitalize all letters.
print(name.upper().lower())  # Lowercase all letters.

# Connect the string
first_name = "Cai"
last_name = "Shanyu"
full_name = first_name + " " + last_name
print("my name is", full_name)

# Blank Space
print("Python")
print("\tPython")  # \t--Tab(制表符)
print("Hello\nPython")  # \n--next_line(换行)
# Delete the blank of the string
language = "         Python    "
print(language)
language = language.lstrip().rstrip()  # left and right
print(language)

# Demos
# 1.个性化消息: 将用户的姓名存到一个变量中，并向该用户显示一条消息
name = input("What is your name?\n\t")
print("You are really BUDE,", name)
# 2.调整名字大小写: 将人名存储到一个变量中并大小写首字母大写显示
print(name.lower(),name.upper(),name.title())
