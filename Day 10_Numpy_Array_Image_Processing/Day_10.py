"""
Image Data Handling using Numpy
"""

a = [0,1,2,3,4,5,6,7,8]
print (type(a))
print (a)  
# it always prints the values with comma seperated , thats list


# Convert your list data to NumPy arrays
import numpy as np

x = np.array( a ) 
print (type(x))

print (x)
# it always prints the values WITHOUT comma seperated , thats ndarray


"""
Explain the ndarray data Structure Image
NumPy_NDArray_Data_Structure.png
"""

# to print the data type of the elements of array 
print (x.dtype)


# to print the dimension of the array 
print (x.ndim)

# to print the shape of the array 
# returns a tuple listing the length of the array along each dimension
# For a 1D array, the shape would be (n,) 
# where n is the number of elements in your array.
print (x.shape)


# Shows bytes per element 
print (x.itemsize)

# reports the entire number of elements in an array
print(x.size)

# returns the number of bytes used by the data portion of the array
print (x.nbytes)

print (x.strides)


# Array Indexing will always return the data type object 
print (x[0])
print (x[2])
print (x[-1])


# Array Slicing will always return ndarray  
# data [ from : to ]
print (x[:])  # blank means from start or till end
print (x[0:]) 
print (x[:3]) 
print (x[0:2])




"""
Reshaping is changing the arrangement of items so that shape of the array changes
Flattening, however, will convert a multi-dimensional array to a flat 1d array. 
And not any other shape.
"""

# Reshaping to 2 Dimensional Array - 3 Rows and 3 Columns
x = x.reshape(3,3)
print (x)

import numpy as np
a = np.array(list(range(1,28)))
print(a)


# reshape the data set in 2-D
two_d = a.reshape(9,3)
print(two_d)

# reshape the data in 3-D
three_d = a.reshape(3,3,3)
print(three_d)

print (x.ndim)
print (x.shape)
print (x.strides)


# Due to reshaping .. none of the below has changed 
print (x.dtype)
print (x.itemsize)
print (x.size)
print (x.nbytes)


# Reshaping to 3 Dimensional Arry -  3 layers of 3 Rows and 3 Columns 
x = np.array( [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27] )
print(x)

x = x.reshape(3,3,3)
 
print (x)
print (x.ndim)
print (x.shape)

print (x.dtype)
print (x.itemsize)
print(x.size)
print (x.nbytes)

       

"""
For 1D array, shape return a  tuple with only 1 component (i.e. (n,))
For 2D array, shape return a  tuple with only 2 components (i.e. (n,m))
For 3D array, shape return a  tuple with only 3 components (i.e. (n,m,k) )
"""


# Creating 2 Dimensional Array 
x = np.array( [ [1, 2, 3], [4, 5, 6] ] )
print (type(x))

print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)
# For 2D array, return a shape tuple with only 2 elements (i.e. (n,m))



# Array Indexing 
print (x)

print (x[0])
print (type(x[0]))

print (type(x[0,0]))
print (x[0,0])
print (x[0,1])
print (x[0,2])


print (x[1])
print (type(x[1]))

print (type(x[1,0]))
print (x[1,0])
print (x[1,1])
print (x[1,2])



# Creating 3 Dimensional Array

#x = np.array([ [ [1, 2, 3], [4, 5, 6]], [ [11, 22, 33], [44, 55, 66] ], [ [111, 222, 333], [444, 555, 666] ]  ] )
x = np.array([ [ [1, 2, 3], [4, 5, 6], [7,8,9] ], [ [11, 22, 33], [44, 55, 66], [77,88,99] ], [ [111, 222, 333], [444, 555, 666], [777,888,999] ]  ] )
print (x)

print (x.ndim)
print (x.shape)
print (x.dtype)
# For 3D array, return a shape tuple with only 3 elements (i.e. (k,n,m) )
# We introduced the concept of another layer represented by n


# Array Indexing 
print (x)
print (x[0])      # 0th Layer
print (x[0,0])    # 0th Layer and 0th Row
print (x[0,0,0])  # 0th Layer and 0th Row and 0th Column



# Creating multi dimensional array 

# One Dimensional Array 
x = np.array( [1,2,3], ndmin = 1 )  # ndmin = 1
print (type(x))
print (x)

print(x.strides)
print (x.ndim )
print (x.shape )
print (x.dtype )
print (x[0])
print (type(x[0]))
# If we access on the zeroth location we would get 1


# Two Dimensional Array with only one row of data
x = np.array( [1,2,3] , ndmin = 2) 
print (type(x))
print (x)

print (x.strides)
print (x.ndim)
print (x.shape)
print (x.dtype)

# If we access on the zeroth location we would get the 1D array [1 2 3]
print (x[0])
print (type(x[0]))
print (x[0][0])
print (x[0,0])
print (type(x[0][0]))


# Three Dimensional Array with only one row of data 
x = np.array( [1,2,3] , ndmin = 3)
 
print (type(x))
print (x)

print (x.strides) # (24, 24, 8)
print (x.ndim)
print (x.shape)
print (x.dtype)
# If we access on the zeroth location we would get 2D array [[1 2 3]]
print (x[0])
print (type(x[0]))
print (x[0][0])
print (type(x[0][0]))
print(x[0][0][0])
print (type(x[0][0][0]))


"""
Array         Dimen     Shape
[1 2 3]         1       (3,)

[[1 2 3]]       2       (1,3)    1 row  3 col

[[[1 2 3]]]     3       (1,1,3)  1 layer 1 row  3 col

"""


# Numpy supports all data types likes bool, integer, float, complex etc.
# They are defined by the numpy.dtype class 

import numpy as np 

x = np.float32(1.0) 
print (x) 
print (type(x)) 
 

x = np.float64(1.0)
print (x) 
print (type(x)) 
 

x = np.int_([1,2,4]) 
print ( x )
print (type(x)) 
 
# complex will convert your data type into iota form or real and imagaionary expression iota = (-1)**1/2
x = np.array([1, 2, 3], dtype = complex) 
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)
print (x.strides)

print (x.itemsize)
print(x.size)
print (x.nbytes)




"""
There are a couple of mechanisms for creating arrays in NumPy:
 a. Conversion from other Python structures (e.g., lists, tuples).
 b. Built-in NumPy array creation (e.g., arange, ones, zeros, etc.).
 c. Reading arrays from disk, either from standard or custom formats 
     (e.g. reading from a CSV file).
"""
# Using the built in function arange 

# Arange function will generate array from 0 to size-1 
# arange is similar to range function but generates an array , 
# where in range gives you a list of elements

import numpy as np 

x = np.arange(20, dtype=np.uint8)
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)
print (x.itemsize)

# zeros(shape) -- creates an array filled with 0 values with the specified shape.
# The default dtype is float64.
import numpy as np 
x = np.zeros((3, 3, 3))
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)




# ones(shape) -- creates an array filled with 1 values. 

import numpy as np 
x = np.ones((3, 3, 3), dtype=np.int8 )
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)


# linspace() -- creates arrays with a specified number of elements, 
# and spaced equally between the specified beginning and end values.

import numpy as np 
x = np.linspace(1, 4, 10, dtype = np.float) # try with float16,float32,float64
print (x)
print (x.ndim)
print (x.shape)
print (x.dtype)
print (x.itemsize)


"""
Arrays Operations - Basic operations apply element-wise. 
The result is a new array with the resultant elements.
Operations like *= and += will modify the existing array.
"""

import numpy as np
a = np.arange(5) 
print (a)

b = np.arange(5) 
print(b)


x= np.array(list(zip(a,b)))
print (x) 
print (x.ndim)
print (x.shape)
print (x.dtype)

x = a + b
print (x) 

x = a - b
print (x)

x = a**3
print (x)
 
x = a>3
print (x)
 
x= 10*np.sin(a)
print (x) 

x = a*b
print (x)


"""
Color-image data for single image is typically stored in three dimensions. 
Each image is a three-dimensional array of (height, width, channels), 
where the channels are usually red, green, and blue (RGB) values. 
One 256x256 RGB images would have shape (256, 256, 3). 

(An extended representation is RGBA, where the A–alpha–denotes the level of opacity.)
One 256x256 ARGB images would have shape (256, 256, 4). 


Color-image data for multiple images is typically stored in four dimensions. 
A collection of images is then just (image_number, height, width, channels). 
One thousand 256x256 RGB images would have shape (1000, 256, 256, 3). 

"""
 

# What are images
import numpy as np
import matplotlib.pyplot as plt
random_image = np.random.random([50,50])
plt.imshow(random_image, cmap = 'gray')

print("Values min/max", random_image.min(), random_image.max())




#Scikit-image is a good library to start with image processing.
from skimage import io

                          # 220 x 147 ( width x height )
photo = io.imread('images/hawa_mahal.jpg')  
#photo = io.imread('images/hawa_mahal.jpg', as_gray=True)  

print(type(photo))
print (photo.dtype)
print (photo.itemsize)
print (photo.size) # 147x220x3 = 97020  ( height x width x channel )
print (photo.nbytes)

print (photo.ndim)
# height = 147, width = 220 , RBG/Color Channel = 3 
print (photo.shape)  # ( height x width x channel ) 
                     # ( layers x rows  x columns )

print (photo)

print("Values min/max", photo.min(), photo.max())


print(photo[0]) # first layer
print(photo[146]) # Last layer

print(photo[146][0]) # 0th row for the last layer

print(photo[146][0][0]) # RED Component of 0th row for the last layer


import matplotlib.pyplot as plt
plt.imshow (photo)


plt.imshow (photo[:,:,0])
plt.imshow (photo[:,:,1])
plt.imshow (photo[:,:,2])


# Reversed rows to get upside down image
plt.imshow(photo[::-1])


# Revered the columns so we got a mirrored image
plt.imshow(photo[:,::-1])

# Section of the photos
plt.imshow(photo[50:147, 150:220])

# halved the size of the image
plt.imshow(photo[::2,::2])


import numpy as np
                        # condition,True,False
photo_masked = np.where(photo>100, 255, 0)
plt.imshow(photo_masked)

# Converts landscape into portrait
plt.imshow(photo[:,:,0].T)


# Convert image to grayScale
from skimage.color import rgb2gray
grayscale = rgb2gray(photo)

print(grayscale)

import matplotlib.pyplot as plt
plt.imshow(grayscale, cmap=plt.cm.gray)




"""
3-channel RGB PIL Image to 3D NumPy array and back 
"""

from PIL import Image
import numpy as np

#Import an image
image = Image.open('images/hawa_mahal.jpg')

image
print(type(image))

arr = np.array(image)
 
arr
print(type(arr))

# Convert array to Image
img = Image.fromarray(arr)

img


# convert into gray-scale:
im = image.convert('L')

im


import numpy as np
im = np.array(im)

im




"""
learn how to use numpy to store and manipulate image data
"""
# use PIL to create (and display) an image

from PIL import Image
import numpy as np

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[128:256, 128:256] = [255, 0, 0]
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()



"""
Create an image from array 
"""

import numpy as np
import matplotlib.pyplot as plt
     
# Generate random array
width, height = 16,16
iMat = np.random.rand(width*height).reshape((width,height))
iMat
print(type(iMat))
print(iMat.ndim)
print(iMat.shape)

# Show it!
plt.imshow(iMat,'gray')
plt.show() 

# Save it
img = Image.fromarray(iMat, 'L') # RGB for color images 
img.save('rgb.png')
img.show()
    



# Importing the required module
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

img = np.ones((8, 8))

img = [
       [1, 1, 0, 0, 0, 0, 1, 1],
       [1, 0, 1, 1, 1, 1, 0, 1],
       [0, 1, 0, 1, 1, 0, 1, 0],
       [0, 1, 1, 1, 1, 1, 1, 0],
       [0, 1, 0, 1, 1, 0, 1, 0],
       [0, 1, 1, 0, 0, 1, 1, 0],
       [1, 0, 1, 1, 1, 1, 0, 1],
       [1, 1, 0, 0, 0, 0, 1, 1]
       ]

print(type(img))


plt.imshow(img, "gray")


img_file = Image.fromarray(img, "I")
img_file.save("Smile.png")
img_file.show()


""" 
Wap to create an  colored image using numpy array
"""

# Importing the numpy and matplotlib module
import numpy as np
import matplotlib.pyplot as plt

# Importing Pillow libraray for saving the numpy array as image
from PIL import Image

# Defining the color codes for creating the image
numpy_img = [
[(255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 255, 255)],
[(255, 255, 255), (255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0), (255, 255, 255)],
[(255, 0, 0), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255), (255, 0, 0)],
[(255, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 0, 0)],
[(255, 0, 0), (255, 255, 255), (0, 255, 0), (255, 255, 255), (255, 255, 255), (0, 255, 0), (255, 255, 255), (255, 0, 0)],
[(255, 0, 0), (255, 255, 255), (255, 255, 255), (0, 255, 0), (0, 255, 0), (255, 255, 255), (255, 255, 255), (255, 0, 0)],
[(255, 255, 255),(255,0,0),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,0,0),(255,255,255)],
[(255,255,255),(255,255,255),(255,0,0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 255, 255), (255, 255, 255)]
]

# Creating the image using .imshow
plt.imshow(np.array(numpy_img, dtype=np.uint8))

# Saving the numpy array as image
img_data = Image.fromarray(np.array(numpy_img,dtype=np.uint8), 'RGB')
img_data.save("colorsmile.png")
img_data.show()


"""
Code Challenges
Using skimage Library 
    Changing Format                 ( rgb2gray rgb2hsv)
    Resizing Images                 ( resize )
    Upscale / Downscale Images      ( rescale )
    Rotate by different angles      ( rotate )
    Horizontal and Vertical Flip    ( fliplr )
    Image Cropping                  ( )
    Altering Image Brightness       ( )
    Use Filters                     ( )


"""