#Hii all today this is DAY33(07-12-2023) today's topic is Hands on Experience  examples
#we have completed a half of a topic in python balance 40% there out of 100%

#1.Write a program to check whether the given character is a vowel or not.

vowels=input("Enter a Char:")
if(vowels=='A'or vowels== 'E' or vowels=='I' or vowels=='O'  or vowels=='U' or vowels=='a' or vowels=='e' or vowels=='i' or vowels=='o' or vowels=='u'):
    print("Enter Char is Vowels:",vowels)
else:
    print("Entered char is Not a vowels")

#2.Using if..else..elif statement check smallest of three numbers.
num1=int(input("Enter a Number1:"))
num2=int(input("Enter a Number2:"))
num3=int(input("Enter a Number3:"))
if(num1<num2  and num1<num3):
    small=num1
elif(num2<num1 and num2<num3):
    small=num2
else:
    small=num3
print(small,'this is smallest')

