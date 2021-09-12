# import.pyのためのファイル

def add(a, b):
    return a + b

# このファイルを実行した時だけ、実行される.
# 別のファイルにインポートされたときは実行されない
if __name__ == '__main__':
    print(add(2, 3))
    print(add(5, 8))