#Hii all This is DAY61(04-01-2023) Today's task is Write a program that prints the maximum value and minimum value  in a Tuple.


t = (25, 17, 55, 63, 40)
max_val = t[0]
for i in range(len(t)):
    if t[i] > max_val:
        max_val = t[i]
print("Maximum value is:", max_val)

#minimum value  in a Tuple.
t = (25, 17, 55, 63, 40)
max_val = t[0]
for i in range(len(t)):
    if t[i] < max_val:
        max_val = t[i]
print("Maximum value is:", max_val)
