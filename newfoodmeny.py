import streamlit as st
import pandas as pd

# ---- CATEGORY-WISE DATA ---- #
menu = {
    "Beverages": [
        ("Milk Tea", 50), ("Black Tea", 40), ("Lemon Tea", 70), ("Ginger Lemon Honey", 100),
        ("Mint Tea", 50), ("Milk Coffee", 70), ("Black Coffee", 50), ("Cappuccino", 100),
        ("Cold Coffee", 130), ("Frappe", 190), ("Sweet/Salted Lassi", 100), ("Lemon Water", 70),
        ("Lemon Soda", 100), ("Lemonade", 80), ("Banana Shake", 130), ("Oreo Shake", 200),
        ("Kitkat Shake", 200), ("Club Soda", 30), ("Soft Drink 750 ML", 60), ("Water Bottle 1L", 30)
    ],
    "Soups": [
        ("Tomato Soup", 150), ("Veg Manchow Soup", 150), ("Sweet Corn", 150),
        ("Veg Clear soup", 160), ("Chicken Clear Soup", 220), ("Chicken Manchow Soup", 230)
    ],
    "Breakfast": [
        ("Masala Omlet", 90), ("Bread Omlet", 100), ("Mushroom Omlette", 160),
        ("Cheese Omlet", 150), ("Eggs (Boiled/Scrambled/Fried)", 110), ("Poha", 130),
        ("Butter Toast", 80), ("French Toast", 110), ("Nutella Toast", 150), ("Plain Maggie", 80),
        ("Masala Maggie", 100), ("Cheese Maggie", 140), ("Veg Maggie", 110), ("Egg Maggie", 130),
        ("Garlic bread", 150), ("Aloo Paratha", 100), ("Pyaz Paratha", 100), ("Gobhi Paratha", 130),
        ("Egg Paratha", 130), ("Panner Paratha", 160), ("Poori Bhaji", 180),
        ("Hash Potatoes w/Toast and Coffee/Tea", 250), ("Full English Breakfast", 400)
    ],
    "Appetizers": [
        ("Peanut Masala", 140), ("Veg Pakoda", 190), ("Paneer Pakoda", 340), ("Chilli Paneer", 350),
        ("Cheese Nachoes", 190), ("Chilli Chicken", 410), ("Chicken 65", 420), ("Garlic Chicken", 410),
        ("Pepper Chicken", 440), ("Chicken Pakoda", 440), ("Chicken Nuggets", 270), ("BBQ Wings", 450),
        ("French Fries", 150), ("Piri Piri French Fries", 180), ("Cheese French Fries", 200),
        ("Potato Wedges", 190), ("Chilli Potatoes", 280), ("Honey Chilli Potato", 290),
        ("Masala Papad", 130), ("Veg Momos (Steamed)", 150), ("Chicken Momos (Steamed)", 200)
    ],
    "Sandwich": [
        ("Veg Club Sandwich", 200), ("Veg Cheese Grilled Sandwich", 220),
        ("Chicken Club Sandwich", 280), ("Bombay Sandwich", 200), ("Chilli Cheese Toast", 110),
        ("Paneer Tikka Sandwich", 240), ("Peri Peri Chicken Sandwich", 290),
        ("Grilled Chicken Sandwich", 280), ("Garlic Chicken Mayo Sandwich", 290)
    ]
    # Add other categories here in same format...
}

# Dropdown for menu selection
section = st.selectbox("Select Menu Section", list(menu.keys()))

# Display selected section with markdown
st.subheader(section)
selected_items = {}  # Dictionary to store selected items and quantities

for item, price in menu[section].items():
    quantity = st.number_input(f"Quantity for {item} (₹{price})", min_value=0, max_value=10, step=1)
    if quantity > 0:
        selected_items[item] = {"price": price, "quantity": quantity}

# Order summary and form for customer details
if selected_items:
    st.subheader("Order Summary")
    total_amount = 0
    for item, details in selected_items.items():
        st.write(f"{item} x {details['quantity']} = ₹{details['quantity'] * details['price']}")
        total_amount += details['quantity'] * details['price']
    
    st.write(f"**Total Amount: ₹{total_amount}**")

    # Customer details
    st.subheader("Enter Your Details")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    address = st.text_area("Shipping Address")

    # Button to place order
    if st.button("Place Order"):
        if name and email and phone and address:
            st.success("🎉 Your order has been placed successfully!")
            st.write("**Order Details**")
            st.write(f"**Name:** {name}")
            st.write(f"**Email:** {email}")
            st.write(f"**Phone:** {phone}")
            st.write(f"**Address:** {address}")
            st.write("**Items Ordered:**")
            for item, details in selected_items.items():
                st.write(f"{item} x {details['quantity']} = ₹{details['quantity'] * details['price']}")
            st.write(f"**Total Amount:** ₹{total_amount}")
        else:
            st.warning("Please fill in all customer details before placing the order.")
else:
    st.warning("Please select items from the menu to place an order.")

# Footer
st.write("---")
st.write("**Nirvana by Oztel, Kasol**")
st.write("****")
st.write("📞 858 057 4937")

# Display items for selected category
items = menu[selected_category]
df = pd.DataFrame(items, columns=["Item", "Price (₹)"])
st.table(df)
