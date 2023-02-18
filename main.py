

class MyNewClass():

    def __init__(self, x, y):
        self.new_info = x
        self.new_info_2 = y

    def add(self, x, y):
        total = x + y
        return total

    def changeInfo(self, info1, info2):
        self.new_info = info1 
        self.new_info_2 = info2




Harry = MyNewClass("harry", "rebecca")

print(Harry.new_info, Harry.new_info_2)
Harry.changeInfo("This has been changed", "this has also been changed")
print(Harry.new_info, Harry.new_info_2)


