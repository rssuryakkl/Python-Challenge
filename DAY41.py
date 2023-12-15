#hii all this is DAY41(15-12-2023) Today's Topic is Print the sum of the current number and the previous number

# Printing current and previous number sum in a range(10)
# Initialize the first number
previous_number = 0
kk=int(input())
# Loop through the range and print the sum of current and previous numbers
for current_number in range(kk):
    total = current_number + previous_number
    print(f"Current Number {current_number} Previous Number {previous_number} Sum: {total}")
    previous_number = current_number  # Update previous_number for the next iteration
