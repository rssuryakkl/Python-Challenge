#hii all This is DAY38(12-12-2023) today's Topic is palin Drome
#palindrome mean by reading in forward and backward is known as palindrome
# function which return reverse of a string
def isPalindrome(s):
    return s == s[::-1]
# Driver code
s = input("Enter a Code:")
ans = isPalindrome(s)
if ans:
    print("Yes",s,"is a Palindrome")
else:
    print("No",s,"is Not a Palindrome")
