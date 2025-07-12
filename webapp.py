import pandas as pd
import streamlit as st

url = "https://raw.githubusercontent.com/patilajinkya/niravana/refs/heads/main/nirvana_converted.csv"

df = pd.read_csv(url)


df = pd.DataFrame(df)

# App UI
st.title("🍹 Nirvana Menu")

# Dropdown for category
categories = df["Category"].unique()
selected_category = st.selectbox("Select a category", categories)

# Filter items
filtered_items = df[df["Category"] == selected_category]

# Subheader
st.subheader(f"Menu: {selected_category}", anchor=None, divider=True)

# Display items as cards
cols_per_row = 2
rows = [filtered_items.iloc[i:i + cols_per_row] for i in range(0, len(filtered_items), cols_per_row)]

for row_items in rows:
    cols = st.columns(len(row_items))
    for col, (_, item) in zip(cols, row_items.iterrows()):
        col.markdown(
            f"""
            <div style="
                background-color: #ffffff;
                border-radius: 12px;
                padding: 20px;
                margin-bottom: 16px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                color: black;
                text-align: center;
                font-family: 'Segoe UI', sans-serif;
            ">
                <h4 style="margin: 0 0 10px 0; font-size: 18px; color: black;">{item['Item']}</h4>
                <p style="margin: 0; font-size: 16px;"><strong>₹{item['Price']}</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )

