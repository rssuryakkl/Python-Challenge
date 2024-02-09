#Hii all This is DAY97(09-02-2024)Today's Topic is Program to create an Abecedarian series. (Abecedarian refers list of elements appear in alphabetical order)


str1="ABCDEFGH"
str2="ate"
for i in str1:
    print ((i+str2),end='\t')


def rem_vowels(s):
    temp_str=''
    for i in s:
        if i in "aAeEiIoOuU":
            pass
        else:
            temp_str+=i
    print ("The string without vowels: ", temp_str)
str1= input ("Enter a String: ")
rem_vowels (str1)














