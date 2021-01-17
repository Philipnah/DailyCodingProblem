
import numpy

inputArray = [1, 2, 3, 4, 5]
#inputArray = [3, 2, 1]

outputArray = []

def WithoutDivision():
     # 'i' is also used in inputArray slicing so it has to be minimum 1,
     # otherwise the slicing loops around and gives two times the same array
     i = 1
     while i < len(inputArray) + 1:
          combiSlice = inputArray[:i-1] + inputArray[i:]
          print(combiSlice)

          product = 1
          n = 0 
          while n < len(combiSlice):
               product = product * combiSlice[n]
               n += 1

          outputArray.append(product)
          i += 1


def Division():
     i = 0
     while i < len(inputArray):
          product = 1
          n = 0 
          while n < len(inputArray):
               product = product * inputArray[n]
               n += 1
          outputArray.append(product/inputArray[i])
          i += 1
     


WithoutDivision()

if len(inputArray) != len(outputArray):
     print("Error! input and output don't have the same lenght!")
else:
     print("\nArray length is " + str(len(outputArray)) + "\ninputArray was: " + str(inputArray) + "\noutputArray is: " + str(outputArray))