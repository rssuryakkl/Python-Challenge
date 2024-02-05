#Hii all This is DAY93(05-02-2024) Today's Topic is Write a program that reverse a list using a loop


def reverse_list(list1):
  reversed_list = []
  for i in range(len(list1) - 1, -1, -1):
    reversed_list.append(list1[i])
  return reversed_list


list1 = list(input("Enter a number:"))
print(reverse_list(list1))
