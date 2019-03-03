try:
    a = input("数値入力")
    b = input("数値入力")
    a = int(a)
    b = int(b)
    print(a/b)
except(ZeroDivisionError, ValueError):
    print("0以外の数値を入力してください")


