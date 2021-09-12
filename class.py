class Person:
    # 情報（属性）
    def __init__(self, name):
        self.name = name

    # 機能（メソッド）
    def greet(self):
        print('hello')

    def sleep(self):
        print('zzz')

    def run(self):
        print('run!!!')


Alice = Person('Alice')

Alice.sleep()
# zzz
Alice.run()
# run!!!