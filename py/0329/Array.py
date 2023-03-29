a = "python"
print(a[0], " ", a[1], " ", "...", a[5])
print("python"[0], "...", "python"[1], "...", "python"[5])
print("동양미래대학교"[0])
print(len(a))

##슬라이싱 ->양수로 슬라이싱 하는건시험 출제
# 원래는 a[0:3:1] 인데 :1을 생략
#-> 2칸씩 넘어가고 싶으면 a[0:3:2]로 적어주면 됌
# a[ : ] 처음부터 끝까지 보여줘라
# a[ : 3] 처음부터 2까지 보여줘라
# a [0: len(a)]  처음부터 leng -1 까지 보여줘라
# 음수로 보는 법은 시험에 안낼게요

school = "동양미래대"
#1개씩
print("school[:] : " , school[ : ]) #동양미래대학교
print("school[0:3] : " , school[0:3]) #동양미
print("school[1:4] : " , school[1:4]) #양미래
print("school[2:4] : " , school[2:4]) #미래
print("school[1:] : " , school[1: ]) #양미래대
#건너뛰기
school1 = "동양미래대학교-컴퓨터소프트에어공학과"
print("school1[::] : " , school1[::]) #동양미래대학교-컴퓨터소프트에어공학과
print("school1[0:len(school1):2] : " , school1[0:len(school1):2]) #동미대교컴..
print("school1[8:len(school1):2] : " , school1[8:len(school1):2]) #컴터프웨공과
print("school1[8:len(school1)] : " , school1[8:len(school1)]) #컴퓨터소프트웨어공학과
print("school1[:15:4] : " , school1[:15:4] ) 
#동양미래대학교-컴퓨터소프트에어 4칸씩 뛰기.동대컴프

