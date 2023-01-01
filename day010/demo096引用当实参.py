demo1 = 111
print(demo1)
print(id(demo1))
print("==================================================")


def show_me(num1):
    print(num1)
    print(id(num1))


show_me(demo1)  # 2308364832432
# 引用地址是一样的
print("==================================================")
demo2 = id(demo1)
show_me(demo2)
# 不可变类型的数据，不能直接作为参数传递过去
print("==================================================")
demo3 = [11, 22, 33]
show_me(demo3)
