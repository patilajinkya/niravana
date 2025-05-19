import streamlit as st

st.set_page_config(page_title="Nirvana Cafe", layout="wide")

# ---------- Initialize session state for cart ----------
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Title
st.title("Nirvana Cafe Menu")

# Menu data
menu = {
    "Beverages": {
        "Milk Tea": 50, "Black Tea": 40, "Lemon Tea": 70, "Ginger Lemon Honey": 100,
        "Mint Tea": 50, "Milk Coffee": 70, "Black Coffee": 50, "Cappuccino": 100,
        "Cold Coffee": 130, "Frappe": 190, "Sweet/Salted Lassi": 100, "Lemon Water": 70,
        "Lemon Soda": 100, "Lemonade": 80, "Banana Shake": 130, "Oreo Shake": 200,
        "Kitkat Shake": 200, "Club Soda": 30, "Soft Drink 750 ML": 60, "Water Bottle 1L": 30
    },
    "Soups": {
        "Tomato Soup": 150, "Veg Manchow Soup": 150, "Sweet Corn": 150,
        "Veg Clear soup": 160, "Chicken Clear Soup": 220, "Chicken Manchow Soup": 230
    },
    "Breakfast": {
        "Masala Omlet": 90, "Bread Omlet": 100, "Mushroom Omlette": 160,
        "Cheese Omlet": 150, "Eggs (Boiled/Scrambled/Fried)": 110, "Poha": 130,
        "Butter Toast": 80, "French Toast": 110, "Nutella Toast": 150, "Plain Maggie": 80,
        "Masala Maggie": 100, "Cheese Maggie": 140, "Veg Maggie": 110, "Egg Maggie": 130,
        "Garlic bread": 150, "Aloo Paratha": 100, "Pyaz Paratha": 100, "Gobhi Paratha": 130,
        "Egg Paratha": 130, "Panner Paratha": 160, "Poori Bhaji": 180,
        "Hash Potatoes w/Toast and Coffee/Tea": 250, "Full English Breakfast": 400,
        "More Breakfast Options in South Indian": None
    },
    "Appetizers": {
        "Peanut Masala": 140, "Veg Pakoda": 190, "Paneer Pakoda": 340, "Chilli Paneer": 350,
        "Cheese Nachoes": 190, "Chilli Chicken": 410, "Chicken 65": 420, "Garlic Chicken": 410,
        "Pepper Chicken": 440, "Chicken Pakoda": 440, "Chicken Nuggets": 270, "BBQ Wings": 450,
        "French Fries": 150, "Piri Piri French Fries": 180, "Cheese French Fries": 200,
        "Potato Wedges": 190, "Chilli Potatoes": 280, "Honey Chilli Potato": 290,
        "Masala Papad": 130, "Veg Momos (Steamed)": 150, "Chicken Momos (Steamed)": 200
    },
    "Sandwich": {
        "Veg Club Sandwich": 200, "Veg Cheese Grilled Sandwich": 220,
        "Chicken Club Sandwich": 280, "Bombay Sandwich": 200, "Chilli Cheese Toast": 110,
        "Paneer Tikka Sandwich": 240, "Peri Peri Chicken Sandwich": 290,
        "Grilled Chicken Sandwich": 280, "Garlic Chicken Mayo Sandwich": 290
    },
    "Main Course (Veg)": {
        "Dal Fry": 170, "Dal Tadka": 190, "Dal Makkani": 220, "Rajma": 200,
        "Dum Aloo": 180, "Aloo Mattar": 190, "Aloo Gobhi": 190, "Aloo Jeera": 180,
        "Mixed veg": 220, "Kadai Paneer": 290, "Mattar Paneer": 290,
        "Panner Butter Masala": 300, "Kaju Paneer": 340
    },
    "Main Course (Non Veg)": {
        "Kadai Chicken": 460, "Chicken Curry": 460, "Rara Chicken": 480,
        "Butter Chicken": 520, "Mughlai Chicken": 540, "Kaju Chicken": 550,
        "Egg Curry": 200, "Egg Burji": 180
    },
    "Roti": {
        "Tawa Roti": 20, "Butter Roti": 25
    },
    "Rice and Noodles": {
        "Plain Rice": 120, "Jeera Rice": 150, "Veg Fried Rice": 180, "Egg Fried Rice": 200,
        "Chicken Fried Rice": 220, "Veg Noodles": 180, "Egg Noodles": 200, "Chicken Noodles": 220
    },
    "South Indian": {
        "Idli (2 Pcs)": 100, "Dosa": 150, "Onion Dosa": 170, "Masala Dosa": 180,
        "Egg Dosa": 200, "Uthappam": 150, "Mysore Bonda": 100, "Medu Vada": 130,
        "Ponganalu (6 Pcs)": 120, "Upma Suji": 120, "Upma Broken Rice": 130,
        "Vermecelli Upma": 150, "Lemon Rice": 200, "Tamarind Rice (Pulihora)": 190,
        "Mango Dal": 210, "Curd Rice": 180, "Sambar Rice": 260, "Rasam Rice": 210,
        "Dal rasam Rice": 220, "Aloo Fry": 200, "Punugulu Curry": 250,
        "Guttu Vankay": 240, "Kaju Chicken Pakodi": 450, "Andhra Chicken Fry": 460
    },
    "Biryanis": {
        "Bagara Rice & Chicken Curry": 500, "Bagara Rice & Chicken Fry": 500,
        "Bagara Rice & Aloo Fry": 400, "Chicken Dum Biryani": 550,
        "Mutton Dum Biryani": 650, "Andhra Chicken Biryani": 490
    },
    "Dessert": {
        "Ghee Bobattu (2 Pieces)": 200, "Semiya Payasam (Verimiceli Keer)": 190,
        "Gulab Jamun (4 Pieces)": 180, "Double ka meeta": 250
    },
    "Extras": {
        "Plain Mayo": 20, "Extra Cheese": 25, "Bbq Dip": 30, "Thousand Island": 30,
        "Chipotle Southwest": 30, "Mint Mayo": 30, "Peri Peri Sauce": 30,
        "Sweet Chilli": 30, "Siracha": 30
    }
}

st.title("Nirvana Cafe Menu")

section = st.selectbox("Select Menu Section", list(menu.keys()))
st.subheader(section)

for item, price in menu[section].items():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**{item}** — ₹{price}")
    with col2:
        qty_key = f"{item}_qty"
        qty = st.number_input("Qty", min_value=0, max_value=10, key=qty_key)
        if st.button("Add to Cart", key=f"add_{item}"):
            if qty > 0:
                if item in st.session_state.cart:
                    st.session_state.cart[item]["quantity"] += qty
                else:
                    st.session_state.cart[item] = {"price": price, "quantity": qty}
                st.success(f"Added {qty} x {item} to cart")
            else:
                st.warning("Please select a quantity greater than 0")

# ---------- Cart and Order Section ----------
st.markdown("---")
st.header("🛒 Your Cart")

if st.session_state.cart:
    total = 0
    for item, details in st.session_state.cart.items():
        item_total = details["price"] * details["quantity"]
        st.write(f"{item} — {details['quantity']} x ₹{details['price']} = ₹{item_total}")
        total += item_total
    st.markdown(f"### Total: ₹{total}")

    st.subheader("Enter Your Details")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    address = st.text_area("Delivery Address")

    if st.button("Place Order"):
        if name and email and phone and address:
            st.success("✅ Order placed successfully!")
            st.write("**Order Summary:**")
            for item, details in st.session_state.cart.items():
                st.write(f"{item} x {details['quantity']} = ₹{details['price'] * details['quantity']}")
            st.write(f"**Total: ₹{total}**")
            st.write(f"**Name:** {name}")
            st.write(f"**Email:** {email}")
            st.write(f"**Phone:** {phone}")
            st.write(f"**Address:** {address}")
            # Clear cart after placing order
            st.session_state.cart.clear()
        else:
            st.warning("Please fill all your details before placing the order.")
else:
    st.info("Your cart is empty.")

# ---------- Footer ----------
st.write("---")
st.write("📍 Nirvana by Oztel, Kasol")
st.write("📞 858 057 4937")
