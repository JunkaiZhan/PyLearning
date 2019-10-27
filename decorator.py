#!/usr/bin/python3

# Author: zhanjunkai

# Q: What are decorators?
# A: They are the functions or class which can modify the functionality of other functions.
#    Using decorators can make you code concise.

from functools import wraps
import pysnooper

# ----------------------------------------------
# Function: temp_func_1()
# Description: 
# ----------------------------------------------
def temp_func_1():
    print("This is temp_func_1.")

# ----------------------------------------------
# Function: temp_func_3()
# Description: 
# ----------------------------------------------
def temp_func_3(name = "Junkai"):

    def hello():
        return "Hello, " + name

    def bye():
        return "Byebye, " + name

    if name == "Junkai":
        return hello
    else:
        return bye

# ----------------------------------------------
# Function: temp_func_4()
# Description: 
# ----------------------------------------------
def temp_func_4(arg_func):
    print(arg_func())

# ----------------------------------------------
# Class: logit_c
# Description: define a decorator base class
# ----------------------------------------------
# classes can also be used to build decorators.
class logit_c(object):

    _logfile = "log.txt"

    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        print(log_string) # report the log message local
        self.func(*args)
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string) # report the log message into log file
        self.notify()

    def notify(self):
        # if need more log operation, can modify the functionality
        pass

# ----------------------------------------------
# Class: email_logit_c
# Description: define a decorator extend class
# ----------------------------------------------
class email_logit_c(logit_c):

    # the email_logit_c is extended from logit_c
    # for adding notify funtionality

    def __init__(self, email="junkaizhan@gmail.com", *args, **kwargs):
        self.email = email
        super(email_logit_c, self).__init__(*args, **kwargs) #! why use super ??

    def notify(self):
        # new operation for notify, such as sent an email to self.email
        pass

# ----------------------------------------------
# Function: decorator_demo()
# Description: a decorator demo
# ----------------------------------------------
def decorator_demo():
    
    # 1. Everything in python is an object, include function --------
    print("\n>>>>> Step 1: Everything in python is an object")
    temp = temp_func_1 # Then temp is a new function object
    temp()

    # 2. Functions can be defined in a function ---------------------
    print("\n>>>>> Step 2: Functions can be defined in a function")
    def temp_func_2():
        return "This is temp_func_2."
    
    print(temp_func_2()) # Then execute the temp_func_2 by adding ()

    # 3. Function can be returned from a function -------------------
    print("\n>>>>> Step 3: Function can be returned from a function")
    temp = temp_func_3(name = "Junk") # temp_func_3 will return a function
    print(temp())                       # Then we can execute the temp by ()

    # 4. Function as an argument to another function ----------------
    print("\n>>>>> Step 4: Function as an argument to another function")
    temp_func_4(temp_func_2)

    # 5. Combine 1234, create the first decorator ------------------
    # ! Note: use a decorator means modify the functionality of the function
    # How to do that: 
    # -1- Define a decorator，which is a function (A) actually and its argument is a function(B).
    # -2- Define a new function (C) in the decorator, to modify the argument function (B)
    # -3- Then return the new function (C) to caller 
    print("\n>>>>> Step 5: Create the first decorator and use it")
    
    # Now we define a decorator (A) 
    def iam_decorator (func_need_dec): # func_need_dec here is the function (B)
        
        # Use wraps decorator can advoid the __name__ and docstring be changed
        @wraps(func_need_dec)
        
        # Define a new function (C)
        def new_func_after_dec():
            print("Pre work before executing func_need_dec()")
            func_need_dec()
            print("Post work after executing func_need_dec()")
        return new_func_after_dec
    
    @iam_decorator
    def func_need_dec():
        print("I am the function need decoration")
    # Equivalent to: func_need_dec = iam_decorator(func_need_dec)

    func_need_dec() # The func_need_dec has been decorated by iam_decorator

    # 6. More advanced application -----------------------------------
    # It mean the decorators can be used in authorization check
    print("\n>>>>> Step 6: Add dynamic switch for decorated function")
    
    def iam_decorator_2 (func_need_dec):
        @wraps(func_need_dec)
        def new_function_after_dec():
            if SW == True:
                return func_need_dec()
            else:
                return "The SW is turn off now"
        return new_function_after_dec
    
    @iam_decorator_2
    def func_need_dec_2():
        return "I am func_need_dec_2"
    
    SW = False
    print(func_need_dec_2())

    SW = True
    print(func_need_dec_2())

    # 7. Another use: logit -----------------------------------------------
    print("\n>>>>> Step 7: Add log message for function ")

    def logit(func_old): # Decorator is function, so it can have args
        @wraps(func_need_dec)
        def with_log(*args): # With argument, send to func_need_dec
            print(func_old.__name__ + " was called")
            return func_old(*args)
        return with_log
    
    @pysnooper.snoop(prefix="hello func ")
    @logit
    def hello(name):
        return "Hello, " + name

    print(hello("Junkai"))

    # 8. Decorator with arguments -----------------------------------------
    print("\n>>>>> Step 8: Decorator with argument")

    # Nesting a decorator within a function
    def logit_new(text):
        def log_decorator(func):
            @wraps(func)
            def new_func(*args, **kwargs):
                print(func.__name__ + " was called and outside param is " + text)
                return func(*args, **kwargs) #! must return, if just code "func(*args, **kwargs)", will return None to caller
            return new_func
        print("logit with argument: %s is called" % text)
        return log_decorator

    @pysnooper.snoop(prefix="Step 8: ") 
    @logit_new("TEXT DEMO")
    def sub(opa, opb):
        if (opa > opb): 
            return opa - opb
        else:
            return opb - opa
    
    result = sub(7, 4)
    # ? Can be understood as: sub = the function returned from logit_new, so sub = log_decorator
    # ? Then, because the decorator is nested, sub = the function returned from log_decorator
    # ? Finally, the sub is new_func. The new_func is designed to do two things.
    # ? -1- print the ... was called and outside param ....
    # ? -2- then execute the func, but the func will return a value, which must be captured by new_func
    # ? So, it is must use return key word to return the (value returned from func)
    print(result)

    # 9. Decorators Class ---------------------------------------------------------
    print("\n>>>>> Step 9: Decorator class")

    logit_c._logfile = "out.log" # if change the log file
    @logit_c # or @email_logit_c
    def last_func(name):
        print("This is the last func: " + name)

    last_func("In Step 9")
    
# ----------------------------------------------
# Function: main()
# Description: run the main program
# ----------------------------------------------
def main():
    decorator_demo()


if __name__ == '__main__':
    main()
