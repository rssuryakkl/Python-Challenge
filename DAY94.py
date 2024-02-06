#Hii all this is DAY94(06-02-2024) Today's topic is Inverted Pyramid of Numbers

rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
