import random
list = ['a', 'b', 'c', 'd', 'e', 'f']
list1 = random.shuffle(list)
print(list)

for i in range(len(list)):
    print("{} - {}".format(list[i], list1[i]))
