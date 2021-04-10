print("----------位置实参----------")
#  调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的
#  一个形参。最简单的关联方式是基于实参的顺序。
#  此关联方式为: 位置实参


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')

#  根据需要，调用函数任意次
describe_pet('dog', 'willie')

print("\n----------位置实参的顺序很重要----------")
describe_pet('harry', 'hamster')
