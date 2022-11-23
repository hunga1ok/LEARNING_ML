import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

classFile = ""

# while(classFile != 'c'): 
#     classFile = input('Enter a class file to grade (i.e. class1 for class1.txt): ')
#     try:
#         file = open(os.path.join(__location__, classFile))
#         print("Successfully opened " + classFile)
#         print("**** ANALYZING ****")
#         for line in file:
#             print(line)
#             listItem = line.split(',')
#             print(listItem.count)
#     except:
#         print("File cannot be found ")

pattern = re.compile("^N[0-9]{8}")


try:
    totalValidLine = 0
    totalInvalidLine = 0
    
    file = open(os.path.join(__location__, "class2.txt"))
    print("Successfully opened " + "class1.txt")
    print("**** ANALYZING ****")
    for line in file:
        analyzingResult = ""
        listItem = line.split(',')
        if len(listItem) != 26:
            print("Invalid line of data: does not contain exactly 26 values:\n" + line, end='')
            analyzingResult += "Invalid line of data: does not contain exactly 26 values:\n" + line
        elif len(listItem[0]) != 9 or (not pattern.match(listItem[0])) : 
            print("Invalid line of data: N# is invalid:\n" + line, end='')
            analyzingResult += "Invalid line of data: N# is invalid:\n" + line
        
        if len(analyzingResult) != 0 : totalInvalidLine += 1 
        else: totalValidLine += 1
    print("**** REPORT ****")
    print("Total valid lines of data: " + str(totalValidLine))
    print("Total invalid lines of data: " + str(totalInvalidLine))

except Exception:
    print("File cannot be found " + Exception)