import streamlit as st
from functions import calculate_savings, calculate_adjustment

# Initialize session state if not already done
if 'current_age' not in st.session_state:
    st.session_state['current_age'] = 30
if 'retirement_age' not in st.session_state:
    st.session_state['retirement_age'] = 62
if 'current_savings' not in st.session_state:
    st.session_state['current_savings'] = 5000
if 'annual_savings' not in st.session_state:
    st.session_state['annual_savings'] = 9000
if 'annual_return' not in st.session_state:
    st.session_state['annual_return'] = 11.0
if 'target_savings' not in st.session_state:
    st.session_state['target_savings'] = 2800000.0

# Streamlit UI
st.title("Retirement Calculator")

col1, col2 = st.columns(2)

with col1:
    st.session_state['current_age'] = st.number_input("Current Age:", min_value=1, max_value=90, value=st.session_state['current_age'])
    st.session_state['current_savings'] = st.number_input("Current Savings ($):", min_value=0, value=st.session_state['current_savings'], step=100)
    st.session_state['annual_savings'] = st.number_input("Savings Per Year ($):", min_value=0, value=st.session_state['annual_savings'], step=1000)

with col2:
    st.session_state['retirement_age'] = st.number_input("Retirement Age:", min_value=st.session_state['current_age'], max_value=100, value=st.session_state['retirement_age'])
    st.session_state['annual_return'] = st.number_input("Estimated Annual Return (%):", min_value=0.0, max_value=100.0, value=st.session_state['annual_return'], step=0.1)
    st.session_state['target_savings'] = st.number_input("Target Savings ($):", min_value=0.0, value=st.session_state['target_savings'], step=10000.0)

if st.button("Calculate"):
    estimated_savings = calculate_savings(
        st.session_state['current_age'],
        st.session_state['retirement_age'],
        st.session_state['current_savings'],
        st.session_state['annual_savings'],
        st.session_state['annual_return']
    )
    shortfall, suggestion = calculate_adjustment(
        st.session_state['target_savings'],
        estimated_savings,
        st.session_state['retirement_age'] - st.session_state['current_age'],
        st.session_state['annual_return']
    )

    st.subheader("Results")
    st.write(f"Years of work remaining: {st.session_state['retirement_age']-st.session_state['current_age']}")
    st.write(f"Estimated Savings at Retirement Age: ${estimated_savings:,.2f}")
    st.write(f"Shortfall or Overage: ${shortfall:,.2f}")
    st.write(f"Suggestion: {suggestion}")
