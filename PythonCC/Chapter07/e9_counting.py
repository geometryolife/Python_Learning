print("----------在循环中使用continue----------")
#  打印1~10中的奇数
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
