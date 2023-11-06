#we are going to see a example on 5subject mark average
#Hii all this is DAY9

#(iii) Nested if..elif...else statement:

tamil=int(input("Enter a Tamil Mark:"))
english=int(input("Enter a English Mark:"))
maths=int(input("Enter a Maths Mark:"))
science=int(input("Enter a Science Mark:"))
social=int(input("Enter a Social Mark:"))

average=(tamil+english+maths+science+social)/5
print("Average is:",average)

if average>=80:
    print("Grade A")
elif average>=70 and average <80:
    print("Grade B")
elif average>=60 and average<70:
    print("Grade C")
elif average>=50 and average<60:
    print("Grade D")
else:
    print("Grade E")


#example task on check weather a given letter is vowels or not

vowels=input("Enter a letter to check weather vowels or not:")    
if vowels in ('a','i','o','u','e','A','E','I','O','U'):
    print("Enter letter ",vowels,"is vowels ")
else:
    print("Not a Vowels")
