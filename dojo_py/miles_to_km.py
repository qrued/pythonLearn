# Convert miles to killometers
# Km = 1.6 * miles


def miles_km(miles):
    km = 1.6 * (miles)
    return km


dist_miles = float(input("Enter distance in miles: "))
km = miles_km(dist_miles)
print(km)
