def findRent(start,end):
 # yours codes goes here:
    if start < 0 or end < 0 or start > 24 or end > 24:
        return "Invalid input: Times must be between 0 and 24."
    
    if start > end:
        return "Invalid input: Starting time cannot be greater than ending time."
    
    total_cost = 0
    current_time = start

    while current_time < end:
        if (0 <= current_time < 7) or (21 <= current_time < 24):
            rate = 500
        elif (7 <= current_time < 10) or (19 <= current_time < 21):
            rate = 1000
        else:
            rate = 1500
        
        total_cost += rate
        current_time += 1

    return f"Total amount to be paid: RWF {total_cost}"


start=int(input("Enter start time:"))
end=int(input("Enter end time:"))
print(findRent(start,end))
