demo1 = {10, 11, 12}
print(type(demo1))
demo1.add(100)  # 单个数据可以这样追加的，
print(demo1)  # {100, 10, 11, 12}
# demo1.add([11, 12, 13])  # 追加序列会报错
print("==================================================")
demo1.update([10, 20, 30])
print(demo1)  # {100, 10, 11, 12, 20, 30}
# 序列会作为单个元素，直接追加进去

# 同时，因为集合是没有顺序的数据类型
# 追加的数据也会在集合中失去具体的顺序
