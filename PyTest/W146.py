from PyTest import *
##///////////////////// PROBLEM STATEMENT /////////////////////////
## Given three ints, a b c, print True if b is greater than a,   //
## and c is greater than b. However, with the exception that if  //
## "bOk" is True, b does not need to be greater than a.          //
##   1 2 4 False -> True                                         //
##   1 2 1 False -> False                                        //
##   1 1 2 True -> True                                          //
##/////////////////////////////////////////////////////////////////

# Input the values

a = int(input())
b = int(input())
c = int(input())
boolValue = input()

# IF "bOk" is TRUE and C is GREATER than B - Print TRUE
# ELSE is A < B < C - Print TRUE
if boolValue == "True" and b < c:
    print("True")
elif a<b<c:
    print("True")
else:
    print("False")