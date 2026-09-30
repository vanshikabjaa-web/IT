import streamlit as st

st.set_page_config(page_title="Income Tax Calculator", page_icon="💰", layout="centered")

st.title("💰 Income Tax Calculator (India)")
st.write("Calculate your income tax under the New Tax Regime.")

# User Inputs
st.header("Enter Your Details")

income = st.number_input(
    "Annual Income (₹)",
    min_value=0,
    max_value=100000000,
    value=800000,
    step=10000
)

# Tax Calculation Function
def calculate_tax(income):
    tax = 0

    if income <= 400000:
        tax = 0
    elif income <= 800000:
        tax = (income - 400000) * 0.05
    elif income <= 1200000:
        tax = 20000 + (income - 800000) * 0.10
    elif income <= 1600000:
        tax = 60000 + (income - 1200000) * 0.15
    elif income <= 2000000:
        tax = 120000 + (income - 1600000) * 0.20
    elif income <= 2400000:
        tax = 200000 + (income - 2000000) * 0.25
    else:
        tax = 300000 + (income - 2400000) * 0.30

    return max(tax, 0)

# Calculate Button
if st.button("Calculate Tax"):
    tax = calculate_tax(income)
    cess = tax * 0.04
    total_tax = tax + cess
    net_income = income - total_tax

    st.success("Calculation Complete!")

    st.subheader("📊 Tax Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Annual Income", f"₹{income:,.0f}")
        st.metric("Income Tax", f"₹{tax:,.0f}")

    with col2:
        st.metric("Health & Education Cess", f"₹{cess:,.0f}")
        st.metric("Net Income", f"₹{net_income:,.0f}")

    st.divider()

    st.subheader("Tax Slabs Used")

    st.table({
        "Income Range": [
            "₹0 – ₹4,00,000",
            "₹4,00,001 – ₹8,00,000",
            "₹8,00,001 – ₹12,00,000",
            "₹12,00,001 – ₹16,00,000",
            "₹16,00,001 – ₹20,00,000",
            "₹20,00,001 – ₹24,00,000",
            "Above ₹24,00,000"
        ],
        "Rate": ["0%", "5%", "10%", "15%", "20%", "25%", "30%"]
    })

st.caption("Note: This is a simplified calculator based on the New Tax Regime slab rates and includes 4% cess.")