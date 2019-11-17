#!/usr/bin/python3

# Author: zhanjunkai

# ----------------------------------------------
# Function: args_demo()
# Description: a demo for *args and **kwargs
# ----------------------------------------------
def args_demo():

    print("-------------- What is *args ----------------")
    #? -1- Pass a varaible number of arguments to a function
    #? -2- *args is used to send a non-keyworded variable length argument tuple 
    #?     to the function
    def text_args(first_arg, *args):
        print("First args is: ", first_arg)
        for arg in args:
            print("Another arg is : ", arg)    
    text_args("Learning", "Python", "Demo", "HelloWorld")

    print("-------------- What is **kwargs --------------")
    #? -1- **kwargs allows you to pass keyworded variable length of argument to a function
    #?     It means pass a dict as argument
    def greet_me(**kwargs):
        for key, value in kwargs.items():
            print("{0} ----> {1}".format(key, value))    
    greet_me(name = "Google")

    print("------------- Call function --------------")
    def test_args_kwargs(arg1, arg2, arg3):
        print("ARG1 is :", arg1)
        print("ARG2 is :", arg2)
        print("ARG3 is :", arg3)
    
    args = (12, True, "JunkaiZhan")
    test_args_kwargs(*args)

    kwargs = {"arg1": True, "arg3": "JunkaiZhan", "arg2": 13}
    test_args_kwargs(**kwargs)

    #? Order of using *args, **kwargs and formal args
    # some_func(fargs, *args, **kwargs)

    print("--------------- Use as decorator --------------")
    
    # import someclass
    # def get_info(self, *args):
    #    # do somethine
    #    return "Test Data"
    # someclass.get_info = get_info()

# ----------------------------------------------
# Function: main()
# Description: run the main program
# ----------------------------------------------
def main():
    args_demo()

if __name__ == "__main__":
    main()