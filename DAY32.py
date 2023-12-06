#hii all this is DAY32(06-12-2023) today's topic is Dictionaries
MyDict = { 'Reg_No': '1221',
           'Name' : 'Tamilselvi',
           'School' : 'CGHSS',
           'Address' : 'Rotler St., Chennai 112' }
print(MyDict)

MyDict = { 'Reg_No': '1221',
           'Name' : 'Tamilselvi',
           'School' : 'CGHSS',
           'Address' : 'Rotler St., Chennai 112' }
print("Name of the Student is :",MyDict['Name'])
print("Name of School",MyDict['School'])

#add new in dict
MyDict['Class'] = 'XII - A' # Adding new value
print("Class: ", MyDict['Class']) # Printing newly added value
print(MyDict)

#deleting the dict
# Deleting a particular element
del MyDict['Class'] 
print(MyDict)

# Deleting all elements
MyDict.clear() 
print(MyDict)

