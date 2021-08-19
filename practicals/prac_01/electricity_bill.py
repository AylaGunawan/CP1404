"""
CP1404 - Practical 01
Electricity Bill Estimator (Practice)
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
# cents_per_kwh = int(input("Enter cents per kWh: ")) * 0.01
chosen_tariff = int(input("Which tariff? 11 or 31: "))
while chosen_tariff != 11 and chosen_tariff != 31:
    print("Invalid tariff")
    chosen_tariff = int(input("Which tariff? 11 or 31: "))
if chosen_tariff == 11:
    cents_per_kwh = TARIFF_11
else:
    cents_per_kwh = TARIFF_31
daily_use_in_kwh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))

estimated_bill = (daily_use_in_kwh * cents_per_kwh) * number_of_billing_days
print(f"Estimated bill: ${estimated_bill:.2f}")
