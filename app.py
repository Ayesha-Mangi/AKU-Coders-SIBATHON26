import streamlit as st
from energy_calculator import energy_score, waste_percentage, carbon_emission
from solar_calculator import solar_estimate
from ai_suggestions import generate_suggestions
import matplotlib.pyplot as plt

st.set_page_config(page_title="EcoCampus", layout="wide")

# ---------------- UI THEME (ONLY UI – NO LOGIC CHANGED) ----------------

st.markdown("""
<style>

.stApp{
    background-color:#f4e6d8;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background-color:#3a1f12;
}
section[data-testid="stSidebar"] *{
    color:#f7ede4;
}

/* 🔥 Sidebar input values darker (ONLY CHANGE ADDED) */
section[data-testid="stSidebar"] input,
section[data-testid="stSidebar"] textarea{
    color:#2b160c !important;
    font-weight:600 !important;
    background-color:#fffaf5 !important;
}

section[data-testid="stSidebar"] input::placeholder{
    color:#5a3a2a !important;
    opacity:1 !important;
}

/* Header */
.header-box{
    background:#ffffff;
    padding:18px 25px;
    border-radius:18px;
    box-shadow:0 6px 14px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

/* Cards */
.card{
    background:white;
    padding:18px;
    border-radius:16px;
    box-shadow:0 6px 14px rgba(0,0,0,0.08);
    margin-bottom:18px;
}

/* Buttons */
.stButton>button{
    background:#7b4a2e;
    color:white;
    border:none;
    border-radius:10px;
    padding:8px 18px;
}
.stButton>button:hover{
    background:#5c3320;
}

h1,h2,h3{
    color:#3a1f12;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

st.sidebar.header("📥 Campus Inputs")

bill = st.sidebar.number_input("Monthly Electricity Bill (PKR)", min_value=0.0)
rooms = st.sidebar.number_input("Number of Rooms", min_value=1)
monthly_units = st.sidebar.number_input("Monthly Electricity Units (kWh)", min_value=0.0)
ac_hours = st.sidebar.slider("AC Usage Hours per Day", 0, 24, 6)
light_hours = st.sidebar.slider("Light Usage Hours per Day", 0, 24, 8)
campus_size = st.sidebar.number_input("Campus Size (sq ft)", min_value=0.0)
lab_computers = st.sidebar.number_input("Number of Computers in Labs", min_value=0)
lab_hours = st.sidebar.slider("Computer Lab Usage Hours per Day", 0, 24, 6)


# ---------------- TOP HEADER ----------------

st.markdown("""
<div class="header-box">
<h1>🌍 EcoCampus – Smart Energy Optimizer</h1>
<p>Analyze campus energy efficiency and get smart sustainability insights.</p>
</div>
""", unsafe_allow_html=True)


# ---------------- MAIN ACTION ----------------

if st.button("🚀 Analyze Energy"):

    score_data = energy_score(ac_hours, light_hours, bill, rooms, lab_hours, lab_computers)
    score = score_data["Final Score"]
    waste = waste_percentage(score)
    emission_kg, emission_tons = carbon_emission(
        ac_hours, light_hours, lab_hours, lab_computers, rooms
    )

    solar_results = solar_estimate(
        campus_size=campus_size,
        monthly_bill=bill,
        monthly_units=monthly_units
    )

    tips = generate_suggestions(
        score, waste,
        ac_hours=ac_hours,
        light_hours=light_hours,
        lab_hours=lab_hours
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📊 Analysis", "⚡ Consumption", "🌞 Solar", "💡 AI Roadmap"]
    )

    # ---------------- TAB 1 ----------------

    with tab1:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("🏫 Campus Energy Metrics")
        c1, c2, c3 = st.columns(3)

        c1.metric("Energy Efficiency Score", f"{score}/100")
        c2.metric("Energy Waste", f"{waste}%")
        c3.metric("Monthly Carbon Emission", f"{emission_tons} tons CO₂")

        yearly_emission_kg = emission_kg * 12
        yearly_emission_tons = emission_tons * 12
        trees_needed = yearly_emission_kg / 21

        st.markdown("### 🌍 Annual Carbon Impact")

        t1, t2 = st.columns(2)
        t1.metric("Yearly CO₂ Emission", f"{round(yearly_emission_tons,2)} tons")
        t2.metric("Trees Required to Offset", f"{int(trees_needed)} 🌳")

        if score >= 80:
            st.success("🌿 Green Champion – Excellent Energy Management!")
        elif score >= 60:
            st.warning("🌱 Improving – Some optimizations needed.")
        else:
            st.error("⚠ Needs Improvement – High Energy Waste Detected.")

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- TAB 2 ----------------

    with tab2:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("⚡ Monthly Energy Consumption Breakdown")

        days_per_month = 30

        ac_energy = rooms * 1.5 * ac_hours * days_per_month
        light_energy = rooms * 0.5 * light_hours * days_per_month
        lab_energy = lab_computers * 0.2 * lab_hours * days_per_month
        other_energy = monthly_units * 0.15 if monthly_units > 0 else 0

        total_energy = ac_energy + light_energy + lab_energy + other_energy

        if total_energy > 0:

            labels = ["AC", "Lights", "Computer Labs", "Other"]
            values = [ac_energy, light_energy, lab_energy, other_energy]

            fig3, ax3 = plt.subplots()
            ax3.pie(
                values,
                labels=labels,
                autopct='%1.1f%%',
                colors=['#7b4a2e', '#c08a63', '#e2b48c', '#8f6a54']
            )
            ax3.set_title("Energy Distribution (kWh)")
            st.pyplot(fig3)

        else:
            st.warning("Enter usage data first.")

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- TAB 3 ----------------

    with tab3:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("🌞 Solar Energy Potential")

        s1, s2, s3 = st.columns(3)

        s1.metric("Solar Capacity", f"{solar_results['Solar Capacity (kW)']} kW")
        s2.metric("Yearly Savings", f"{solar_results['Yearly Savings (PKR)']} PKR")
        s3.metric("Payback Period", f"{solar_results['Payback Period (Years)']} Years")

        st.markdown("### 📈 Long-Term Solar Impact")

        st.write("🌿 CO₂ Reduction per Year:",
                 solar_results["CO2 Reduction (Tons/Year)"], "tons")
        st.write("💰 10-Year Profit:",
                 solar_results["10-Year Profit (PKR)"], "PKR")

        st.success(solar_results["Recommendation"])

        years = list(range(1, 11))
        yearly_savings = solar_results["Yearly Savings (PKR)"]
        cumulative = [yearly_savings * y for y in years]

        fig, ax = plt.subplots()
        ax.plot(years, cumulative, marker='o', color='#7b4a2e')
        ax.set_xlabel("Years")
        ax.set_ylabel("Cumulative Savings (PKR)")
        ax.set_title("10-Year Solar Savings Projection")
        ax.grid(True)

        st.pyplot(fig)

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- TAB 4 ----------------

    with tab4:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("💡 Smart Recommendations")

        for tip in tips:
            st.info(tip)

        st.markdown("</div>", unsafe_allow_html=True)
