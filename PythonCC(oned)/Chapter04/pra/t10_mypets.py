#  使用切片，打印前面、中间、后面三个元素
mypets = ['cat', 'dog', 'fish', 'tiger', 'bird', 'dragon']

print("The first three items in the list are:")
print(mypets[:3])

print("\nThree items from the middle of the list are:")
middle = int(len(mypets) / 3)
print(mypets[middle:middle + 3])

print("\nThe last three items in the list are:")
print(mypets[-3:])
