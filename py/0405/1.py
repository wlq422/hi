#0405
#문자열

str = "파이썬수업 씨수업 파이썬수업 파이썬수업"
str2 = "파이썬수업 씨수업 파이썬수업 파이썬수업"

#format
#3+4=7
print(3,"+",4, " =", 7)
f1= "{} + {} = {}".format(3,4,3+4)
f2= "{0} + {1} = {2},{2},{2},".format(3,4,3+4) #숫자명시
f3 = "{0:d} + {1:f} = {2:f}".format(3,4.0,3+4.0)
f4 = "{0:10d} + {1:10f} = {2:f}".format(3,4.0,3+4.0)#f앞에는 숫자만큼 공간을 주라는 뜻

print(f4)


#join
#"**".join(str)

'''
#sprit
print(str.sprit())

print(str2.split(","))
print(str2.split("업"))

#replace
print(str.replace("파이썬","자바",3))

#count
print(str.count("파이썬"))

#find , index
print("find : " , str.find("파이썬") , "index : " , str.index("씨"))
print(str.find("에이아이")) #없을 때 return -1
print(str.index("에이아이")) # 없을 때 에러 냄
'''