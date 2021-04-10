print("----------默认值----------")
#  编写函数时，可以给每个形参指定默认值。
#  在调用函数中给形参提供了实参时，Python将使用指定的实参值；
#  否则，将使用形参的默认值。
#  给形参指定默认值后，可在函数调用中省略相应的实参。
#  使用默认值可简化函数调用，还可清楚地指出函数的典型用法。


#  def describe_pet(animal_type='dog', pet_name):
#  SyntaxError: non-default argument follows default argument
#  非默认参数不能跟随默认参数，否则会产生语法错误

#  由于给animal_type指定了默认值，无需通过实参来指定动物类型，因此在
#  函数调用中只包含一个实参--宠物的名字，这个实参将关联到函数定义中的
#  第一个形参。这就是需要将pet_name放在参数列表开头的原因所在。


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())


describe_pet(pet_name='willie')
#  使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认
#  值的形参。这让Python依然能够正确地解读位置实参。
#  使用这个函数的最简单方式
describe_pet('willie')

#  如果要描述的动物不是小狗，可使用类似于下面的函数调用
describe_pet(pet_name='harry', animal_type='hamster')

print("\n----------等效的函数调用----------")
#  可混合使用位置实参、关键字实参和默认值

#  一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')

#  一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#  注意: 使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行。

print("\n----------避免实参错误----------")
#  describe_pet()
