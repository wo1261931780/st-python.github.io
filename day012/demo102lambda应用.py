demo_f1 = lambda demo1, demo2: demo1 if demo1 > demo2 else demo2
print(demo_f1(11, 22))
# 三元运算符做表达式


print("==================================================")
common_dic = [{"name": "demo1", "age": 11}, {"name": "demo3", "age": 33}, {"name": "demo2", "age": 22}]

common_dic.sort(key=lambda x: x["age"])
print(common_dic)
print("==================================================")
common_dic.sort(key=lambda x: x["name"], reverse=True)
# reverse表示降序排列
print(common_dic)
# 解释一下，首先是指定排序的东西，这里指定的就是key
# 然后，设置key的排序原则，就使用lambda表达式完成
# 最后选择是否需要降序排列
