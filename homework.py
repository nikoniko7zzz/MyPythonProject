# 9月12日　課題　--------------------------------------

# 10から0までカウントダウンする////////////////
# count = 10
# while count >= 0:
#     print(count)
#     count = count - 1

# 10から5までカウントダウンする////////////////
# count = 10
# while count > 0:
#     print(count)
#     if count == 5:
#         break
#     count = count - 1

# リストの中身を順に表示する////////////////
# num_list = [10, 20, 30]

# for n in num_list:
#     print(n)

# 文字列'Hello'を10回出力する////////////////
# for i in range(10):
#     print('Hello')

# 整数5から整数10までを順に出力する////////////////
# for i in range(5, 11):
#     print(i)
# // 5
# // 6
# // 7
# // 8
# // 9
# // 10

# 内包表記を使って一行で書く////////////////
# num_list = []
# for i in range(10):
#     num_list.append(i)
# print(num_list)

# num_list = [i for i in range(10)]
# print(num_list)
# // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 引数num1, num2を受け取り、num1とnum2を足した結果を返す////////////////
# 関数名はaddとする
# def add(num1, num2):
#     return num1 + num2


# print(add(1, 2))
# // 3

# 引数numを受け取り、numを2乗した結果を返す////////////////
# def square(num):
#     return num ** 2


# print(square(5))
# // 25

# キーワード引数を使い、num2には5を、num1には3を、この順番で渡す////////////////
# def add(num1, num2):
#     return num1 + num2


# print(add(num2=5, num1=3))

# def add(num1, num2=10):
#     return num1 + num2

#  square = lambda num: num ** 2

# print(add(3))
# // 13


# def add(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     return sum


# print(add(1, 2, 3))
# // 6

# 一行にしなさい
# def square(num):
#     return num ** 2


# print(square(9))

def square(n): return n ** 2

# def square(n): return n**2

# 以下は「ユーザに数値を入力させ、その数値を加算していく」プログラムです。////////////////
# もし数値以外の値が入力されたときは、例外処理の構文を用いてプログラムを
# 正常に終了する必要があります。
# なお、受け取る例外の種類は指定せず、すべての例外を一か所で受け取ります。
# 空欄を埋め、プログラムを完成させてください。
# sum = 0
# while True:
#     try:
#         s = input('Please input number:')
#         num = int(s)
#         prev = sum
#         sum = sum + num
#         print(str(prev) + ' + ' + str(num) + ' => ' + str(sum))
#     except:
#         print('Not a number is inputted. Program exit.')
#         break

# import sampleB

# print(sampleB.add(10, 20))
