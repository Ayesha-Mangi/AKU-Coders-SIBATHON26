def generate_suggestions(score, waste, ac_hours=None, light_hours=None, lab_hours=None):
    """
    Generate smart rule-based improvement roadmap based on benchmark gaps.
    Optional: pass current AC, Light, Lab hours for benchmark comparison.
    """
    tips = []

    # ---- Basic efficiency tips ----
    if score < 70:
        tips.append("Reduce AC usage by 1–2 hours daily to improve efficiency.")

    if waste > 15:
        tips.append("Switch to LED lighting to reduce energy waste.")

    if score < 50:
        tips.append("Conduct an energy audit to identify major energy leaks.")

    tips.append("Consider installing solar panels for long-term cost savings.")
    tips.append("Encourage students and staff to follow energy-saving practices.")

    # ---- Benchmark-based roadmap ----
    IDEAL_AC_HOURS = 6
    IDEAL_LIGHT_HOURS = 8
    IDEAL_LAB_HOURS = 6

    if ac_hours is not None and ac_hours > IDEAL_AC_HOURS:
        tips.append(f"🌿 Reduce AC usage by {ac_hours - IDEAL_AC_HOURS} hour(s) per day to meet sustainable benchmark.")

    if light_hours is not None and light_hours > IDEAL_LIGHT_HOURS:
        tips.append(f"🌱 Reduce lighting usage by {light_hours - IDEAL_LIGHT_HOURS} hour(s) per day to meet benchmark.")

    if lab_hours is not None and lab_hours > IDEAL_LAB_HOURS:
        tips.append(f"💻 Limit computer lab usage by {lab_hours - IDEAL_LAB_HOURS} hour(s) per day for efficiency.")

    return tips

#
# def generate_suggestions(score, waste):
#     tips = []
#
#     if score < 70:
#         tips.append("Reduce AC usage by 1–2 hours daily to improve efficiency.")
#
#     if waste > 15:
#         tips.append("Switch to LED lighting to reduce energy waste.")
#
#     if score < 50:
#         tips.append("Conduct an energy audit to identify major energy leaks.")
#
#     tips.append("Consider installing solar panels for long-term cost savings.")
#     tips.append("Encourage students and staff to follow energy-saving practices.")
#
#     return tips