

class MyNewClass():

    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def changeInfo(self, info1, info2):
         self.name1 = info1 
         self.name2 = info2

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y


Harry = MyNewClass("harry", "rebecca")

print(Harry.name1, Harry.name2)
Harry.changeInfo("Steven", "Pinot")
print(Harry.name1, Harry.name2)

print(Harry.add(5,7))
print(Harry.subtract(5,2))
