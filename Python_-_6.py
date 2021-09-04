###############Tuples #################
# # • is a term for an ordered set of data.
# # • Are immutable. They can’t be changed :
# # attempting to append an item to a tuple will actually give you an
# # error.
# t = "a", "b","c"
# print(type(t))
# print(t)
# print(("a", "b", "c"))
# print("a","b","c") # this not a tuple

# #To join two or more tuples you can use the + operator:
#print(("a", "b", "c") + ("e","f"))
#
#
#print(("a", "b", "c") , ("e","f"))   #these are 2 tuples

#OneMemberTuple = ("Gabbar", )  #do NOT forget the comma, else would be a string!
#print(type(OneMemberTuple))


#we could have different data types on the tuples
# welcome = "Welcome to my Class", "Dara A.", 2021
# student = "Gabbar", "Singh", 1984
# teacher = "Singh", "Saheb", 2005
# print(welcome)
# print(student)
# print(student[0]) #supports indexing
# print(student[1])
# print(student[2])


# #this is an error because tuple is immutable !
# student = "Gabbar", "Singh", 1984
# student[0]= "Jean"


#this is a list and mutable
# student2 = ["Gabbar", "Singh", 1984]
# print(student2)
# student2[0] = "Jean"
# print(student2)



#list mutable, tuple immutable
# a = [0,1,2]
#print(type(a))
##id() return the identity of an object. This identity has to be unique and constant for
## this object during the lifetime.
# print(hex(id(a)))   #convert an integer number into hexadecimal
# a[2]=345
# print(hex(id(a[2])))
# print(hex(id(a)))




# # supports slicing
# teacher = "Dara", "Saheb", 2005
# print(type(teacher))
# print(hex(id(teacher)))
# #this teacher points on a completly new object !!
# teacher = teacher[0], "Dara Sahib",teacher[2]
# print(teacher)
# print(hex(id(teacher)))




# Why should we use tuple over a list??
# • A list is INTENDED (NOT ENFORCED THOUGH!) to keep  same type of objects
# • A list is mutable.
# • A tuple is INTENDED(EVEN TOUGH THEY COULD BE THE SAME) TO keep different type of objects
# • A tuple is immutable



#We could assign different values to different variable
# a = b = c = d = 12
# print(c)
# a, b = 12, 13 # can we do the same on tuple?!
# print(a, b)
# a, b = b, a
# print("a is {}".format(a))
# print("b is {}".format(b))


#student = "Gabbar0", "Singh0", 19840
#print("student before    " + hex(id(student)))
#student1 = "Gabbar1", "Singh1", 19841
#print("student1 before   " + hex(id(student1)))
#student, student1 = student1,student
#print(student)
#print("student  after    " + hex(id(student)))
#print(student1)
#print("student1 after    " + hex(id(student1)))



#teacher1 = "Dara", "Saheb", 2005
#print(type(teacher1))
#teacher2 = teacher1[0], "Dara Sahib",teacher1[2]
#print(type(teacher2))
#print("before changing them")
#print("teacher1" ,(teacher1))  #it does implicitely the string concatenation between str and tuple
#print("teacher1" + str(teacher1))
#print("teacher2" + str(teacher2))
#print("after changing them")
#teacher1, teacher2 = teacher2, teacher1
#print("teacher1" + str(teacher1))
#print("teacher2" + str(teacher2))






# #unpacking the tuple
# teacher = "Dara", "Saheb", 2005
# firstName, lastName, year = teacher
# print(firstName)
# print(lastName)
# print(year)





# Exercice: Given the tuple below that represents teacher courses for this
# semester, write code to print the teacher details, followed by a listing
# of all the courses for his semester.
# teacher = "Dara", "Saheb", 2021, ((1, "Python"), (2, "Java"), (3, "Javascript"), (4, "C++"))
# print(teacher)
#
# firstName, lastName, year, courses = teacher
# print(firstName)
# print(lastName)
# print(year)
# for course in courses:
#     code, title = course
#     print("\tcourse code {}, Title: {}".format(code, title))



# Which of the following creates a list?
# numbers1 = (1,2,3,4,5)
# print(type(numbers1))
# numbers2 = {1,2,3,4,5}
# print(type(numbers2))
# numbers3 = [1,2,3,4,5]
# print(type(numbers3))







# The code below create 2 lists, alpha1 and alpha2, then compares them.
# The result is True or False?
# alpha1 = ["A","B","C"]
# alpha2 = ["A"]
# alpha2.append("B")
# alpha2.append("C")
# print(alpha1 == alpha2)






# What will be the output from this program?
# numbers = range(13)
# new_range = numbers[1::2]  #slicing the range numbers
# print(type(new_range))
# for i in new_range:
#     print(i, end=', ')






# # What output will the following program produce?
# even = range(0, 20, 2)
# for number in even[::-1]:
#     print(number, end=' ')   #18 16 14 12 10 8 6 4 2 0
# print()
# for number in even[-1::]:
#     print(number, end=' ')  #18
# print()
# for number in even[1::-1]: #2 0
#     print(number, end=' ')







# #Assuming countries are declared as
# countries = ((1, 'english', 'Canada'),
#             ('2', 'french', "France"),
#             ('3', 'german', 'Germany'),
#             (4, 'hindi', 'India'),
#             ('5', 'italian', 'Italy')
#             )
# write a code that will produce the output:
# Canada
# France
# Germany
# India
# Italy

# # The answer:
# for country in countries:
#     number, language, name = country
#     print(name)
#     print(number,language,name)


