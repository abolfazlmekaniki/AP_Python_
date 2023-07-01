The last two arguments in the function signature are *args and **keywords.


# Advanced Programming - HW6

1. Functions in python are defined as follows:

    ```python

    def func(a, b, c, ..., *args, **keywords):

    ```

    Explain the last two arguments and their application with examples:

    *args is used to pass a variable number of non-keyword arguments to a function. When the *args parameter is used in a function definition, it allows the function to receive any number of positional arguments, which are then collected into a tuple. These positional arguments can be accessed within the function using the args variable.

    Here's an example of how *args can be used in a function:
    ```python

    def multiply(*args):
        result = 1
        for arg in args:
            result *= arg
        return result

    print(multiply(2, 3, 4))  # Output: 24
    print(multiply(5, 10, 2, 3))  # Output: 300

    ```

    In this example, the multiply function can take any number of arguments, and it will multiply all of them together.

    **keywords is used to pass a variable number of keyword arguments to a function. When the **keywords parameter is used in a function definition, it allows the function to receive any number of keyword arguments, which are then collected into a dictionary. These keyword arguments can be accessed within the function using the keywords variable.

    Here's an example of how **keywords can be used in a function:
    ```python

    def print_values(**keywords):
        for key, value in keywords.items():
            print(f"{key}: {value}")

    print_values(a=1, b=2, c=3)  # Output: a: 1 \n b: 2 \n c: 3
    print_values(name="John", age=30, city="New York")  # Output: name: John \n age: 30 \n city: New York

    ```

    In this example, the print_values function can take any number of keyword arguments, and it will print out each key-value pair in the dictionary.


2. Consider the following codes:

    ```python
    A0 = dict(zip((’a’, ’b’, ’c’, ’d’, ’e’), (’1’, ’2’, ’3’, ’4’, ’5’)))
    A1 = range(10)
    A2 = [i for i in A1 if i in A0]
    A3 = sorted(A0[i] for i in A0)
    A4 = [[i, i*i] for i in A1]
    ```

    * Write the output of each line without running their:

    ```python
        A0={"a":'1',"b":'2',"c":'3',"d":'4',"e":'5'}

        // A1 is range object that represents an immutable sequence of numbers.

        A2=[] // because A0 keys are not in range 0-10 so it is empty list.

        A3 = ['1','2','3','4','5']  // "for i in A0" iterates in A0 keys and append that key value in A3 in a sorted way .

        A4= [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]] // from 0-9 , append a list of [i , i^2] to A4.

    ```


    * Write the code to print all the variables of A0...A4 with one loop.

        for that we can store all the variables in a dictionary and iterate to ite keys and values in order to print all the variables.

        ```python

        variables = {'A0': A0, 'A1': A1, 'A2': A2, 'A3': A3, 'A4': A4}

        for var_name, var_value in variables.items():
            print(f'{var_name}: {var_value}')

        ```