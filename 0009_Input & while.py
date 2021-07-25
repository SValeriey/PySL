# input() 暂停程序，等待用户输入文本，存入变量以便使用
# message = input("Tell me something and I will repeat it back to you.\n")
# print(message)

# while
current_number = 1
while current_number <= 5:
    print(current_number, end=' ')
    current_number = current_number + 1
print()

# 可以使用while让用户决定什么时候退出程序
# break退出整个循环
# continue退出当前循环，继续下一个循环

unconfirmed_user = ['alice', 'brian', 'candace']
confirmed_user = []
while unconfirmed_user:
    confirmed_user.append(unconfirmed_user.pop())
    print(confirmed_user)

pets = ['dog', 'fish', 'dog', 'cat', 'rabbit', 'dog']
print(pets)
while 'dog' in pets:
    pets.remove('dog')
print(pets)
