# 剔除人名中的空白
fname = "\t Joe \t\n "
lname = " Chen\t"
name = fname + lname
print(name)

print("--------------------")

fname = fname.strip()
lname = lname.rstrip()
lname = lname.lstrip()
name = fname + " " + lname
print(name)
