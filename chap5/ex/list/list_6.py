#listを用いたクイズ

colors = ["purple", "orange", "green"]

guess = input("何色が含まれているでしょう?")

if guess in colors:
    print("正解")
else:
    print("不正解")
