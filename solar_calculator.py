def solar_estimate(
        campus_size,  # in square feet
        monthly_bill,  # in PKR
        monthly_units,  # electricity units consumed per month
        sell_rate=19,  # net metering sell rate per unit (PKR)
        maintenance_percent=0.02  # yearly maintenance cost %
):

    # ✅ Input safety
    campus_size = max(campus_size, 0)
    monthly_bill = max(monthly_bill, 0)
    monthly_units = max(monthly_units, 0)
    sell_rate = max(sell_rate, 0)
    maintenance_percent = max(maintenance_percent, 0)

    # 1️⃣ Solar Capacity Estimation
    solar_capacity = campus_size / 100  # 100 sq ft = 1 kW

    # Estimated monthly solar production (1 kW ≈ 120 units/month avg Pakistan)
    solar_units = solar_capacity * 120

    # 2️⃣ Bill Savings Percentage (basic logic kept same)
    savings_percent = min(solar_capacity * 0.8, 50)
    yearly_savings = (monthly_bill * (savings_percent / 100)) * 12

    # 3️⃣ Installation Cost (PKR)
    installation_cost = solar_capacity * 150000

    # 4️⃣ Maintenance Cost
    maintenance_cost = installation_cost * maintenance_percent
    net_yearly_savings = yearly_savings - maintenance_cost

    # 5️⃣ Net Metering Income
    extra_units = round(max(solar_units - monthly_units, 0), 2)
    net_metering_income = extra_units * sell_rate * 12

    total_yearly_benefit = net_yearly_savings + net_metering_income

    # 6️⃣ Payback Period (logic improvement)
    if total_yearly_benefit > 0:
        payback_period = installation_cost / total_yearly_benefit
    else:
        payback_period = None  # safer than 0

    # 7️⃣ CO₂ Reduction (tons per year approx)
    co2_reduction = solar_capacity * 1.5

    # 8️⃣ 10-Year Profit Projection
    profit_10_years = (total_yearly_benefit * 10) - installation_cost

    # 9️⃣ Smart Recommendation
    if solar_capacity < 10:
        recommendation = "Rooftop Solar System Recommended"
    elif solar_capacity < 50:
        recommendation = "On-Grid Commercial Solar System Recommended"
    else:
        recommendation = "Hybrid Large-Scale Solar System Recommended"

    return {
        "Solar Capacity (kW)": round(solar_capacity, 2),
        "Yearly Savings (PKR)": round(total_yearly_benefit, 2),
        "Payback Period (Years)": round(payback_period, 2) if payback_period else None,
        "CO2 Reduction (Tons/Year)": round(co2_reduction, 2),
        "10-Year Profit (PKR)": round(profit_10_years, 2),
        "Recommendation": recommendation
    }

