#bool

print(type(True), type(False))
a = "hello"
print(bool("hello"), bool("hi"), bool(3), bool(1.2), bool(-2)) #모두 True
print(bool(""),bool(0)) #빈문자랑 0이 false ** 공백은 true
print(int(True), int(False),str(True)) #출력 : 1 0 True
