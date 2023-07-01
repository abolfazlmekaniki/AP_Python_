import math
import subprocess
import matplotlib.pyplot as plt
import time







class CGaussSolver():
    def __init__(self,pf,a,b,n):
        self.m_Pf=pf
        self.m_A=a
        self.m_B=b
        self.m_N=n
        self.m_Result=None
        print(self.m_Pf)
    
    def legendre(self,m_N,x):
        if m_N==0:
            return 1
        elif m_N==1:
            return x
        else:
            return ((2.0 * m_N - 1) / m_N) * x * self.legendre(m_N - 1, x) - ((1.0 * m_N - 1) / m_N) * self.legendre(m_N - 2, x);


    def dLegendre(self,m_N,x):
        dLegendre=(1.0 * m_N / (x * x - 1)) * ((x * self.legendre(m_N, x)) - self.legendre(m_N - 1, x))
        return dLegendre


    def legendreZeroes(self,m_N,i):
        pi=3.141592655
        xold1 = math.cos(pi * (i - 1 / 4.0) / (m_N + 1 / 2.0))
        iteration = 1
        while True:
                if iteration != 1:
                    xold1 = xnew1
                xnew1 = xold1 - self.legendre(m_N, xold1) / self.dLegendre(m_N, xold1)
                iteration += 1
                print(1 + abs((xnew1 - xold1)))
                if 1 + abs((xnew1 - xold1)) >1.:
                    print("in if ")
                    break

        return xnew1
    

    def weight(self,m_N,x):

        weightI = 2 / ((1 - x**2) * self.dLegendre(m_N, x)**2);
        return weightI;


    def exec(self):
        integral =0
        iteration =1
        iteration+=1
        integral=0
        for i in range(1,self.m_N+1):
            integral = integral + self.m_Pf(self.legendreZeroes(self.m_N, i)) * self.weight(self.m_N,self.legendreZeroes(self.m_N, i))

        self.m_Result = ((self.m_B - self.m_A) / 2.0) * integral;

    def getResult(self):
        return self.m_Result
    




def my_function(x):
    xN = 0.5 * x + 0.5;
    return ((xN**3) / (xN + 1))*math.cos((xN**2))

solver = CGaussSolver(my_function, 0, 1, 10)
print("Before solver.exec()")
solver.exec()
print("After solver.exec()")
result = solver.getResult()
print(result)

cpp_time = []
python_time = []
iteration = 11

for i in range(1, iteration + 1):
    solver = CGaussSolver(my_function, 0, 1, i)
    start_py = time.time()
    solver.Exec()
    end_py = time.time()
    compile_command = ['g++', 'main.cpp', 'CGaussSolver.cpp', '-o', 'my_program']
    subprocess.run(compile_command)
    run_command = ['./my_program','10']
    start_cpp = time.time()
    subprocess.call(run_command)
    end_cpp = time.time()
    pythontime=((end_py - start_py) * 1000)
    cpptime=((end_cpp - start_cpp) * 1000)
    print(f"python : (n = {i}) : {solver.getResult()}")
    print(f"Python exe time is : {pythontime} ms")
    print(f"C++ exe time is    : {cpptime} ms")
    print()
    cpp_time.append(cpptime)
    python_time.append(pythontime)


x_axis = list(range(1, iteration + 1))
plt.figure(num="Python / Cpp")
plt.plot(x_axis, python_time, color="blue", scalex=[1, iteration + 1])
plt.plot(x_axis, cpp_time, color="green", scalex=[1, iteration + 1])
plt.legend(["Python", "C++"])
plt.xlabel("Iteration")
plt.ylabel("Time (ms)")
plt.savefig("img.pdf", format="pdf")
# plt.show()



'''    *args is used to pass a variable number of non-keyword arguments to a function. When the *args parameter is used in a function definition, it allows the function to receive any number of positional arguments, which are then collected into a tuple. These positional arguments can be accessed within the function using the args variable.

    Here's an example of how *args can be used in a function:
'''
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(multiply(2, 3, 4))  # Output: 24
print(multiply(5, 10, 2, 3))  # Output: 300


# In this example, the multiply function can take any number of arguments, and it will multiply all of them together.



''' 

  **keywords is used to pass a variable number of keyword arguments to a function. When the **keywords parameter is used in a function definition, it allows the function to receive any number of keyword arguments, which are then collected into a dictionary. These keyword arguments can be accessed within the function using the keywords variable.

  Here's an example of how **keywords can be used in a function:

'''

def print_values(**keywords):
    for key, value in keywords.items():
        print(f"{key}: {value}")

print_values(a=1, b=2, c=3)  # Output: a: 1 \n b: 2 \n c: 3
print_values(name="John", age=30, city="New York")  # Output: name: John \n age: 30 \n city: New York


    #In this example, the print_values function can take any number of keyword arguments, and it will print out each key-value pair in the dictionary.

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), ('1', '2', '3', '4', '5')))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = sorted(A0[i] for i in A0)
A4 = [[i, i*i] for i in A1]

'''

        A0={"a":'1',"b":'2',"c":'3',"d":'4',"e":'5'}

        A1 is range object that represents an immutable sequence of numbers.

        A2=[] // because A0 keys are not in range 0-10 so it is empty list.

        A3 = ['1','2','3','4','5']  // "for i in A0" iterates in A0 keys and append that key value in A3 in a sorted way .

        A4= [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]] // from 0-9 , append a list of [i , i^2] to A4.

'''


# Write the code to print all the variables of A0...A4 with one loop.

#  for that we can store all the variables in a dictionary and iterate to ite keys and values in order to print all the variables.



variables = {'A0': A0, 'A1': A1, 'A2': A2, 'A3': A3, 'A4': A4}

for var_name, var_value in variables.items():
    print(f'{var_name}: {var_value}')



# estimate pi :

import random
import math

def IsInCircle(x, y):
    distance = math.sqrt(x**2 + y**2)
    return distance <= 1

def find():
    true_pi = math.pi
    estimated_pi = 0
    num_points = 0
    error = float('inf')
    while error > 0.01:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if IsInCircle(x, y):
            estimated_pi = (estimated_pi * num_points + 4) / (num_points + 1)
        else:
            estimated_pi = (estimated_pi * num_points) / (num_points + 1)
        num_points += 1
        error = abs(estimated_pi - true_pi) / true_pi
    return num_points


#part 5 


def find_special_numbers(arr):
    special_numbers = []
    for i in range(len(arr)):
        print(i)
        if arr[i]%6==0 and (i+1) %6 ==0 :
            special_numbers.append(arr[i])

    return special_numbers


arr = [1,2,3,4,5,6,7,8,9,10,11,12]
special_numbers = find_special_numbers(arr)
print(special_numbers)