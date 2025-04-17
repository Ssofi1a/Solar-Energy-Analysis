import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sunlight_data = {
    'Վայոց ձոր': [53.9, 67.2, 85.5, 106.4, 120.0, 113.3, 84.8],
    'Տավուշ': [48.6, 58.8, 75.5, 95.0, 106.0, 100.8, 75.2],
    'Լոռի': [38.4, 47.6, 61.4, 76.0, 84.0, 78.7, 60.8],
    'Շիրակ': [30.6, 38.5, 50.6, 63.7, 70.0, 65.3, 49.6],
    'Գեղարքունիք': [35.3, 44.1, 57.3, 70.3, 78.0, 73.9, 57.6]
}

months = ['Մարտ', 'Ապրիլ', 'Մայիս', 'Հունիս', 'Հուլիս', 'Օգոստոս', 'Սեպտեմբեր']
df = pd.DataFrame(sunlight_data, index=months)

def calculate_solar_output(region, area, efficiency):
    monthly_output = df[region] * area * efficiency
    yearly_output = monthly_output.sum()
    best_months = monthly_output.sort_values(ascending=False).head(3)
    return monthly_output, yearly_output, best_months

region = input("Մուտքագրեք մարզի անունը (օր. ՝ Վայոց ձոր, Տավուշ, Լոռի, Շիրակ, Գեղարքունիք): ")
area = float(input("Մուտքագրեք արևային պանելների մակերեսը (մ²): \n"))
efficiency = 0.2

monthly_output, yearly_output, best_months = calculate_solar_output(region, area, efficiency)

print(f"Տարեկան ընդհանուր արտադրություն ({region}): {yearly_output:.1f} կՎտ*ժ\n")
print("Առավել նպատակահարմար ամիսներ:")
print(best_months)

plt.figure(figsize=(10, 5))
monthly_output.plot(kind='bar', color='orange')
plt.title(f'{region} մարզի արևային արտադրություն ամսեկան (կՎտ*ժ)')
plt.ylabel('կՎտ*ժ')
plt.xlabel('Ամիսներ')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()