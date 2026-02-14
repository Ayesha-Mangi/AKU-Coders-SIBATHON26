
def energy_score(ac_hours, light_hours, monthly_bill, rooms):
    """
    Calculate overall energy efficiency score (0–100)
    Using weighted system:
    AC usage = 40%
    Light usage = 20%
    Bill factor = 20%
    Room efficiency = 20%
    """

    # ---- 1️⃣ AC Usage Score (40%) ----
    ideal_ac_hours = 6
    ac_score = 100 - max((ac_hours - ideal_ac_hours) * 8, 0)
    ac_score = max(min(ac_score, 100), 0)

    # ---- 2️⃣ Light Usage Score (20%) ----
    ideal_light_hours = 8
    light_score = 100 - max((light_hours - ideal_light_hours) * 5, 0)
    light_score = max(min(light_score, 100), 0)

    # ---- 3️⃣ Electricity Bill Factor (20%) ----
    # Higher bill = lower score
    if monthly_bill <= 100000:
        bill_score = 100
    elif monthly_bill <= 300000:
        bill_score = 70
    else:
        bill_score = 40

    # ---- 4️⃣ Room Efficiency Factor (20%) ----
    if rooms == 0:
        room_score = 0
    else:
        bill_per_room = monthly_bill / rooms

        if bill_per_room <= 3000:
            room_score = 100
        elif bill_per_room <= 6000:
            room_score = 70
        else:
            room_score = 40

    # ---- Final Weighted Score ----
    final_score = (
        ac_score * 0.4 +
        light_score * 0.2 +
        bill_score * 0.2 +
        room_score * 0.2
    )

    return round(final_score, 2)


def waste_percentage(score):
    """
    Waste is inverse of efficiency
    """
    waste = 100 - score
    return round(waste, 2)


def carbon_emission(monthly_bill):
    """
    Estimate CO₂ emissions based on electricity usage.
    Assume:
    1 PKR ≈ 0.0025 kg CO₂ (approx estimation)
    """

    emission_kg = monthly_bill * 0.0025
    emission_tons = emission_kg / 1000

    return round(emission_kg, 2), round(emission_tons, 3)

