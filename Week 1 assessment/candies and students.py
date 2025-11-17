#distribute candies and students
candies=int(input("Enter number of candies:"))
students=int(input("Enter number of students:"))

noofcandiestostudents=candies //students
noofcandiesremain= candies%students
print("The number of candies each studnet will get:",noofcandiestostudents,"candies")
print(f"he number of candies remain from {candies} candies:",noofcandiesremain,"candies")