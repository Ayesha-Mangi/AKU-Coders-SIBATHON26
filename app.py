import streamlit as st
from energy_calculator import energy_score, waste_percentage, carbon_emission
from solar_calculator import solar_estimate
from ai_suggestions import generate_suggestions
import matplotlib.pyplot as plt

st.set_page_config(page_title="EcoCampus", layout="wide")

# ---------------- SIDEBAR INPUTS ----------------
st.sidebar.header("📥 Enter Campus Energy Data")
bill = st.sidebar.number_input("Monthly Electricity Bill (PKR)", min_value=0.0)
rooms = st.sidebar.number_input("Number of Rooms", min_value=1)
monthly_units = st.sidebar.number_input("Monthly Electricity Units (kWh)", min_value=0.0)
ac_hours = st.sidebar.slider("AC Usage Hours per Day", 0, 24, 6)
light_hours = st.sidebar.slider("Light Usage Hours per Day", 0, 24, 8)
campus_size = st.sidebar.number_input("Campus Size (sq ft)", min_value=0.0)
lab_computers = st.sidebar.number_input("Number of Computers in Labs", min_value=0)
lab_hours = st.sidebar.slider("Computer Lab Usage Hours per Day", 0, 24, 6)

st.title("🌍 EcoCampus – Smart Energy Optimizer")
st.markdown("Analyze campus energy efficiency and get smart sustainability insights.")

if st.button("🚀 Analyze Energy"):

    # ---- ENERGY CALCULATIONS ----
    score_data = energy_score(ac_hours, light_hours, bill, rooms, lab_hours, lab_computers)
    score = score_data["Final Score"]
    waste = waste_percentage(score)
    emission_kg, emission_tons = carbon_emission(ac_hours, light_hours, lab_hours, lab_computers, rooms)

    # ---- SOLAR CALCULATIONS ----
    solar_results = solar_estimate(
        campus_size=campus_size,
        monthly_bill=bill,
        monthly_units=monthly_units
    )

    # ---- AI SUGGESTIONS ----
    tips = generate_suggestions(score, waste, ac_hours=ac_hours, light_hours=light_hours, lab_hours=lab_hours)

    # ---- TABS FOR PROFESSIONAL GUI ----
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Analysis", "⚡ Consumption", "🌞 Solar", "💡 AI Roadmap"])

    # ---------------- TAB 1: ANALYSIS ----------------
    with tab1:
        st.subheader("🏫 Campus Energy Metrics")
        c1, c2, c3 = st.columns(3)
        c1.metric("Energy Efficiency Score", f"{score}/100", delta="Higher is better 🌿")
        c2.metric("Energy Waste", f"{waste}%", delta="Lower is better ⚠")
        c3.metric("Monthly Carbon Emission", f"{emission_tons} tons CO₂", delta="Lower is better 🌱")

        # Annual Carbon + Trees
        yearly_emission_kg = emission_kg * 12
        yearly_emission_tons = emission_tons * 12
        trees_needed = yearly_emission_kg / 21

        st.markdown("### 🌍 Annual Carbon Impact")
        t1, t2 = st.columns(2)
        t1.metric("Yearly CO₂ Emission", f"{round(yearly_emission_tons, 2)} tons")
        t2.metric("Trees Required to Offset", f"{int(trees_needed)} Trees 🌳")
        st.info("📌 Approximation: 1 mature tree absorbs ~21 kg CO₂/year.")

        # Eco Badge
        st.subheader("🏅 Eco Status")
        if score >= 80:
            st.success("🌿 Green Champion – Excellent Energy Management!")
        elif score >= 60:
            st.warning("🌱 Improving – Some optimizations needed.")
        else:
            st.error("⚠ Needs Improvement – High Energy Waste Detected.")

    # ---------------- TAB 2: CONSUMPTION ----------------
    with tab2:
        st.subheader("⚡ Estimated Monthly Energy Consumption Breakdown")
        days_per_month = 30

        ac_energy = rooms * 1.5 * ac_hours * days_per_month
        light_energy = rooms * 0.5 * light_hours * days_per_month
        lab_energy = lab_computers * 0.2 * lab_hours * days_per_month
        other_energy = monthly_units * 0.15 if monthly_units > 0 else 0

        total_energy = ac_energy + light_energy + lab_energy + other_energy

        if total_energy > 0:
            labels = ["AC", "Lights", "Computer Labs", "Other Appliances"]
            values = [ac_energy, light_energy, lab_energy, other_energy]

            fig3, ax3 = plt.subplots()
            ax3.pie(values, labels=labels, autopct='%1.1f%%',
                    colors=['#4CAF50','#81C784','#FFB74D','#90A4AE'],
                    explode=[0.1,0,0,0])
            ax3.set_title("Estimated Monthly Energy Consumption Distribution (kWh)")
            st.pyplot(fig3)
            st.caption("📌 Energy values estimated using standard appliance power ratings.")
        else:
            st.warning("Enter electricity usage data to see consumption breakdown.")

    # ---------------- TAB 3: SOLAR ----------------
    with tab3:
        st.subheader("🌞 Solar Energy Potential")
        s1, s2, s3 = st.columns(3)
        s1.metric("Solar Capacity", f"{solar_results['Solar Capacity (kW)']} kW")
        s2.metric("Yearly Savings", f"{solar_results['Yearly Savings (PKR)']} PKR")
        s3.metric("Payback Period", f"{solar_results['Payback Period (Years)']} Years")

        st.markdown("### 📈 Long-Term Solar Impact")
        st.write("🌿 CO₂ Reduction per Year:", solar_results["CO2 Reduction (Tons/Year)"], "tons")
        st.write("💰 10-Year Profit Projection:", solar_results["10-Year Profit (PKR)"], "PKR")
        st.success(f"🔎 Recommendation: {solar_results['Recommendation']}")

        years = list(range(1, 11))
        yearly_savings = solar_results["Yearly Savings (PKR)"]
        cumulative = [yearly_savings * y for y in years]

        fig, ax = plt.subplots()
        ax.plot(years, cumulative, marker='o', color='#4CAF50')
        ax.set_xlabel("Years")
        ax.set_ylabel("Cumulative Savings (PKR)")
        ax.set_title("10-Year Solar Savings Projection")
        ax.grid(True)
        st.pyplot(fig)

    # ---------------- TAB 4: AI ROADMAP ----------------
    with tab4:
        st.subheader("💡 Smart Recommendations / Improvement Roadmap")
        for tip in tips:
            st.info(tip)


#
# import streamlit as st
# from energy_calculator import energy_score, waste_percentage, carbon_emission
# from solar_calculator import solar_estimate
# from ai_suggestions import generate_suggestions
# import matplotlib.pyplot as plt
#
# st.set_page_config(page_title="EcoCampus", layout="wide")
#
# st.title("🌍 EcoCampus – Smart Energy Optimizer")
# st.markdown("Analyze campus energy efficiency and get smart sustainability insights.")
#
# st.divider()
#
# # ---------------- INPUT SECTION ----------------
# st.header("📥 Enter Campus Energy Data")
#
# col1, col2 = st.columns(2)
#
# with col1:
#     bill = st.number_input("Monthly Electricity Bill (PKR)", min_value=0.0)
#     rooms = st.number_input("Number of Rooms", min_value=1)
#     monthly_units = st.number_input("Monthly Electricity Units (kWh)", min_value=0.0)
#
# with col2:
#     ac_hours = st.slider("AC Usage Hours per Day", 0, 24, 6)
#     light_hours = st.slider("Light Usage Hours per Day", 0, 24, 8)
#     campus_size = st.number_input("Campus Size (sq ft)", min_value=0.0)
#
# st.divider()
#
# # ---------------- ANALYSIS SECTION ----------------
# if st.button("🚀 Analyze Energy"):
#
#     # ---- ENERGY CALCULATIONS ----
#     score = energy_score(ac_hours, light_hours, bill, rooms)
#     waste = waste_percentage(score)
#     emission_kg, emission_tons = carbon_emission(bill)
#
#     # ---- SOLAR CALCULATIONS (UPDATED MODULE) ----
#     solar_results = solar_estimate(
#         campus_size=campus_size,
#         monthly_bill=bill,
#         monthly_units=monthly_units
#     )
#
#     tips = generate_suggestions(score, waste)
#
#     st.header("📊 Energy Analysis Results")
#
#     # ---- METRICS ROW ----
#     m1, m2, m3 = st.columns(3)
#     m1.metric("Energy Efficiency Score", f"{score}/100")
#     m2.metric("Energy Waste", f"{waste}%")
#     m3.metric("Carbon Emission", f"{emission_tons} tons CO₂")
#
#     st.divider()
#
#     # ---- ECO BADGE SYSTEM ----
#     st.subheader("🏅 Eco Status")
#
#     if score >= 80:
#         st.success("🌿 Green Champion – Excellent Energy Management!")
#     elif score >= 60:
#         st.warning("🌱 Improving – Some optimizations needed.")
#     else:
#         st.error("⚠ Needs Improvement – High Energy Waste Detected.")
#
#     st.divider()
#
#     # ---- SOLAR SECTION ----
#     st.subheader("🌞 Solar Energy Potential")
#
#     s1, s2, s3 = st.columns(3)
#     s1.metric("Solar Capacity", f"{solar_results['Solar Capacity (kW)']} kW")
#     s2.metric("Yearly Savings", f"{solar_results['Yearly Savings (PKR)']} PKR")
#     s3.metric("Payback Period", f"{solar_results['Payback Period (Years)']} Years")
#
#     st.divider()
#
#     # ---- ADDITIONAL SOLAR INSIGHTS ----
#     st.subheader("📈 Long-Term Solar Impact")
#
#     st.write("🌿 CO₂ Reduction per Year:",
#              solar_results["CO2 Reduction (Tons/Year)"], "tons")
#
#     st.write("💰 10-Year Profit Projection:",
#              solar_results["10-Year Profit (PKR)"], "PKR")
#
#     st.success(f"🔎 Recommendation: {solar_results['Recommendation']}")
#
#     # ---- 10 Year Savings Graph ----
#     years = list(range(1, 11))
#     yearly_savings = solar_results["Yearly Savings (PKR)"]
#     cumulative = [yearly_savings * y for y in years]
#
#     fig, ax = plt.subplots()
#     ax.plot(years, cumulative)
#     ax.set_xlabel("Years")
#     ax.set_ylabel("Cumulative Savings (PKR)")
#     ax.set_title("10-Year Solar Savings Projection")
#     st.pyplot(fig)
#
#     st.divider()
#
#     # ---- AI SUGGESTIONS ----
#     st.subheader("💡 Smart Recommendations")
#
#     for tip in tips:
#         st.info(tip)
#
