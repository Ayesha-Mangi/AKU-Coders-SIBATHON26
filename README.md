# AKU-Coders-SIBATHON26
# 🌍 EcoCampus – Smart Energy Hub

**EcoCampus** is an AI-powered energy management platform designed to help universities, colleges, and campuses reduce energy wastage, optimize electricity usage, and promote sustainable practices. This project is a **prototype** demonstrating key energy analysis, carbon emission estimation, and solar energy potential calculations.

---

## 📝 Problem Statement

Many campuses face **high electricity bills** and **energy inefficiencies** due to excessive usage of ACs, lights, computer labs, and other appliances. Currently, there is **no simple system** that:

- Analyzes energy consumption  
- Provides actionable recommendations  
- Estimates renewable energy (solar) benefits  

This leads to unnecessary **financial costs** and **carbon emissions**, impacting both budgets and the environment.

---

## 💡 Proposed Solution

EcoCampus is a **prototype platform** that:

1. Allows users to input campus energy data:  
   - Monthly electricity bill, AC & light usage hours, number of rooms, lab computers, campus size  
2. Calculates **Energy Efficiency Score** and **Waste Percentage**  
3. Estimates **CO₂ emissions** and **annual impact**  
4. Provides **AI-driven recommendations** to reduce energy waste  
5. Calculates **solar energy potential**, payback period, and 10-year savings  

All results are presented on an **interactive Streamlit dashboard** with visualizations and eco badges.

---

## 🏗 Technical Architecture

**Frontend (User Interface)**  
- Streamlit web dashboard for easy, interactive input and results  

**Backend Logic (Python Modules)**  
- `energy_calculator.py` → Energy efficiency scoring & CO₂ calculations  
- `solar_calculator.py` → Solar potential & savings analysis  
- `ai_suggestions.py` → Smart recommendations  

**Visualization Layer**  
- Matplotlib charts (Pie, Line)  
- Eco badges indicating energy status  

**Data Flow:**  
User Input → Backend Processing → Calculations → Dashboard Visualization → AI Insights  

---

## ⚡ Features

- 🖥 User-friendly interactive dashboard  
- 📊 Real-time energy efficiency scoring  
- 🌱 CO₂ emissions & trees required to offset  
- 🌞 10-year solar energy savings and payback projection  
- 🤖 AI-based suggestions for energy optimization  

---

## 🌍 Impact

- Reduces campus electricity consumption  
- Lowers energy bills  
- Promotes sustainable behavior and eco-friendly practices  
- Encourages solar and renewable energy adoption  

---

## 🚀 Future Scope

- Integration with **Smart Meters (IoT Devices)**  
- Cloud-based real-time energy monitoring  
- Predictive AI for peak energy consumption  
- Mobile application for facility managers  
- Multi-campus scalability  
- Renewable energy grid integration  

---

## 🛠 Technology Stack

| Layer        | Technology                    |
|-------------|-------------------------------|
| Frontend    | Streamlit                     |
| Backend     | Python (energy_calc, solar_calc, AI tips) |
| Visualization | Matplotlib                  |
| Database    | Optional: CSV / MySQL         |
| AI / Analytics | Rule-based Python logic / OpenAI API |

---
