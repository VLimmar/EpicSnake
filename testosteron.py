from datetime import datetime as dt
# def tirlist(listik, daf):
#     for temp in range(0, len(listik)):
#         listik[temp] = daf(listik[temp])
# def xtwo(a):
#     return a * 2



# a = [17, 18 , 61, 0, 39]
# tirlist(a, str)

# print(a)

# class Zero:
#     def __init__(self, b = 0) -> None:
#         self.zero = b
#     def __call__(self, a = None):
#         if a == None:
#             return self.zero
#         else: 
#             return Zero(self.zero + a)




# a = Zero()
# aa = a(34)(1)(100)()
# print(aa)
# def deco(daf):
#     def riper(*nam):
#         print("Начало")
#         a = daf(*nam)
#         print("Конец")
#         return a
#     return riper
# # @deco
# def name(nam, nyan):
#     return F"привет, {nam}, {nyan}"
# name = deco(name)
# print(name("tea", 7))
def deco(daf):
    def decored(*im):
        c = open("time.txt", "a")
        time = dt.now()
        a = daf(*im)
        aftertime = dt.now()
        c.write(F"{daf.__name__}:{aftertime - time}\n")
        c.close()
        return a
    return decored
@deco
def polechudes():
    a = []
    for temp in range (0, 10000000):
        a.append(temp)
