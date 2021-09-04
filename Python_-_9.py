######################### static method in python #############################
# class MyClass(object):
#     @staticmethod
#     def the_static_method(x):
#         print(x)
# 
# MyClass.the_static_method(2)  # outputs 2






#########################################    closure   ##########################################################
#closure
#Python assumes that all variables in a function are local. This is to avoid accidental
# use of a global variable of the same name, or in an enclosing scope. In some
# important way, this difference is consequence of the fact that in Python local
# variable declaration is automatic/implicit while in JavaScript it is not (you have to use var).

# #example 1
# me = 'test'
# def myFunc():
#     global me
#     me = "locally defined"   # Defined locally but declared as global
#     print(me)
# 
# myFunc()
# print(me)     # Asking for a global variable





# # In Python, global keyword allows you to modify the variable outside of the current
# # scope. It is used to create a global variable and make changes to the variable
# # in a local context.
#
# #Normally, when you create a variable inside a function, that variable is local, and
# # can only be used inside that function. To create a global variable inside a function,
# # you can use the global keyword.
# #To change the value of a global variable inside a function, refer to the variable by
# # using the global keyword:
# #example 2
# def generateNextNumber(startNumber):
#     global current
#     current= startNumber
#     def tempFunction():
#         global current
#         current += 1
#         return current
#     return tempFunction
#
# mytempFunction= generateNextNumber(10)
# for i in range(10):
#     print (mytempFunction())
#
# #example 3
# def generateNextNumber(startNumber):
#     global current
#     current= startNumber
#     def tempFunction(increment):
#         global current
#         current += increment
#         return current
#     return tempFunction
#
# mytempFunction= generateNextNumber(10)
# for i in range(10):
#     print (mytempFunction(5))




# #The nonlocal keyword is used to work with variables inside nested functions, where
# # the variable should not belong to the inner function.
# #Use the keyword nonlocal to declare that the variable is not local.
#
# #another way of doing closure with nonlocal keyword
# #Use a nonlocal declaration
# def generateNextNumber(startNumber):
#     current= startNumber
#     def tempFunction():
#         nonlocal current
#         current += 1
#         return current
#     return tempFunction
#
# mytempFunction = generateNextNumber(10)
# for i in range(10):
#     print(mytempFunction())

###############################################################















