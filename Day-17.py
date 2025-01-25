import pandas as pd
import seaborn as sns

# dataset
data = {
    'Temperature' : [25, 28, 32, 35, 38, 40, 42, 45, 30, 33, 36, 37],
    'Ice Cream Sales' : [200, 250, 300, 350, 400, 420, 430, 450, 280, 310, 360, 370],
    'Advertising_Budget' : [50, 55, 60, 70, 75, 80, 85, 90, 60, 65, 70, 75],
    'Customer_Count' : [80, 100, 120, 140, 150, 160, 170, 180, 110, 130, 140, 145],
}

df = pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt

#pair plot
sns.pairplot(df, diag_kind = 'kde', markers = "o", plot_kws={'alpha' : 0.7})
plt.suptitle("Pair plot of Ice cream sales Data", y = 1.02, fontsize = 16)
plt.show()



# Example weather data 
data = {
    'Temperature': [22, 25, 28, 20, 18, 21, 19, 24, 32, 34, 35, 23, 15, 12, 14, 24, 20, 19, 18, 23, 18, 25, 28, 29],
    'Humidity': [65, 60, 72, 78, 80, 73, 72, 69, 75, 62, 68, 66, 71, 73, 70, 62, 65, 64, 63, 65],
    'Wind Speed': [15, 10, 20, 25, 12, 14, 18, 10, 12, 15, 8, 10, 12, 14, 10, 15, 8, 10],
    'Pressure': [1015, 1012, 1017, 1014, 1013, 1016, 1011, 1018, 1013, 1015, 1013]
}

# Create a DataFrame
df = pd.DataFrame(data)

# --- Scatter Plot ---
plt.figure(figsize=(8, 6))
plt.scatter(df['Temperature'], df['Humidity'], color='blue', label='Temp vs Humidity')

# Adding labels and title
plt.title("Temperature vs Humidity", fontsize=14)
plt.xlabel("Temperature (°C)", fontsize=12)
