# Convert the below list into numpy array then display tha array 
# input: my_list = [1,2,3,4,5]
import numpy as np 
my_list = [1,2,3,4,5]
arr = np.array(my_list)
print(arr)

# Convert the below list into a numpy array then display the 
# array then display the first and last index and then multiply
# each element by 2 and display the result
my_list = [1,2,3,4,5]
arr = np.array(my_list)

print(arr)

print("First element:", arr[0])
print("Last element:", arr[-1])

# Multiply each element by 2
multiplied_array = arr * 2

print("updated array :",multiplied_array)


# write a numpy program to create an array of 10 zeros,10 ones and 10 fives
ar = np.zeros((1,10))
print("An array of 10 zeros :",ar)
ar = np.ones((1,10))
print("An array of 10 ones :",ar)
ar = np.ones((1,10)) + 4
print("An array of 10 five :",ar)

# write a numpy program to create a 3x3 matrix with values 
# ranging from 2 to 10

arr = np.arange(2, 11)
matrix = arr.reshape(3, 3)

print("3x3 Matrix with values ranging from 2 to 10:")
print(matrix)