#Convert minutes to hours and minutes
total_minutes=int(input("Enter total no of minutes:"))
no_of_min_in_one_hour=60
no_of_hours=total_minutes // 60
remaining_min=total_minutes % 60
print(f"{total_minutes} no of minutes will be equal to {no_of_hours} hours and {remaining_min} minutes")