from turtle import*

degree = 1             #角度初期
distance = 50          #距離初期

for i in range(40):    #40回繰り返す
    forward(distance)  #distance文進む
    right(degree)      #degree文右に曲がる
    degree += 2        #角度を2足す
    distance -= 1      #距離から1引く
