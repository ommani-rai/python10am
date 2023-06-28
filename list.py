# list
# start index: 0
# negative indexing: start with -1
# list1 = ['ram', 'shyam', 1,3, False, True]
# lis = [1,2,3,4,5]
# tup = (6,7,8,9,0)
# print(type(list1))
# print("hello \n world")
# print(list1[:4])
# print(list1[3:])

# list1[1:3] = ["hari", 'abc', 'xyz', 'asfasdf']
# list1.append("curry")
# list1.insert(0, "apple")
# list1.extend(lis)
# list1.extend(tup)
# print(list1)



# list1 = ['ram', 'shyam', 1,3, False, True]
# del list1[0]
# list1.pop(5)
# list1.remove("shyam")
# print(list1)


# sort
numbers = [2,33,56,6878,89,8]
# num = numbers.copy()
num = list(numbers)

# print(num)
fruits = ['apple', 'orange', 'mango', 'kiwi', 'papaya', 'avocado']
fruits.sort(reverse=True)
# fruits.sort()
# print(fruits)
numbers.sort()
# print(numbers)
combinedList = fruits + numbers
print(combinedList)
