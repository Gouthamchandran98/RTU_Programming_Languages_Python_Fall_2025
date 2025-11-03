"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# Create the datasets
temperatures = [22.5, 21.0, 23.1, 19.8, 20.0, 24.3, 22.0]
city_population = {
    "Riga": 632000,
    "Daugavpils": 84000,
    "Liepaja": 70000,
    "Jelgava": 56000,
    "Jurmala": 49000,
}

# Compute aggregates
average_temperature = sum(temperatures) / len(temperatures) if temperatures else 0.0
total_population = sum(city_population.values()) if city_population else 0

if city_population:
    largest_city, largest_population = max(
        city_population.items(), key=lambda kv: kv[1]
    )
    smallest_city, smallest_population = min(
        city_population.items(), key=lambda kv: kv[1]
    )
else:
    largest_city = smallest_city = ""
    largest_population = smallest_population = 0

# Print results
print(f"Temperatures (week): {temperatures}")
print(f"Average temperature: {average_temperature:.2f}°C\n")

print("City populations:")
for city, pop in city_population.items():
    print(f" - {city}: {pop:,d}")

print()
print(f"Largest city: {largest_city} — {largest_population:,d}")
print(f"Smallest city: {smallest_city} — {smallest_population:,d}")
print(f"Total population: {total_population:,d}")
