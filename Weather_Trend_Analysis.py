import os
import pandas as pd
import matplotlib.pyplot as plt

# Set project folder as working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create graphs folder if it does not exist
os.makedirs("graphs", exist_ok=True)

# Load dataset
data = pd.read_csv("dataset/weather trend analysis.csv")

print("====================================")
print(" WEATHER TREND ANALYSIS ON AQI")
print(" OF DIFFERENT CITIES IN INDIA")
print("====================================")

# Display dataset information
print("\nFirst Five Records:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Remove duplicate records
data = data.drop_duplicates()

print("\nDuplicates Removed Successfully!")

# Calculate overall average AQI
average_aqi = data["AQI"].mean()

print("\nOverall Average AQI:", average_aqi)

# Calculate city-wise average AQI
city_aqi = data.groupby("city")["AQI"].mean()

print("\nAvailable Cities:")
print(city_aqi.index.tolist())

# USER INPUT
city_name = input("\nEnter a city name: ")

# Search for selected city
if city_name.lower() in city_aqi.index.str.lower():

    selected_city = city_aqi[
        city_aqi.index.str.lower() == city_name.lower()
    ]

    print("\nCity Found!")
    print("City Name:", selected_city.index[0])
    print("Average AQI:", round(selected_city.iloc[0], 2))

else:
    print("\nSorry! City not found in dataset.")

# Create one city-wise AQI graph
plt.figure(figsize=(12, 6))

city_aqi.plot(kind="bar")

plt.title("Average AQI of Different Cities")
plt.xlabel("Cities")
plt.ylabel("Average AQI")

plt.xticks(rotation=45)
plt.tight_layout()

# Save graph
plt.savefig("graphs/city_wise_aqi.png")

print("\nGraph saved successfully!")

plt.show()

print("\nPROJECT COMPLETED SUCCESSFULLY!")
