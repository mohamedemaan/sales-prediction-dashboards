# =========================
# IMPORT LIBRARIES
# =========================

import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Sales Prediction Dashboard",
    layout="wide"
)


# =========================
# LOAD MODEL
# =========================

model = pickle.load(open("sales_model.pkl", "rb"))


# =========================
# TITLE
# =========================

st.title("🔥 Sales Prediction Dashboard")


# =========================
# SIDEBAR
# =========================

st.sidebar.header("Enter Input Values")


feature1 = st.sidebar.number_input(
    "Feature 1",
    value=0.0
)

feature2 = st.sidebar.number_input(
    "Feature 2",
    value=0.0
)

feature3 = st.sidebar.number_input(
    "Feature 3",
    value=0.0
)


# =========================
# PREDICTION
# =========================

if st.sidebar.button("Predict Sales"):

    input_data = pd.DataFrame(
        [[feature1, feature2, feature3]]
    )

    prediction = model.predict(input_data)

    st.success(
        f"🔥 Predicted Sales: {prediction[0]}"
    )


# =========================
# SAMPLE CHART
# =========================

st.subheader("📊 Sample Sales Chart")

sample_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 150, 120, 180, 210]
})

fig, ax = plt.subplots()

ax.plot(
    sample_data["Month"],
    sample_data["Sales"]
)

ax.set_xlabel("Month")

ax.set_ylabel("Sales")

ax.set_title("Monthly Sales")

st.pyplot(fig)


# =========================
# METRICS
# =========================

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", "₹50K")

col2.metric("Growth", "12%")

col3.metric("Customers", "1,250")


# =========================
# FOOTER
# =========================

st.write("✅ AI Dashboard Created Using Streamlit")