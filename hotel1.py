import streamlit as st

st.set_page_config(page_title="Hotel Management - The Python Restaurant", page_icon="🍽️", layout="wide")

# --- MENU DATA ---
menu = {
    # Starters
    'Garlic Bread': 90,
    'French Fries': 80,
    'Spring Rolls': 100,
    'Cheese Balls': 110,
    'Tomato Soup': 70,

    # Main Course
    'Pizza': 100,
    'Burger': 80,
    'Pasta': 60,
    'Veg Biryani': 120,
    'Paneer Butter Masala': 140,
    'Chicken Curry': 180,
    'Fried Rice': 90,
    'Noodles': 85,

    # Desserts
    'Chocolate Cake': 100,
    'Ice Cream': 80,
    'Brownie': 120,
    'Gulab Jamun': 70,

    # Beverages
    'Coffee': 70,
    'Cold Drink': 50,
    'Mango Shake': 90,
    'Lemon Soda': 60
}

# --- APP TITLE ---
st.title("🍴 Five Star Python Restaurant")
st.markdown("#### Order your favorite food items and enjoy your meal 😋")

# --- TABS FOR CATEGORIES ---
tabs = st.tabs(["🍟 Starters", "🍕 Main Course", "🍰 Desserts", "🥤 Beverages"])

categories = {
    "🍟 Starters": ['Garlic Bread', 'French Fries', 'Spring Rolls', 'Cheese Balls', 'Tomato Soup'],
    "🍕 Main Course": ['Pizza', 'Burger', 'Pasta', 'Veg Biryani', 'Paneer Butter Masala', 'Chicken Curry', 'Fried Rice', 'Noodles'],
    "🍰 Desserts": ['Chocolate Cake', 'Ice Cream', 'Brownie', 'Gulab Jamun'],
    "🥤 Beverages": ['Coffee', 'Cold Drink', 'Mango Shake', 'Lemon Soda']
}

selected_items = []

# --- DISPLAY ITEMS IN EACH TAB ---
for i, (tab_name, items) in enumerate(categories.items()):
    with tabs[i]:
        st.subheader(tab_name)
        for item in items:
            if st.checkbox(f"{item} - ₹{menu[item]}", key=item):
                selected_items.append(item)

# --- TOTAL CALCULATION ---
order_total = sum(menu[item] for item in selected_items)

st.divider()
st.subheader("🧾 Your Order Summary")

if selected_items:
    st.write(f"**Items Selected:** {', '.join(selected_items)}")
    st.success(f"💰 Total Amount: ₹{order_total}")
else:
    st.info("No items selected yet. Start adding items from the menu above.")

# --- PLACE ORDER BUTTON ---
if st.button("✅ Place Order"):
    if selected_items:
        st.balloons()
        st.success(f"🎉 Order placed successfully! Total payable: ₹{order_total}")
    else:
        st.error("Please select at least one item to place your order.")

