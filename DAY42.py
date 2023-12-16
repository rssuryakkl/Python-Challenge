#hii all this is DAY42(16-12-2023) Reverse the string

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
s =input("Enter a String:")
print("The original string is : ", end="")
print(s)
print("The reversed string is : ", end="")
print(reverse(s))
