print("----------禁止函数修改列表----------")


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #  模拟根据设计制作3D打印模型的过程
        print("Printing models: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


#  主程序
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#  通过切片操作，把列表的副本传递给函数，从而保护了原列表不被修改
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

#  未修改原列表
print(unprinted_designs)


#  ----------禁止函数修改列表----------
#  Printing models: dodecahedron
#  Printing models: robot pendant
#  Printing models: iphone case

#  The following models have been printed:
#  dodecahedron
#  robot pendant
#  iphone case
#  ['iphone case', 'robot pendant', 'dodecahedron']
