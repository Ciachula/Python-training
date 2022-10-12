#Question1
print("Hello, world!")
Hello, world!

#Question2
print("3+4")
3+4

print(3+4)
7

#Question4
# Create variables
num_years = 4
days_per_year = 365 
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)

126144000


# TODO: Set the value of the births_per_min variable
births_per_min = 250

# TODO: Set the value of the births_per_day variable
births_per_day = births_per_min * mins_per_hour * hours_per_day
360000

#Question5
# Load the data from the titanic competition
import pandas as pd
titanic_data = pd.read_csv("../input/titanic/train.csv")





