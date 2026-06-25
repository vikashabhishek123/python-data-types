# """
# This is a demo file for numpy series in python.
# here we learn about indexing and slicing of numpy series. 

# array[index] #1d array
# array[rows , columns] #2d array

# """
# #here we learn about indexing of numpy series.
# import numpy as np
# # arr =np.array([44,67,34,24,67])
# # print(arr[-1]) #last element
# # print(arr[0]) #first element


# #here we learn about slicing of numpy series.
# arr =np.array([45,67,34,24,67])
# # print(arr[0:3]) #slicing from index 0 to 2
# # print(arr[0:4]) #slicing from index 0 to 3
# # print(arr[:: 2]) #slicing from index 0 to end with step size of 2
# # print(arr[::-1]) #slicing from index 0 to end with step size of -1 (reverse order)

# #fancy indexing of numpy series.
# # arr = np.array([45,67,34,24,67])
# # print(arr[[0,2,4]]) #fancy indexing using list of indices

# #filtering of numpy series or boolean masking of numpy series.
# arr = np.array([45,67,34,24,67])
# print(arr[arr>40]) #filtering the elements greater than 40
# print(arr[arr==67]) #filtering the elements equal to 67

# print(arr[arr!=67]) #filtering the elements not equal to 67

