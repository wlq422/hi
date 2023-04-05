'''
#for , while
#반복문
#in range

for i in 10,25,32,4352,565,624 :
    print ("i : ", i)

#range
for i in range(0,20,1) :
    print ("i : " , i)
for i in range(20) :
    print ("i : " , i)



#1부터 10까지 합을 구하시오
#2가지 방법으로 , range 도 쓰고 그냥 명시도 하고

sum = 0
for i in 1,2,3,4,5,6,7,8,9,10 :
    sum = sum + i
    print(i,"번째 loop입니다. sum은 " ,sum," 입니다")
    #print ("하하하")

print("range를 사용하였음")
sum = 0    
for i in range(1,11,1) :
    sum += i
    #sum = sum + i
    print(i,"번째 loop입니다. sum은 " ,sum," 입니다")
    
    '''