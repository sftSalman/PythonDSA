# class OverloadingDemo:
#     def add(self, x, y):
#         print(x+y)
#
#     def add(self, x, y, z):
#         print(x+y+z)
#
#
# obj = OverloadingDemo()
# obj.add(2, 3)




class OverloadingDemo:
    def add(self, x, y, z=None):
        if z is not None:
            print(x + y + z)
        else:
            print(x + y)


obj = OverloadingDemo()
obj.add(2, 3)        # Output: 5
obj.add(2, 3, 4)     # Output: 9
