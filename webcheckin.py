import streamlit as st

st.header("NIRAVANA WEBCHECK_IN")

with st.form("NIRVANA WEBCHECK-IN"):
    st.write("Niravana Webcheck-in")
    name_val = st.text_input("Name:-")
    where_val = st.text_input("Where are you coming from?")
    whereto_val = st.text_input("Where you headed to?")
    phone_val = st.text_input("Mobile Number:-")
    email_val = st.text_input("Email ID:-")
    nationa_val = st.text_input("Nationality:-")
    check0n_val = st.date_input("checkin date")
    checkout_val = st.date_input("checkout date")


    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("NAME:-", name_val, "Mobile Number", phone_val, "Email ID", email_val,"Where are you coming from?", where_val, "Where you headed to?", whereto_val, "checkin date", check0n_val, "checkoutdate",checkout_val)
