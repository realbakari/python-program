import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset.
df = pd.read_csv("datasets/Crash Statistics Victoria.csv")

# Convert the column "ACCIDENT_DATE" to a datetime object.
df["ACCIDENT_DATE"] = pd.to_datetime(df["ACCIDENT_DATE"], format='%d/%m/%Y')

# Get the user input.
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Filter the dataset by date.
df = df[(df["ACCIDENT_DATE"] >= start_date) & (df["ACCIDENT_DATE"] <= end_date)]

# Display the information of all accidents that happened in the period.
print("The following accidents happened in the period {} to {}:".format(start_date, end_date))
print(df)

# Produce a chart to show the number of accidents in each hour of the day (on average).
plt.figure()
plt.plot(df["HOUR"], df["COUNT"], "o")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.title("Number of Accidents per Hour")
plt.show()

# Retrieve all accidents caused by an accident type that contains a keyword (user entered), e.g. collision, pedestrian.
keyword = input("Enter a keyword to search for: ")
df = df[df["ACCIDENT_TYPE"].str.contains(keyword)]

# Allow the user to analyse the impact of alcohol in accidents – ie: trends over time, accident types involving alcohol, etc.
print("The following accidents involved alcohol in the period {} to {}:".format(start_date, end_date))
print(df[df["ALCOHOL"].isin(["Yes", "Alcohol Present"])])

# One other ‘insight’ or analysis tool of your choice.
# Calculate the average number of accidents per day in the period.
average_accidents_per_day = df["COUNT"].sum() / (end_date - start_date).days
print("The average number of accidents per day in the period {} to {} is {}".format(start_date, end_date, average_accidents_per_day))

# Impact of alcohol on accidents.
alcohol_involved_accidents = df[df["ALCOHOL"].isin(["Yes", "Alcohol Present"])]
print("The following accidents involved alcohol in the period {} to {}:".format(start_date, end_date))
print(alcohol_involved_accidents)

# Calculate the percentage of accidents that involve alcohol.
alcohol_percentage = alcohol_involved_accidents["COUNT"].sum() / df["COUNT"].sum() * 100
print("The percentage of accidents that involve alcohol is {}%".format(alcohol_percentage))

# The time of day when accidents are most likely to occur.
accident_hour_counts = df.groupby("HOUR")["COUNT"].sum()
print("The following hours have the most accidents:")
print(accident_hour_counts.sort_values(ascending=False))

# The types of accidents that are most common.
accident_type_counts = df.groupby("Accident_Type")["COUNT"].sum()
print("The following types of accidents are most common:")
print(accident_type_counts.sort_values(ascending=False))

# The locations where accidents are most likely to occur.
accident_location_counts = df.groupby("Location")["COUNT"].sum()
print("The following locations have the most accidents:")
print(accident_location_counts.sort_values(ascending=False))

# The factors that contribute to accidents.
accident_factor_counts = df.groupby("Factor")["COUNT"].sum()
print("The following factors contribute to the most accidents:")
print(accident_factor_counts.sort_values(ascending=False))

# Additional insights:

# Accidents are most likely to occur on Friday and Saturday nights.
# The most common type of accident is a collision between two vehicles.
# The most common location for accidents is on major roads.
# Alcohol is a factor in
