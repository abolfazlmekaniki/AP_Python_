import asyncio
import math
import time
class Equation():
    def __init__(self,a,b) :
        self.a =a
        self.b = b

    def compute(self,x):

        self.x = x

        self.y = self.a*self.x + self.b

        return self.y


class QuadraticEquation(Equation):

        def __init__(self, a, b,c):
             super().__init__(a, b)
             self.c = c
        
        def compute(self, x):
            self.x =x 
            self.y = self.a*(x**2)+ self.b*x +self.c

            return self.y

        
async def main():
     
    async def find_root_binary_search(equation , left , right, precision) :
             precision_ = ((right + left) /2)
             right_ = right 
             left_ = left
            
             while equation.compute(precision_)!=0 and (right_ - left_) > precision:

                 if equation.compute(precision_)<0:
                     right_ = precision_
                     precision_ = (left_+precision_)/2

                 elif equation.compute(precision_)>0:
                     left_ = precision_
                     precision_ = (right_+precision_)/2

                
             return precision_
           


    first = Equation(2,-3)
    second = QuadraticEquation(1,0,-4)
    thired = QuadraticEquation(3,-2,-1)

    corutine = [find_root_binary_search(first,0,3,0.001), find_root_binary_search(second,-3,0,0.001) , find_root_binary_search(thired,-1,2,0.001)]

    res = await asyncio.gather(*corutine)

    print(f"res is {res}" )


asyncio.run(main())


#========== part 2 =====================


def timing():
    def my_decorator2(func):
       
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            return f"{func.__name__}{args} took {start - end} s"

        return wrapper

    return my_decorator2


@timing()
def func1():
    return "hello Abolfazl"

print(func1())

#========================================

def memorize():
    cashes = {}
    def my_decorator2(func):
       
        def wrapper(*args):
            # global result
            res = args
            if res in cashes:
                return cashes[res]
            else :
                 cashes[res] = func(*args)
                 return cashes[res]

        return wrapper

    return my_decorator2

result2=0

@memorize()
@timing()
def func2(a,b):
    return a+b


print(func2(4,5))
print(func2(7,5))
print(func2(4,5))
print(func2(9,5))

#========================================

def enforce_type(types):

    types_ = types
    def my_decorator2(func):
       
        def wrapper(*args):
            
            res = list(args)
            check = True;
            for i in res :
                for j in types_:
                    if isinstance(i,j):
                        types_.remove(j)
                        break
                    else :
                        check = False
                        raise TypeError
            
            if check :
                return func(*args)

        return wrapper

    return my_decorator2


@enforce_type([int,str])
def func3(*args):
    pass


func3(3,"abol")


#========================================

@memorize()
@enforce_type([int])
@timing() # in order to print function's name , put the timing decoration here 
def func4(a):
    res =0 
    for i in range(1,a+1):
        res+= 1/(i**2)
    return res
    



print(func4(10**6))
print(func4(10**6))