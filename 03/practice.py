# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner    # ✅ Return the function, not call it
#
# def ordinary():
#     print("I got ordinary")
#
# decorated_func = make_pretty(ordinary)  # ✅ Now returns the decorated version
# decorated_func()  # ✅ Call it
#
# def divide(x,y):
#     print(x//y)
#
# def outerdiv(func):
#     def inner(x,y):
#         if(x<y):
#             x,y = y,x
#             return func(x,y)
#         else:
#             return func(x,y)
#     return inner
#
# div1 = outerdiv(divide)
#
# div1(2,4)



def split_str(function):
    def wrapper():
        func = function()
        split_str = func.split()
        return split_str
    return wrapper

def uppercase(function):
    def wrapper():
        func = function()
        uper = func.upper()
        return uper
    return wrapper

@split_str
@uppercase
def say_hi():
    return "hi world"
print(say_hi())
