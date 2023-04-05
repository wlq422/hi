#break continue
#단어 입력을 무한 루프로 받는다
# 그 글자를 3번 써줌
# "exit" -> 루프를 끝내고 종료
# "apple" -> 3번 안쓰고 그냥 다시 단어 입력을 받음

'''
while True : 
    단어를 입력 받는다
    if exit인경우  :
        break
    elif apple인 경우:
        continue
    else :
        for :
            3번 찍는다
'''

while True : 
    word = input("단어를 입력하세요")
    if word == "exit":
        print("넌 exit 을 입력했다.break를 만난다.")
        break
        print("break 뒤의 문장")
    elif word == "apple" :
        print("넌 apple을 입력했따. countinue 를 만난다")
        continue
        print("countinue뒤의문장")
    else :
        for i in range(3) : 
            print(word, end =' ')
        print("해당 단어 끝")

        
    