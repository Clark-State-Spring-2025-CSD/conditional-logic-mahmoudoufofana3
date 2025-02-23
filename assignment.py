#Updated 1 Feb 2025
#Create a program that will ask the user for a number between 1 and 12. You may assume the input is correct.
#After getting the number display which season it is. The ranges are:
#Spring: 3,4,5
#Summer: 6,7,8
#Fall: 9,10,11
#Winter 12,1,2
#Here is a sample output:
#What month is it? (1-12): 2
#The current season is Winter.
#For an extra 2 points, display the month as all. So the output becomes:
#What month is it? (1-12): 2
#The month is February and the current season is Winter.
#Remember to also complete the flowchart. It is strongly advised that you do the flowchart first,
#as this will help you write the code.
# Dictionary to map month numbers to month names
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# Ask the user for a number between 1 and 12
month_num = int(input("What month is it? (1-12): "))

# Determine the season based on the month number
if month_num in [3, 4, 5]:
    season = "Spring"
elif month_num in [6, 7, 8]:
    season = "Summer"
elif month_num in [9, 10, 11]:
    season = "Fall"
else:
    season = "Winter"

# Display the month and season
print(f"The month is {months[month_num]} and the current season is {season}.")