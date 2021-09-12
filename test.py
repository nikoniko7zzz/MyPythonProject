# countries = {'jp': 'Japan', 'us': 'America', 'fr': 'France'}
# for c in countries:
#     print(c)
# # jp
# # us
# # fr

# countries = {'jp': 'Japan', 'us': 'America', 'fr': 'France'}
# for k, v in countries.items():
#     print(k, v)
# # jp Japan
# # us America
# # fr France

# for k, v in countries.items():
#     print(v)

# for k in countries.keys():
#     print(k)

# for i in range(10):
#     print(i)

# for i in range(2, 8):
#     print(i)

# for i in range(3):
#     print('hello')

# x = [10, 30, 20, 40]
# y = ['dog', 'cat', 'bird']
# d = {}
# for a, b in zip(x, y):
#     print(a, b)
#     d[a] = b
# print(d)
# # 10 dog
# # 30 cat
# # 20 bird
# # {10: 'dog', 30: 'cat', 20: 'bird'}
#
# l = []
# for i in range(1, 11):
#     l.append(i ** 2)
# print(l)
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# l = [i ** 2 for i in range(1, 11)]
# print(l)
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# pets = ['dog', 'cat', 'bird']
# list = {p: len(p) for p in pets}
# print(list)
# # {'dog': 3, 'cat': 3, 'bird': 4}

# l = [1, 2, 3, 4, 4, 5, 6, 7, 7]
# p = {i for i in l}
# print(p)
# # {1, 2, 3, 4, 5, 6, 7}



# 要確認
# l = []
# for i in range(1,11):
#     if i
#
# l = [i for i in range(1,11) if i ** 2 >= 10]
# print(l)
# ここまで

# l = []
# for i in range(1, 4):
#     for j in range(5, 8):
#         l.append((i, j))
# print(l)
# # [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]
#
# ll = [[(i, j) for i in range(1, 4)] for j in range(5, 8)]
# print(ll)
# # [[(1, 5), (2, 5), (3, 5)], [(1, 6), (2, 6), (3, 6)], [(1, 7), (2, 7), (3, 7)]]

# # 1から100までの数字を出力するプログラミングを書いてください。
# ただし、数字が3の倍数の時は数字の代わりにFizzと出力し、
# 5の倍数の時は数字の代わりにBuzzと出力し、
# 3と5の倍数のときは、FizzBuzzと出力すること。
# for i in range(1,101):
#     if i%3 == 0:
#         print('Fizz')
#     elif i%5 == 0:
#         print('Buzz')
#     elif i%3 == 0 and i%5 == 0:
#         print('FizzBuzz')
#     else:
#         print(i)

# 関数
# def test_func():
#     print('call test_func')
#
#
# class TestClass:
#     # メソッド
#     def test_method():
#         print('call test_method')
#
#
# print('------------------------')
# print(test_func)
# print(TestClass.test_method)
#
# print('------------------------')
# print(type(test_func))
# print(type(TestClass.test_method))
#
# print('------------------------')
# t = TestClass()
# print(test_func)
# print(t.test_method)
#
# print('あなたの名前を教えてください。')
#
# your_name = input('>> ')
#
# print(your_name)

# for i in range(5,11):
#     print(i)

# def func2():
#     print('this is func')
#
# func2()

# def add(a, b):
#     print(a * b)
#
# add(1, 2)
# add(2, 3)

# def add(a, b):
#     return a + b
# print(add(1, 2))
# print(add(2, 3))


# def add(a, b):
#     return a + b
#
#
# def sub(a, b):
#     return a - b
#
#
# print(add(1, 2))
# print(add(2, 3))


# def func(a=0, **kwargs):
#     print('a:', a)
#     print('kwargs:', kwargs)
#
# func()
# func(a=1, b=2)
# func(a=1, b=2, c=3, d=4)

# def func(*args, **kwargs):
#     print('args:', args)
#     print('kwargs:', kwargs)
#
# func()
# func(a=1, b=2)
# func(1, 2, a=3, b=4)

#
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
#
# func = add
# print(func(10, 20, 30))
#
# def sortkey(x):
#     return  x[1]
#
# ll = [[3, 5], [1, 2], [4, 3], [2, 4], [5, 1]]


# def adder(a):
#     def inner(x):
#         # xは関数内関数の引数、aはadder呼び出し時の引数
#         return x + a
#     return inner
#
# # クロージャを作成し、add3, add5に代入する
# add3 = adder(3)
# add5 = adder(5)
#
# # add3, add5に代入されたクロージャを呼び出す
# print(add3(10))
# print(add5(10))

# ll = [[3, 5], [1, 2], [4, 3], [2, 4], [5, 1]]
# def sortkey(x):
#     return x[1]
#
# print(sorted(ll, key=sortkey))

# add = lambda a, b: a + b
# print(add(2, 3))

# def adder(a):
#     return lambda x: x + a
#
# a = adder(3)
# b = adder(5)
#
# print(a(10))
# print(b(10))


# def hoge(hello):
#     return sorted(hello, key=sortkey))

# def func2(l):
#     return l[1] + l[2]
#
# def func1(x):
#     try:
#         func2([x])
#     except:
#         print('exception occurred')
#
# func1(1)
# print('end')

# while True:
#     try:
#         s = input('Input number(q for exit):')
#         if s == 'q':
#             break
#         num = int(s)
#         print(100 / num)
#     except ZeroDivisionError as ex:
#         print('num is 0')

# # 反転させたい文字列
# str = '12345'
# #
# # # 文字列[::-1]とすれば反転できる
# rslt = str[::-1]
# print(rslt)
# # => '54321'
#
# def sortkey(x):
#     return x[1]
#
# sorted(ll, key=sortkey)

def hoge(x):
    return x[::-1]

# x = 'hello'

print(hoge('hello'))







