#!/usr/bin/python3

# Author: zhanjunkai

from collections import namedtuple

# --------------------------------------------------
# Function: profile()
# Description: a useless function with multi return
# --------------------------------------------------
def profile():
    name = "Junkai"
    age  = 25
    return (name, age)

# --------------------------------------------------
# Function: profile_2()
# Description: a useless function with multi return
# --------------------------------------------------
def profile_2():
    name = "Junk"
    age  = 18
    return name, age

# --------------------------------------------------
# Function: profile_3()
# Description: a useless function with multi return
# --------------------------------------------------
def profile_3():

    # namedtuple is a class name
    # so person is just declaration
    person = namedtuple('person', 'name age')
    return person(name = "Jack", age = 21) 

# ----------------------------------------------
# Function: return_demo()
# Description: a demo of return multi variables
# ----------------------------------------------
def return_demo():
    
    # Perform profile function
    print("--------------- Step 1: perform profile function 1 ----------")
    profile_data = profile()
    print("Profile[0] = " + str(profile_data[0]))
    print("Profile[1] = " + str(profile_data[1]))

    # Perform profile_2 function
    print("--------------- Step 2: perform profile function 2 ----------")
    name_2, age_2 = profile_2()
    print("Name from profile_2 = " + str(name_2))
    print("Age from profile_2  = " + str(age_2))

    # Perform profile_3 function
    print("--------------- Step 3: perform profile function 3 ----------")
    # Use 1: as namedtuple
    print(">>> namedtuple as object")
    p = profile_3()
    print(p, type(p))
    print("p.name : " + str(p.name))
    print("p.age  : " + str(p.age))

    # Use 2: as plain tuple
    print(">>> nametuple as plain tuple")
    print("p.name : " + str(p[0]))
    print("p.name : " + str(p[1]))

    # USe 3: unpack the object immediatly
    print(">>> namedtuple unpack immediatly")
    name, age = p
    print("name is : " + str(name))
    print("age is  : " + str(age))


# ----------------------------------------------
# Function: main()
# Description: run the main program
# ----------------------------------------------
def main():
    return_demo()

if __name__ == '__main__':
    main()