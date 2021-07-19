# Create a list.
friends = ['yyj', 'wd', 'pp', 'hhj', 'jm', 'am', 2012, 2015]
# Display the list.
print(friends)
print(friends[0].title())  # start from 0
print(friends[-1], friends[-2])  # end with -1

# Edit the list.
# 1. Change the element.
friends[1] = 'WD'
print(friends)
# 2. Add the elements.
friends.append(2021)  # append(element) -- Add in the tail of list.
print(friends)
friends.insert(1, 'and')  # insert(n,element) -- Add in the n+1 th
print(friends)
# 3. Delete elements
del friends[1]  # del list[n] -- Delete the n+1 th element.
print(friends)
friends.pop()  # pop() -- Delete the last element.
friends.pop(-2)  # pop(n) -- Delete the n+1 th element.
print(friends)
friends.remove('yyj')  # remove(element)
print(friends)

# Sort the list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # sort() -- Sort permanent
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))  # sorted(list) -- Sort temporary

# Reverse the list
friends.reverse()
print(friends)

# Get the length of list
print(len(friends))
