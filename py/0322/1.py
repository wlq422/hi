# 2023-03-22
# 한줄 주석 ->#
#여러줄 주석은 ''' 으로 사용
''' 여러줄 
주석
 입니다'''

#출력 명령 print()
#String ",' 사용
print("오늘은 파이썬 수업입니다.")
print('hello !! ')

#타입 확인
print(type(2)) 

#숫자
print(2)
print(5.5)

#
print("Hello" + "Python")

# print("Hello" + 33) #에러난다 
print("Hello" ,33)  #이렇게 표현해야함

print("213 호" * 3)
print("heelo", "hi", "213")
print("heelo", "heelo", 213, " ", 1111)

#eval 모든 실행가능한 파이썬 문장의 문자열을 실행
print(eval('3+8'))

var = '3+8'
print(eval(var))
print(var)