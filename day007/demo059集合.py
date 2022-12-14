demo1 = {}
print(type(demo1))  # <class 'dict'>
print("==================================================")
demo2 = {10, 20}
print(type(demo2))  # <class 'set'>
# 在python中，直接设置一个大括号，只会得到一个字典类型的数据
# 但是集合和字典,在格式上是几乎一样的——都是使用大括号来构建
print("==================================================")
# 集合没有顺序，自然也就不支持按顺序操作——简单来说，没有下标
# demo2[0]这种操作是无效的，也是没有用的
demo3 = {10, 11, 12, 11, 10}
print(demo3)  # {10, 11, 12}
# 集合自带了去重功能
print("==================================================")
demo4 = set()  # 创建空集合只能使用set小括号
print(type(demo4))  # <class 'set'>
