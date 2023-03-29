str_a = "하하하"
#str_b = "호호호"

print(type(str_a))
str_a.replace ("하","호")
print(str_a.replace ("하","호"))
str_b =  str_a.replace("하","호")
print("str_a: ", str_a)
print("str_b: ", str_b)

str_c = "안녕하세요. 파이썬 수업입니다. 파이썬. 파이선. 파이선. 파이썬. 파이선"
print(str_c.replace("파이썬", "자바", 5))

#Q
#6자리 실수를 입력 받는다. 222.788
#출력 : 실수의 각 자리의 합을 출력한다. 2+2+2+7+8+8 =>??
# input(), int(), str.replace()

a = input("6자리 실수 입력 : ") #212.222
num = a.replace('.', '') 
#.이 있으면 공백으로 바꿔달라고 하는 것 212222로변환
# 212222->str로 바꿔서 배열로 읽어 내면 됌
sum = 0
sum += int(num[0])
sum += int(num[1])
sum += int(num[2])
sum += int(num[3])
sum += int(num[4])
sum += int(num[5])
print("입력값 : " , a)
print("실수의 각 자리 합은 : " , sum)