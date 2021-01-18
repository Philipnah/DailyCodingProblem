# first we sort the list
# if integer is <= 0 then slice it from the array
# loop count from the lowest found positive integer and test if it exists in the array


import numpy as np

inputArray = [3, 4, -1, 1]

print("\nInput array was: " + str(inputArray))

inputArray = np.sort(inputArray)

for i in inputArray:
     if i <= 0:
          inputArray = inputArray[1:]


answer = 0
try:
     answer = inputArray[0]
except:
     print("There is no answer for this array.")


# You could also just test if answer was in inputArray
n = 0
while n < len(inputArray):
     if answer != inputArray[n]:
          print("The missing number is: " + str(answer))
          break
     elif answer > len(inputArray) - 1:
          print("The missing number is: " + str(answer + 1))
          break
     else:
          answer += 1
          n += 1
