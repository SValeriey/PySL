friends = ['yyj', 'wd', 'pp', 'hhj', 'jm', 'am', 2012, 2015]

# Traverse the list
for friend in friends:
    print(friend)
    print("good\n")
print("Done.")

# Create the digit list.
for value in range(1, 5):  # range(s,e) -- s,s+1,s+2,...,e-1
    print(value)
even = list(range(2, 11, 2))  # range(s,e,s) -- step
print(even)

square = []
for value in even:
    square.append(value ** 2)
print(square)

# Some operate for digit -- min, max, sum
digit = list(range(1, 11))
print(min(digit), max(digit), sum(digit))

# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# Demos
# 1. 数到20
for value in range(1, 21):
    print(value, end=' ')
print()
# 2. 计算1-1000总和，验证列表是否1-1000 调用sum()
digit = range(1, 1001)
print(min(digit), max(digit), sum(digit))
# 3. 创建3-30内可以被3整除的列表并打印
digit = [value for value in range(3, 31) if value % 3 == 0]
print(digit, end=' ')
print()

# Cut the list.
my_bro = friends[0:6]  # list[s,e] -- elements in list from s to e-1
print(my_bro)
# if you have not given s, the start from 0, ignored e then to the end

# Duplicate the list
food = ['pizza', 'falafel', 'carrot cake']
favourite_food = food[:]  # you should use slice to duplicate list!
# favourite_food = food  # ERROR
print(favourite_food)
