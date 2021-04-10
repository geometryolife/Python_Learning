print("----------关键字实参----------")
#  关键字实参是传递给函数的名称-值对。你直接在实参中将名和值
#  关联起来了，因此向函数传递实参时不会混淆。
#  关键字实参无需考虑函数调用中的实参顺序，还清楚地指出了函数
#  调用中各个值的用途。


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

#  注意: 使用关键字实参时，务必准确地指定函数定义中的形参名
