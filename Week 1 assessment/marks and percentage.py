#program to calculate total marks and percentage
Total_number_of_subjects=5
Total_marks_of_each_sub=int(100)
Eng=int(input("Enter Obtain Marks in English:"))
Urdu=int(input("Enter Obtain MArks in Urdu:"))
Maths=int(input("Enter Obtain Marks in Maths:"))
Phy=int(input("Enter Obtain Marks in Physics:"))
Chem=int(input("Enter Obtain Marks in Chemistry:"))

Total_marks=Total_marks_of_each_sub*5
Total_obtained_marks=Eng+Urdu+Maths+Phy+Chem
print("Total Marks of all subjects:",Total_marks)
print ("Total Obtained Marks in all subjects:",Total_obtained_marks)

per=Total_obtained_marks/Total_marks*100
print("Percentage of Obtained marks:", per)

avg=Total_obtained_marks/Total_number_of_subjects
print("Average of all the subjects is:",avg)