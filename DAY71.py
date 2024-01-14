#hii all this is DAY71(14-01-2024) Today's topics is Write a program to count the occurrences of each word in a given string.


sen=input("Enter a string:")
words= sen.split()
d={}
for w in words:
    if w in d:
        d[w]+=1
    else:
        d[w]=1
for x in d.keys():
    print("%s occur %s times:"%(x,d[w]))
