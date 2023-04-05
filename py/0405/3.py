#조건문

'''
문법
if문
if 조건 1 :
    실행문 1

if else문
if 조건1 :
    실행문1
else :
    실행문2 #거짓

if elif else 문
if 조건1 :#참
    실행문1
elif 조건2 :
    실행문2
    ...
elif 조건10 :
    실행문210 
else :
    실행문2 #거짓
'''

'''
#오전/오후
h = 9
if h < 12 :
    #h가 12보다 작을 때 
    print("오전",h,"가 12보다 작다")
else :
    #실행문2
    #가 12보다 크다.
    print("오후",h,"가 12보다 크다")
'''
'''
#오전/오후/저녁
h = 9
if h < 12 :
    #h가 12보다 작을 때 
    print("오전",h,"가 12보다 작다")
elif h<18 :
    #12< h <18
    print("오후",h,"가 12보다 크고 18보다 작다")
else :
    #실행문2
    #18<h
    #가 18보다 크다.
    print("저녁",h,"가 18보다 크다")
'''
#조건문 ex
lunch = input ("밥 먹을래?")
if lunch == "yes" :
    print("밥을 먹고 싶군요.")
    cafeteria = input("학식?")
    if cafeteria == "yes" :
        print("8호관 1층으로 ")
    else :
        print("학식을 싫어하는군요.")
        subway = input("subway? ")
        if subway == "yes" :
            print("8호관 1층으로 고고")
        else : 
            print("subway를 싫어하시는군요.")
else:
    print("밥 먹기 싫군요")