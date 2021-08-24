import numpy as np

print("----------保存和加载数据----------")
print("\n----------保存矩阵到 txt 文件----------")

np.random.seed(1)
arr = np.random.randn(3, 4)

# 保存数据到 .txt 文件
np.savetxt('data/test1.txt', arr, delimiter=',', fmt='%0.8f',
           header='rand1,rand2,rand3,rand4')


"""
>>> Execution Result:
# rand1,rand2,rand3,rand4
1.62434536,-0.61175641,-0.52817175,-1.07296862
0.86540763,-2.30153870,1.74481176,-0.76120690
0.31903910,-0.24937038,1.46210794,-2.06014071
"""
