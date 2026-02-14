def generate_suggestions(score, waste):
    tips = []

    if score < 70:
        tips.append("Reduce AC usage by 1–2 hours daily to improve efficiency.")

    if waste > 15:
        tips.append("Switch to LED lighting to reduce energy waste.")

    if score < 50:
        tips.append("Conduct an energy audit to identify major energy leaks.")

    tips.append("Consider installing solar panels for long-term cost savings.")
    tips.append("Encourage students and staff to follow energy-saving practices.")

    return tips