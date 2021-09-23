"""
CP1404 - Practical 08
Taxi Test
"""

from prac_08.taxi import Taxi

# 1. Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km

prius = Taxi("Prius 1", 100, 1.23)

# 2. Drive the taxi 40 km

prius.drive(40)

# 3. Print the taxi's details and the current fare

print(prius)
print(f"Current fare: ${prius.get_fare():.2f}")

# 4. Restart the meter (start a new fare) and then drive the car 100 km

prius.start_fare()
prius.drive(100)

# 5. Print the details and the current fare

print(prius)
print(f"Current fare: ${prius.get_fare():.2f}")
