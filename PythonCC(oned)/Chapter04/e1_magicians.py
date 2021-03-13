#  遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#  编写for循环时，用于存储列表中每个值的临时变量，可指定名称，有意义。
#  for cat in cats:
#  for doc in dogs:
#  for item in list_of_items:

print("--------------------")

#  在for循环中执行更多的操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

#  for循环结束后执行一些操作
print("Thank you, everyone. That was a great magic show!")

print("--------------------")
#  忘记缩进额外的代码
#  逻辑错误：虽然代码合法，但结果不符合预期
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("--------------------")

#  不必要的缩进
#  IndentationError: unexpected indent

#  循环后不必要的缩进
#  可能导致Python报语法错误，但在大多数情况下，这只会导致逻辑错误

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you, everyone. That was a great magic show!")
