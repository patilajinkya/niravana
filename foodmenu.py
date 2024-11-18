import streamlit as st

# Title
st.markdown(
    """
    <style>
    body {
        background-image: url('data:image/jpg;base64,{image}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .menu-item {
        display: flex;
        justify-content: space-between;
        font-size: 18px;
        font-weight: bold;
        color: white;
        text-shadow: 1px 1px 2px black;
    }
    .menu-section {
        padding: 15px;
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

import base64

# Load and encode the background image
with open("tomato-sauce-on-black-background-2024-10-16-12-43-51-utc.jpg", "rb") as file:
    image = base64.b64encode(file.read()).decode()

# Menu data
menu = {
    "Breakfast": {
        "Aloo Paratha": 100,
        "Bread Omlet": 90,
        "Masala Omlet": 70,
        "Plain Maggie": 80,
        "Veg Maggie": 110,
        "Egg Maggie": 130,
        "Veg Sandwich": 140,
    },
    "Appetizers": {
        "Veg Pakoda": 120,
        "Methi Pakoda": 120,
        "Paneer Pakoda": 170,
        "French Fries": 150,
        "Honey Chilli Potato": 240,
        "Chilli Potato": 220,
        "Potato Wedges": 200,
        "Chicken Pakoda": 300,
        "Chilli Chicken": 350,
        "Chicken Nuggets": 250,
    },
    "Beverages": {
        "Coffee": 70,
        "Black Coffee": 50,
        "Tea": 40,
        "Black Tea": 30,
        "Lemon/Honey Tea": 50,
        "Mint Tea": 50,
        "Lemon Water": 70,
        "Lemon Soda": 100,
        "Cappuccino": 100,
    },
    "Main Course": {
        "Kadai Chicken": 360,
        "Chicken Curry": 350,
        "Rara Chicken": 340,
        "Butter Chicken": 390,
        "Mughlai Chicken": 410,
        "Egg Curry": 150,
        "Egg Burji": 130,
    },
    "Roti & Rice": {
        "Tawa Roti": 15,
        "Butter Roti": 20,
        "Plain Rice": 100,
        "Jeera Rice": 130,
        "Veg Fried Rice": 170,
        "Egg Fried Rice": 190,
        "Chicken Fried Rice": 210,
    },
    "Veg Main Course": {
        "Dal Fry": 150,
        "Dal Tadka": 160,
        "Dal Makkani": 200,
        "Rajma": 170,
        "Dum Aloo": 150,
        "Aloo Mattar": 160,
        "Aloo Gobhi": 160,
        "Mixed Veg": 180,
        "Kadai Paneer": 240,
        "Mattar Paneer": 240,
        "Paneer Butter Masala": 270,
    }
}

# Dropdown for menu selection
section = st.selectbox("Select Menu Section", list(menu.keys()))

# Display selected section with markdown
st.markdown(f"<div class='menu-section'>", unsafe_allow_html=True)
st.subheader(section)
for item, price in menu[section].items():
    st.markdown(
        f"<div class='menu-item'><span>{item}</span><span>₹{price}</span></div>",
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.write("---")
st.markdown("<p style='color: white; text-shadow: 1px 1px 2px black;'>**Nirvana by Oztel, Kasol**</p>", unsafe_allow_html=True)
st.markdown("<p style='color: white; text-shadow: 1px 1px 2px black;'>📞 858 057 4937</p>", unsafe_allow_html=True)
