num1 = 2
num2 = 0.5
s = num1 * num2
print(s)  # 最终结果为1.0，只要有浮点数参与运算，最后结果一定是浮点数
print("==================================================")

print(4 / 2)  # 除法比较特殊，结果为2.0
# 只要涉及到除法，最后一定是浮点数结果
print("==================================================")

print(3 // 2)  # 1，双斜杠//表示获取整除数的结果
print(4 // 2)  # 2
print(5 // 2)  # 2

print("==================================================")
print(2 ** 2)  # 4，**表示次方
print((1 + 3) * 2)  # 8
print((1 + 3) ** 2)  # 16
print("==================================================")
print(2 * 3 ** 2)  # 18，先算次方，再算相乘
