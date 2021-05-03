"""
根据e4_pi_string.py的demo，设计一个程序来计算某一年中有多少
天包含在一百万位的圆周率中。假设每个月都是30天，一年共360天。
"""

filename = '../data/pi_million_digits.txt'

with open(filename) as f_obj:
    lines = f_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# print(pi_string[:52] + "...")

# 中国农历每个月都是30天。

md_lists = []
for mm in range(1, 13):
    if mm < 10:
        m_str = "0" + str(mm)
        # print(m_str)
        for dd in range(1, 31):
            if dd < 10:
                md_str = m_str + "0" + str(dd)
                md_lists.append(md_str)
                # print(md_str)
            else:
                # pass
                md_str = m_str + str(dd)
                # print(md_str)
                md_lists.append(md_str)
    else:
        pass
        m_str = str(mm)
        for dd in range(1, 31):
            if dd < 10:
                md_str = m_str + "0" + str(dd)
                # print(md_str)
                md_lists.append(md_str)
            else:
                md_str = m_str + str(dd)
                md_lists.append(md_str)
                # print(md_str)

# 测试97年
mdy_lists = []
for md_list in md_lists:
    mdy_list = md_list + "97"
    mdy_lists.append(mdy_list)

# 计算97年中有多少天在一百万圆周率中
times = 0
for mdy_list in mdy_lists:
    if mdy_list in pi_string:
        times += 1
print("在1997年中有" + str(times) + "天包含在一百万位的圆周率中。")
