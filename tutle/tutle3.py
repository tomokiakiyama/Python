from turtle import*

#角度のリストを登録する
curve = [10, 160, 10, 20]
speed("fastest")

for i in range(40):              #40回繰り返す
    forward(100)                 #10進む
    degree = curve[i%len(curve)] 
    right(degree)               #リストに従って進む
