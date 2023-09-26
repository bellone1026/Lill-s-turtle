import matplotlib.pyplot as plt
import turtle as tt
b_plma='plus'

# 이차함수 계수 설정
a,b,c=map(float,input().split())
a,b,c=1,b/a,c/a
print(a,b,c)
if a<0:
  a=-a
  b=-b
  c=-c
if b<0:
  b_plma='minus'
  b=-b
d=100

#터틀 화면 안에 그림이 안 그려질 경우
#d=100/abs(max(a,b,c))

# 계수에 대한 선분 설정 + 최종 지점 위치 저장
tt.hideturtle()
tt.goto(0,0)
tt.forward(a*d)
tt.left(90)
tt.forward(b*d)
tt.left(90)
tt.forward(c*d)
tt.penup()
finalx=tt.xcor()
finaly=tt.ycor()

# 움직이는 선분 설정
ty=0
whether=False
t_whether=False
tt.speed(0)
if c>0:
  while whether==False:
    tt.goto(0,0)
    tt.pendown()
    tt.goto(a*d,ty)
    if ty>b*d:
      whether=True
    if ty*(b*d-ty)!=abs(c*d*a*d):
      ty+=1
    else:
      whether=True
      t_whether=True
      tt.goto(finalx,finaly)
  if t_whether==False:
    print('imaginary')
  else:
    if b_plma=='plus':
      print(round(-ty / (a * d), 2))
    else:
      print(-round(-ty / (a * d), 2))
  ty=0
  while whether==True:
    tt.goto(finalx, finaly)
    tt.pendown()
    tt.goto(a * d, finaly-ty)
    if ty > b * d:
      whether = False
    if ty * (b * d - ty) != abs(c * d * a * d):
      ty += 1
    else:
      whether = False
      t_whether = True
      tt.goto(0, 0)
      break
  if t_whether==False:
    print('imaginary')
  else:
    if b_plma == 'plus':
      print(round(-(finaly - ty) / (a * d), 2))
    else:
      print(-round(-(finaly - ty) / (a * d), 2))
elif c<0:
  while whether==False:
    tt.goto(0, 0)
    tt.pendown()
    tt.goto(a * d, -ty)
    if ty * (b * d + ty) != abs(c * d * a * d):
      ty += 1
    else:
      whether = True
      if b_plma == 'plus':
        print(round(ty / (a * d), 2))
      else:
        print(-round(ty / (a * d), 2))
      tt.goto(finalx,finaly)
      tt.pendown()
  ty=0
  while whether==True:
    tt.penup()
    tt.goto(0, 0)
    tt.pendown()
    tt.goto(a * d, b*d+ty)
    if ty * (b * d + ty) != abs(c * d * a * d):
      ty += 1
    else:
      whether = False
      if b_plma=='plus':
        print(round(-(b*d+ty) / (a * d),2))
      else:
        print(-round(-(b*d+ty)/(a*d),2))
      tt.goto(finalx, finaly)

# 좌표평면 위에 나타내기
X=range(-10,10)
Y=[a * i ** 2+ b* i +c for i in X]
plt.plot(X,[0]*20)
plt.plot(X,Y)
plt.show()