print("----------在函数中修改列表----------")
#  不使用函数的情况
#  首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#  模拟打印每个设计，直到没有未打印的设计为止
#  打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()

    #  模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#  显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_models in completed_models:
    print(completed_models)

print("\n----------使用函数的情况----------")


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #  模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


#  主程序
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


#  ----------在函数中修改列表----------
#  Printing model: dodecahedron
#  Printing model: robot pendant
#  Printing model: iphone case

#  The following models have been printed:
#  dodecahedron
#  robot pendant
#  iphone case

#  ----------使用函数的情况----------
#  Printing model: dodecahedron
#  Printing model: robot pendant
#  Printing model: iphone case

#  The following models have been printed:
#  dodecahedron
#  robot pendant
#  iphone case
