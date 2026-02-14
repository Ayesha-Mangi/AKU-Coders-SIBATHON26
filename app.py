import streamlit as st
from energy_calculator import energy_score, waste_percentage, carbon_emission
from solar_calculator import solar_estimate
from ai_suggestions import generate_suggestions
import matplotlib.pyplot as plt

st.set_page_config(page_title="EcoCampus", layout="wide")

st.title("🌍 EcoCampus – Smart Energy Optimizer")
st.markdown("Analyze campus energy efficiency and get smart sustainability insights.")

st.divider()

# ---------------- INPUT SECTION ----------------
st.header("📥 Enter Campus Energy Data")

col1, col2 = st.columns(2)

with col1:
    bill = st.number_input("Monthly Electricity Bill (PKR)", min_value=0.0)
    rooms = st.number_input("Number of Rooms", min_value=1)
    monthly_units = st.number_input("Monthly Electricity Units (kWh)", min_value=0.0)

with col2:
    ac_hours = st.slider("AC Usage Hours per Day", 0, 24, 6)
    light_hours = st.slider("Light Usage Hours per Day", 0, 24, 8)
    campus_size = st.number_input("Campus Size (sq ft)", min_value=0.0)

st.divider()

# ---------------- ANALYSIS SECTION ----------------
if st.button("🚀 Analyze Energy"):

    # ---- ENERGY CALCULATIONS ----
    score = energy_score(ac_hours, light_hours, bill, rooms)
    waste = waste_percentage(score)
    emission_kg, emission_tons = carbon_emission(bill)

    # ---- SOLAR CALCULATIONS (UPDATED MODULE) ----
    solar_results = solar_estimate(
        campus_size=campus_size,
        monthly_bill=bill,
        monthly_units=monthly_units
    )

    tips = generate_suggestions(score, waste)

    st.header("📊 Energy Analysis Results")

    # ---- METRICS ROW ----
    m1, m2, m3 = st.columns(3)
    m1.metric("Energy Efficiency Score", f"{score}/100")
    m2.metric("Energy Waste", f"{waste}%")
    m3.metric("Carbon Emission", f"{emission_tons} tons CO₂")

    st.divider()

    # ---- ECO BADGE SYSTEM ----
    st.subheader("🏅 Eco Status")

    if score >= 80:
        st.success("🌿 Green Champion – Excellent Energy Management!")
    elif score >= 60:
        st.warning("🌱 Improving – Some optimizations needed.")
    else:
        st.error("⚠ Needs Improvement – High Energy Waste Detected.")

    st.divider()

    # ---- SOLAR SECTION ----
    st.subheader("🌞 Solar Energy Potential")

    s1, s2, s3 = st.columns(3)
    s1.metric("Solar Capacity", f"{solar_results['Solar Capacity (kW)']} kW")
    s2.metric("Yearly Savings", f"{solar_results['Yearly Savings (PKR)']} PKR")
    s3.metric("Payback Period", f"{solar_results['Payback Period (Years)']} Years")

    st.divider()

    # ---- ADDITIONAL SOLAR INSIGHTS ----
    st.subheader("📈 Long-Term Solar Impact")

    st.write("🌿 CO₂ Reduction per Year:",
             solar_results["CO2 Reduction (Tons/Year)"], "tons")

    st.write("💰 10-Year Profit Projection:",
             solar_results["10-Year Profit (PKR)"], "PKR")

    st.success(f"🔎 Recommendation: {solar_results['Recommendation']}")

    # ---- 10 Year Savings Graph ----
    years = list(range(1, 11))
    yearly_savings = solar_results["Yearly Savings (PKR)"]
    cumulative = [yearly_savings * y for y in years]

    fig, ax = plt.subplots()
    ax.plot(years, cumulative)
    ax.set_xlabel("Years")
    ax.set_ylabel("Cumulative Savings (PKR)")
    ax.set_title("10-Year Solar Savings Projection")
    st.pyplot(fig)

    st.divider()

    # ---- AI SUGGESTIONS ----
    st.subheader("💡 Smart Recommendations")

    for tip in tips:
        st.info(tip)

