from abc import ABC, abstractmethod

class Test(object):
    @staticmethod
    def main():
        print(3)

if __name__ == "__main__":
    func = getattr(Test, 'main')
    func()