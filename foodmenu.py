import streamlit as st

# Title
st.title("Nirvana Cafe Menu")

# Menu data
menu = {
    "Beverages": {
        "Milk Tea": 50,
        "Black Tea": 40,
        "Lemon Tea": 70,
        "Ginger Lemon Honey": 100,
        "Mint Tea": 50,
        "Milk Coffee": 70,
        "Black Coffee": 50,
        "Cappuccino": 100,
        "Sweet/Salted Lassi": 100,
        "Badam Milk": 100,
        "Detox Kahwa": 80,
        "Lemon Water": 70,
        "Lemon Soda": 100,
        "Cold Coffee": 130,
        "Banana Shake": 130,
        "Oreo Shake": 200,
        "Kitkat Shake": 200,
        "Lemonade": 80,
        "Soft Drink 750 ML": 60
        "Club Soda": 30
        
    },

    "Breakfast": {
        "Masala Omlet": 90,
        "Bread Omlet": 100,
        "Mushroom Omlette": 160,
        "Cheese Omlet": 150,
        "Eggs (Boiled/Scrambled/Fried)": 110,
        "French Toast": 110,
        "Poha": 130,
        "Butter Toast": 80,
        "Nutella Toast": 150,
        "Masala Maggie": 100,
        "Plain Maggie": 80,
        "Cheese Maggie": 140,
        "Veg Maggie": 110,
        "Egg Maggie": 130,
        "Garlic bread": 150,
        "Aloo Paratha": 100,
        "Pyaz Paratha": 100,
        "Gobhi Paratha": 130,
        "Egg Paratha": 130,
        "Panner Paratha": 160,
        "Poori Bhaji": 180,
        "Hash Potatoes with Toast and Coffee/Tea": 250
    },
    "Sandwich": {
        "Veg club Sandwich": 200,
        "Veg Cheese Grilled Sandwich": 220,
        "Bombay Masala Sandwich": 200,
        "Chicken club Sandwich": 280
       
    },
    "Soups": {
        "Tomato Soup": 150,
        "Veg Manchow Soup": 160,
        "Sweet Corn Soup": 150,
        "Chicken Soup": 220,
        "Chicken Manchow Soup": 230
    },
    "Appetizers": {
        "Masala Peanut": 140,
        "Chili Paneer": 350,
        "Chili Potatoes": 280,
        "Veg Pakoda": 190,
        "Cheese Nachoes": 190,
        "French Fries": 150,
        "Piri Piri French Fries": 180,
        "Cheese French Fries": 200,
        "Honey Chili Potato": 290,
        "Masala Papad": 130,
        "Veg Momos": 150,
        "Chicken Momos": 200,
        "Chili Chicken": 420,
        "Chicken Pakoda": 440,
        "Chicken Nuggets": 270
        
    },

    "Main Course (Veg)": {
        "Dal Fry": 170,
        "Dal Tadka": 190,
        "Dal Makhani": 220,
        "Rajma": 200,
        "Dum Aloo": 180,
        "Aloo Matar": 190,
        "Aloo Gobhi": 190,
        "Aloo Jeera": 180,
        "Mixed veg": 220,
        "Kadhai Paneer": 290,
        "Matar Paneer": 290,
        "Panner Butter Masala": 300,
        "Kaju Paneer": 340
    },
    "Main Course(Non Veg)": {
        "Kadhai Chicken": 460,
        "Chicken Curry": 460,
        "Rara Chicken": 480,
        "Butter Chicken": 520,
        "Mughlai Chicken": 540,
        "Kaju Chicken": 550,
        "Egg Curry": 200,
        "Egg Burji": 180
    },
    "Rice and Noodles": {
        "Plain Rice": 120,
        "Jeera Rice": 150,
        "Veg Fried Rice": 180,
        "Egg Fried Rice": 200,
        "Chicken Fried Rice": 220,
        "Veg Noodles": 180,
        "Egg Noodles": 200,
        "Chicken Noodles": 220
    },
    "Roti":{
        "Tawa Roti": 20,
        "Butter Roti": 25
    }
}


# Dropdown for menu selection
section = st.selectbox("Select Menu Section", list(menu.keys()))

# Display selected section with markdown
st.subheader(section)
for item, price in menu[section].items():
    st.markdown(f"<div style='display: flex; justify-content: space-between;'>"
                f"<span>{item}</span>"
                f"<span><b>₹{price}</b></span>"
                f"</div>", unsafe_allow_html=True)

# Footer
st.write("---")
st.write("**Nirvana by Oztel, Kasol**")
st.write("****")
st.write("📞 858 057 4937")

