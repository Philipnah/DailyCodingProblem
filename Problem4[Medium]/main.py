searchQuery = input("Query: ")

stringArray = ["dog", "deer", "deal"]

cut = len(searchQuery)

cutArray = []
i = 0
while i < len(stringArray):
     cutArray.append(stringArray[i][:cut])
     i += 1

response = []
i = 0
while i < len(cutArray):
     if searchQuery == cutArray[i]:
          response.append(stringArray[i])
     i += 1

print(response)