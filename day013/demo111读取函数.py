print("==================================================")
text_io = open("demo109.txt", "r")
# print(text_io.read())
# junw111
# 11111
# 22222
# 这里不会逐行读取，一次性读取所有的文本内容
print("==================================================")

print(text_io.read(10))
# junw111
# 11
# 在上面读取了一次内容，再次读取，就不会按照10个字符去读取
# 同时，因为文本中是有换行符的，所以真实读取的10个字符，和展示出来的不一样
text_io.close()
