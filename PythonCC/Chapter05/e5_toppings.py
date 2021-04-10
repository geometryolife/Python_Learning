print("----------测试多个条件----------")
#  if-elif-else结构很强大，效率高，但只能测试一个特定条件
#  有时候必须检查多个条件，在每个条件为True时都采取相应措施
#  这时应使用一系列不包含elif和else的代码块的简单if语句
requested_toppings = ['mushroom', 'extra cheese']

if 'mushroom' in requested_toppings:
    print("Adding mushroom.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#  程序均会执行这三个独立的测试

print("\n----------逻辑错误测试----------")
#  如果转而使用if-elif-else结构，代码将不能正确地运行，因为有一个
#  测试通过后，就会跳过余下的测试
requested_toppings = ['mushroom', 'extra cheese']

if 'mushroom' in requested_toppings:
    print("Adding mushroom.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
