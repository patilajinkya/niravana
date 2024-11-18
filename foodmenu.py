import streamlit as st

# Title
st.title("Nirvana Cafe Menu")

# Sidebar for navigation
menu_section = st.sidebar.radio("Select Menu Section", [
    "Breakfast",
    "Appetizers",
    "Beverages",
    "Main Course",
    "Roti & Rice",
    "Veg Main Course"
])

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

# Display menu items based on the selected section
st.subheader(f"{menu_section} Menu")
for item, price in menu[menu_section].items():
    st.write(f"{item} - ₹{price}")

# Footer
st.write("---")
st.write("**Nirvana by Oztel, Kasol**")
st.write("📞 858 057 4937")
