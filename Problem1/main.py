k = int(input("k: "))

array = [10,2,3,6,18]

fulfilled = False

i = 0
while i < len(array):
     if k-array[i] in array:
          fulfilled = True
     i += 1

if fulfilled == True:
     print("True")
else:
     print("False")