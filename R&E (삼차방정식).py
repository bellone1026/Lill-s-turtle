import turtle as tt
import matplotlib as mm
import math

#좌표 설정
a=list(map(float,input().split())) # [삼차계수, 이차계수, 일차계수, 상수항] 으로 계수를 입력받기
a[3],a[2],a[1]=a[3]/a[0],a[2]/a[0],a[1]/a[0] # 삼차계수의 계수를 1로 고정하기 위해 다른 계수들을 조정
a[0]=1.0
interver_=0 #전진간격의 소수점 설정
a_=[0,0,0,0]
for i in range(4):
    a_[i]=abs(a[i])
    k=str(a_[i])
    if interver_<len(k[str(a_[i]).index('.')])-1:
        interver_=len(k[str(a_[i]).index('.')])-1
for j in range(4):
    a_[j]=int(a_[j]*(10**interver_))
interver=math.gcd(*a_)/(10**interver_) #최종 전진가격 설정
print(a,a_) #소수점 최소공배수를 곱해진 값 확인
#tt.hideturtle() #깜빡거리는 화살표 제거
dot1=(a[0]*30,0) #설정된 계수 만큼 선분 설정
dot2=(a[0]*30,a[1]*30)
dot3=((a[0]-a[2])*30,a[1]*30)
dot4=((a[0]-a[2])*30,(a[1]-a[3])*30)
tt.goto(dot1)
tt.goto(dot2)
tt.goto(dot3)
tt.goto(dot4)
t=-300 #측정 시작 위치
a,b,c=a[1],a[2],a[3] #후에 쓰일 공식을 편리하게 사용하기 위한 변수 변경

#움직이는 선분 표현하기
tt.speed(0)
tt.pendown()
while t<300:
    tt.penup()
    t+=interver
    dot_p = (t, (a + c)*30)
    tt.goto(dot_p)
    tt.stamp()
    tt.goto(dot4)
    A=(1-t)
    if ((A-b)**2)*(A+b)+4*(A-b)*a*c==c*c*-8:
        dot_q=(30,60*c/(b+t-1))
        tt.pendown()
        tt.goto((t+dot4[0])/2,dot3[1])
        tt.stamp()
        tt.goto(dot_q)
        tt.stamp()
        tt.home()
        tt.penup()
        tt.goto(dot4)
        print(-2*c/(b+t-1))
tt.mainloop()