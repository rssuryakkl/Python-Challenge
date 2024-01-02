#Hii all This is DAY59(02-01-2024) today topic is cinima theaterto check seat are filled or not 

def print_seating_arr(total_Seats,Occupancy_percentage):
    occupied_seats=int(total_Seats*Occupancy_percentage/100)

    for seat_number in range(1,total_Seats+1):
        if seat_number<=occupied_seats:
            print(f"The seat is {seat_number}: Occupied")
        else:
            print(f"The Seat is {seat_number}: is free")
            
total_Seats=100
Occupancy_percentage=75
print(print_seating_arr(total_Seats,Occupancy_percentage))
