demo = 100


def demo1():
    print(demo)


print("==================================================")


def demo2():
    demo = 300
    print(demo)


demo1()
demo2()
# 从这里可以看出来，变量的访问具有就近原则
# 同时，全局变量的访问会被就近修改
print(demo)  # 默认还是访问全局变量，因为代码是按步骤执行的
print("==================================================")


def demo3():
    global demo  # 手动指定访问的是全局变量
    demo = 354564  # 这里就产生了修改过程
    print(demo)


demo3()
