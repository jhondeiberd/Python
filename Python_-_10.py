
###################numpy ############################################
# import numpy
# arr = numpy.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr)
#reshaping means changing the shape of an array.
#the shape of an array is the number of elements in each dimension
#by reshaping we can add or remove dimenions or change the number of elements in each dimension.

#4 arrays of 3 elements each
# newarr=arr.reshape(4,3)
# print(newarr)
# #2 arrays of 6 elements each
# newarr=arr.reshape(2,6)
# print(newarr)
# #12 arrays of 1 element each
# newarr=arr.reshape(12,1)
# print(newarr)


# #we want convert : having 2 arrays,containing 3 arrays, each with 2 elements
# import numpy
# arr = numpy.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(2,3,2)
# #print(newarr)
# #having 2 arrays, that containing 3 arrays, that each contains 2 arrays, each with one element
# newarr=arr.reshape(2,3,2,1)
# print(newarr)


# import numpy
# n=numpy.arange(27)
# print(type(n))
# print(n)
# print(40 * '=')
#
# #lests reshape it to 3 rows (arrays) , and 9 elements in each
# a=n.reshape(3,9)
# print(a)
# print(40 * '=')
#
# #lets reshape it 3 groups of 3 lists of 3 elements each
# b=n.reshape(3,3,3)
# print(b)

#lets have 1000 arrays, that contains 100 arrays,each contains 100 arrays each with 10 elements
# import numpy
# arr = numpy.arange(100000000)
# newarr=arr.reshape(1000,100,100,10)
# print(newarr)

# #lets make a 6 dimensions with 10 elements in each
# import numpy
# arr = numpy.arange(10000000)
# newarr= arr.reshape(10,10,10,10,10,10,10)
# print(newarr)


# #lets create numpy array from a python list:
# import numpy
# # a = [1,2,3,4,5]
# # print("my list is " ,a)
# # m=numpy.asarray(a)
# # print("numpy array is ",m)
#
# #2D list
# a = [[1,2,3],[4,5,6]]
# print("my list is " ,a)
# m=numpy.asarray(a)
# print("numpy array is ",m)


#lets creat numpy array from tuple
# import numpy
# t = ([1,2,3],[4,5,6])
# print("tuple ",t)
# print(40 * '=')
# m=numpy.asarray(t)
# print("numpy array ", m)


#flattering the arrays
#just mean taking a multidimentional array and turning it to a regular , single dimentional array
# import numpy
# arr = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# newarr= arr.reshape(-1)
# print(newarr)


# #iterating a numpy array
# import numpy
# arr = numpy.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# for x in arr:
#     for y in x:
#         for z in y:
#             print(z , end = " ")
#
# #iterating with different step size
# print('##############')
# for x in numpy.nditer(arr[:,::2]):
#     print(x, end = " ")



# #how to convert a list of different sized lists into a NumPy array
# #lests find the longest row and we re gonna add values into other rows till they get equal
# a_list = [[1,2],[1],[1,2,3]]
# row_lenghts =[]
# for row in a_list:
#     row_lenghts.append(len(row))
#
# max_lenght = max(row_lenghts)
# print(max_lenght)
#
# for row in a_list:
#     while len(row) <max_lenght:
#             row.append(None)
#             print(row)
#
# import numpy
# new_balanced_array = numpy.array(a_list)
# print(new_balanced_array)



#when we talk performance of numpy, we talk speed.
#we want to demonstrate some performance numbers of operations between lets say pure python and package NumPy.
#what we want to underline is NumpY is usually faster than the python core library


# import time
# import numpy as np
# size_of_vec = 100000000
# 
# def pure_python_version():
#     t1 = time.time()
#     X = range(size_of_vec)
#     Y = range(size_of_vec)
#     Z= [ X[i] + Y[i] for i in range(len(X))]
#     return time.time() - t1
# 
# def numpy_version():
#     t1 = time.time()
#     X = np.arange(size_of_vec)
#     Y = np.arange(size_of_vec)
#     Z= X + Y
#     return time.time() - t1
# 
# t1 = pure_python_version()
# t2= numpy_version()
# print(t1,t2)
# print("numpy in this example is " + str(t1/t2) + " faster")






#################################################################################################

#OpenCV-Python is a library of Python bindings designed to solve computer vision problems. ...
# All the OpenCV array structures are converted to and from Numpy arrays. This also makes it easier
# to integrate with other libraries that use Numpy such as SciPy and Matplotlib.

#OpenCV is a cross-platform library using which we can develop real-time computer vision applications.
# It mainly focuses on image processing, video capture and analysis including features like face
# detection and object detection.

#in order to instll pip:
#if you dont have pip then:
#getting pip:
#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#python get-pip.py
#pip help
#pip --version
#python -m pip install --upgrade pip
#else you install opencv directly:
#pip install opencv-python




#the OpenCV image processing library.OpenCV is also
#referred to as cv2 in Python.

#Install OpenCV:
# 1. Open the command line and type:
#
# pip install opencv-python
#
# 2. Open a Python session and try:
#
# import cv2
#
# 3. If you get no errors, you installed OpenCV
#  successfully. If errors, then try:
#
# . My OpenCV installation didn't work on Windows
#
# Solution:
#
# 1. Uninstall OpenCV with:
#
# pip uninstall opencv-python
#
# 2. Download a wheel (.whl) file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv

#  and install the file with pip. Make sure you download the correct file for your Windows
# and your Python versions. For example, for Python 3.6 on Windows 64-bit you would do this:
#
# pip install opencv_python‑3.2.0‑cp36‑cp36m‑win_amd64.whl
#
# Try to import cv2 in Python again. If there's still an error, type the following
# again in the command line:
#
# pip install opencv-python
#
# Try importing cv2 again. It should work at this point.

#########################################################################################################

##############################################################
#import cv2

# #now try importing our famous image into python
#
# # 0 for black and 255 for white
# # 0 is for gray scale image
#
#im_g=cv2.imread("c:\\workshop\\smallgray.png",0)
#print(im_g)
#
# print('################################')
# # 1 is for BGR
# im_g=cv2.imread("c:\\workshop\\smallgray.png",1)
#print(im_g)
#
# #so the intensity for the first pixel would be : 187 for Blue, 198 for Green,209 for Red
#
# #in order to create an image from your numpy array:
# cv2.imwrite("c:\\workshop\\newsmallgray.png",im_g)
# #output: true
# #go to c:\workshop folder and find the image just created  : newsmallgray.png
#

#lion=cv2.imread("c:\\workshop\\lion.png",0)
#cv2.imwrite("c:\\workshop\\newlion.png",lion)

#lion=cv2.imread("c:\\workshop\\lion.png",1)
#cv2.imwrite("c:\\workshop\\newlion2.png",lion)




# #################################
# #indexing, slicing and iterating Numpy Arrays
#
# #for a list we do:
# a=[1,2,3]
# print("list ",a)
# print("slice ",a[0:2])

##################################

#with numpy arrays:

##first i need a numpy array and this is the one i will work with for this case:
# im_g=cv2.imread("c:\\workshop\\smallgray.png",0)
# print(im_g)
# print(type(im_g))
# print('##################################')

## to get the first 2 rows
# print(im_g[0:2])
# print('##################################')

##now if we want a slice from the middle, we should
##add a comma and then define the columns we want.
# print(im_g[0:2,0:2])
# print('##################################')

##to see the form of the numpy array
# print(im_g.shape)
# print('##################################')

##we could use the indexing to get the element we want:
# print(im_g[2,3])
# print('##################################')

##in order to iterate in the numpy array:

# for i in im_g:
#     print(i)
# print('##################################')
# #or
#the transpose of the numpy array
# for i in im_g.T:
#    print(i)
# print('##################################')
# #or

# #flat() function is used to make 1-D iterator over the array.

#counter=0
#for i in im_g.flat:
#   counter+=1
#    print(i,end=',' if counter<15 else ' ')
# print('##################################')

# #concatenating (stacking) and splitting numpy arrays
# import numpy

# print(im_g)
# print('#####################################')

# #hstack is used to stack the sequence of input arrays horizontally
# ims=numpy.hstack((im_g,im_g))
# print(ims)
# print('####################################')

# ims=numpy.hstack((im_g,im_g,im_g))
# print(ims)
# print('####################################')




# #vstack is used to stack the sequence of input arrays vertically
# ims=numpy.vstack((im_g,im_g,im_g))
# print(ims)
# print('####################################')


# # lets make one array for each column
# lst=numpy.hsplit(ims,5)
# for l in lst:
#     print(l)
# #the type of lst is python list
# print(type(lst))
# print('####################################')

# #spliting vertically
# lst=numpy.vsplit(ims,3)
# for l in lst:
#     print(l)
# print('####################################')








