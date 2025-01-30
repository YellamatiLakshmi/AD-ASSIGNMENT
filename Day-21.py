# Find cab prediction price(y) byconsidering x value (no.of km traveled (20)) and rate per km is fixed one(m) as 2 and fixed price as that is fare is c value is 5
# Compare the prices of ola and uber which is low and by onsidering the below following things
# Y = MX + C
# Far price is 25 for ola
# No.of km raveled(20)
# Ola : Base price is 50
# Uber : Base price is 35
# Farprice : 50
    #Rate per km : $5 per km -> m


def calculate_fare(rate, km, base_fare):
    return rate * km + base_fare


ola_fare = calculate_fare(2, 20, 50)
uber_fare = calculate_fare(5, 20, 35)

print(f"Ola: ₹{ola_fare}, Uber: ₹{uber_fare}")
print("Ola is cheaper." if ola_fare < uber_fare else "Uber is cheaper.")
