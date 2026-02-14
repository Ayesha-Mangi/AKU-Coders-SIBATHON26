# energy_calculator.py

def bill_score_calc(monthly_bill, max_bill=500000):
    """
    Continuous bill score: higher bill → lower score
    """
    score = max(0, 100 - (monthly_bill / max_bill) * 100)
    return round(score, 2)


def energy_score(ac_hours, light_hours, monthly_bill, rooms, lab_hours=0, lab_computers=0):
    """
    Calculate overall energy efficiency score (0–100)
    Weighted system:
    AC usage = 30%
    Light usage = 20%
    Bill factor = 20%
    Room efficiency = 20%
    Lab usage = 10%
    """

    # ---- 1️⃣ AC Usage Score (30%) ----
    ideal_ac_hours = 6
    ac_score = 100 - max((ac_hours - ideal_ac_hours) * 8, 0)
    ac_score = max(min(ac_score, 100), 0)

    # ---- 2️⃣ Light Usage Score (20%) ----
    ideal_light_hours = 8
    light_score = 100 - max((light_hours - ideal_light_hours) * 5, 0)
    light_score = max(min(light_score, 100), 0)

    # ---- 3️⃣ Electricity Bill Factor (20%) ----
    bill_score = bill_score_calc(monthly_bill)

    # ---- 4️⃣ Room Efficiency Factor (20%) ----
    if rooms == 0:
        room_score = 0
    else:
        bill_per_room = monthly_bill / rooms
        # Continuous scaling
        room_score = max(0, 100 - (bill_per_room / 10000) * 100)

    # ---- 5️⃣ Lab Usage Factor (10%) ----
    lab_score = max(0, 100 - (lab_hours * lab_computers * 0.5))  # 0.5 penalty per computer-hour

    # ---- Final Weighted Score ----
    final_score = (
        ac_score * 0.3 +
        light_score * 0.2 +
        bill_score * 0.2 +
        room_score * 0.2 +
        lab_score * 0.1
    )

    return {
        "Final Score": round(final_score, 2),
        "AC Score": round(ac_score, 2),
        "Light Score": round(light_score, 2),
        "Bill Score": round(bill_score, 2),
        "Room Score": round(room_score, 2),
        "Lab Score": round(lab_score, 2)
    }


def waste_percentage(score):
    """
    Waste is inverse of efficiency
    """
    waste = 100 - score
    return round(waste, 2)


def carbon_emission(ac_hours, light_hours, lab_hours, lab_computers, rooms):
    """
    Estimate CO₂ emissions based on electricity usage in kWh.
    Assumptions:
    - AC: 1.5 kWh per room per hour
    - Light: 0.5 kWh per room per hour
    - Lab computers: 0.2 kWh per computer per hour
    - 1 kWh ≈ 0.92 kg CO₂ (Pakistan electricity avg)
    """
    days_per_month = 30

    ac_energy = rooms * 1.5 * ac_hours * days_per_month
    light_energy = rooms * 0.5 * light_hours * days_per_month
    lab_energy = lab_computers * 0.2 * lab_hours * days_per_month

    total_kwh = ac_energy + light_energy + lab_energy
    emission_kg = total_kwh * 0.92
    emission_tons = emission_kg / 1000

    return round(emission_kg, 2), round(emission_tons, 3)




#
# def energy_score(ac_hours, light_hours, monthly_bill, rooms):
#     """
#     Calculate overall energy efficiency score (0–100)
#     Using weighted system:
#     AC usage = 40%
#     Light usage = 20%
#     Bill factor = 20%
#     Room efficiency = 20%
#     """
#
#     # ---- 1️⃣ AC Usage Score (40%) ----
#     ideal_ac_hours = 6
#     ac_score = 100 - max((ac_hours - ideal_ac_hours) * 8, 0)
#     ac_score = max(min(ac_score, 100), 0)
#
#     # ---- 2️⃣ Light Usage Score (20%) ----
#     ideal_light_hours = 8
#     light_score = 100 - max((light_hours - ideal_light_hours) * 5, 0)
#     light_score = max(min(light_score, 100), 0)
#
#     # ---- 3️⃣ Electricity Bill Factor (20%) ----
#     # Higher bill = lower score
#     if monthly_bill <= 100000:
#         bill_score = 100
#     elif monthly_bill <= 300000:
#         bill_score = 70
#     else:
#         bill_score = 40
#
#     # ---- 4️⃣ Room Efficiency Factor (20%) ----
#     if rooms == 0:
#         room_score = 0
#     else:
#         bill_per_room = monthly_bill / rooms
#
#         if bill_per_room <= 3000:
#             room_score = 100
#         elif bill_per_room <= 6000:
#             room_score = 70
#         else:
#             room_score = 40
#
#     # ---- Final Weighted Score ----
#     final_score = (
#         ac_score * 0.4 +
#         light_score * 0.2 +
#         bill_score * 0.2 +
#         room_score * 0.2
#     )
#
#     return round(final_score, 2)
#
#
# def waste_percentage(score):
#     """
#     Waste is inverse of efficiency
#     """
#     waste = 100 - score
#     return round(waste, 2)
#
#
# def carbon_emission(monthly_bill):
#     """
#     Estimate CO₂ emissions based on electricity usage.
#     Assume:
#     1 PKR ≈ 0.0025 kg CO₂ (approx estimation)
#     """
#
#     emission_kg = monthly_bill * 0.0025
#     emission_tons = emission_kg / 1000
#
#     return round(emission_kg, 2), round(emission_tons, 3)
#
