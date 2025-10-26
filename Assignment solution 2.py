
dictionaryForElementsCounts = {}
listOfDuplicateElements = []
def findDuplicateElements(inputList):

    for element in inputList:
        if element in dictionaryForElementsCounts:
            dictionaryForElementsCounts[element] += 1
        else:
            dictionaryForElementsCounts[element] = 1

    # Add all the duplicate elements in the list ( which are having counts > 1 )
    for element, count in dictionaryForElementsCounts.items():
        if count > 1:
            listOfDuplicateElements.append(element)
    return listOfDuplicateElements

    # Calling and execute the function
inputList = [1, 2, 3, 1, 7, 3,4, 2, 5, 6]

ansList = findDuplicateElements(inputList)
print(ansList)