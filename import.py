# モジュール（〇〇.py　ファイルのこと）をインポート

# sampleB.py全部をインポートする
# import sampleB
#
# print(sampleB.add(2, 3))


# sampleB.py全部をインポートし、BBという名前をつける
# import sampleB as BB
#
# print(BB.add(2, 3))


# sampleB.pyの中のaddという関数だけをインポートする
from sampleB import add

print(add(2, 3))


# sampleB.pyの中のaddという関数だけをインポートし、BBという名前をつける
# from sampleB import add as BB
#
# print(BB(2, 3))