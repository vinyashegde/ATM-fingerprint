import streamlit as st

# Simulated user data for demonstration purposes
USER_BALANCE = 5000  # Starting balance
users = {"James": {"pin": "1234", "balance": USER_BALANCE}}

# Function for fingerprint (simulated) authentication
def fingerprint_authentication():
    st.subheader("Fingerprint Authentication")
    st.write("Please place your finger on the scanner.")
    # Simulate success after clicking a button (replace with actual fingerprint hardware later)
    if st.button("Simulate Fingerprint Scan"):
        st.session_state.fingerprint_authenticated = True
        st.success("Fingerprint authenticated!")
        st.markdown(
            """
            <style>
            .next-button {
                display: flex;
                justify-content: flex-end;
                margin-top: 20px;
            }
            </style>
            """, unsafe_allow_html=True)
        return True
    return False

# Function for entering PIN after fingerprint
def pin_authentication():
    st.subheader("PIN Authentication")
    pin = st.text_input("Enter your PIN:", type="password")
    if st.button("Submit PIN"):
        if pin == users["James"]["pin"]:
            st.session_state.pin_authenticated = True
            st.success("PIN authentication successful!")
            return True
        else:
            st.error("Incorrect PIN!")
    return False

# Function for Balance Inquiry
def balance_inquiry():
    st.subheader("Balance Inquiry")
    st.write(f"Your current balance is: ${users['James']['balance']}")
    return True

# Function for Money Withdrawal
def money_withdrawal():
    st.subheader("Money Withdrawal")
    amount = st.number_input("Enter amount to withdraw:", min_value=0, max_value=users['James']['balance'], step=10)
    if st.button("Withdraw"):
        if amount <= users["James"]["balance"]:
            users["James"]["balance"] -= amount
            st.success(f"${amount} withdrawn successfully!")
            st.write(f"Remaining balance: ${users['James']['balance']}")
            return True
        else:
            st.error("Insufficient funds!")
    return False

# Function for Money Deposit
def money_deposit():
    st.subheader("Money Deposit")
    amount = st.number_input("Enter amount to deposit:", min_value=0, step=10)
    if st.button("Deposit"):
        users["James"]["balance"] += amount
        st.success(f"${amount} deposited successfully!")
        st.write(f"New balance: ${users['James']['balance']}")
        return True
    return False

# Function for Bill Payment
def bill_payment():
    st.subheader("Bill Payment")
    bill_amount = st.number_input("Enter bill amount:", min_value=0, step=10)
    if st.button("Pay Bill"):
        if bill_amount <= users["James"]["balance"]:
            users["James"]["balance"] -= bill_amount
            st.success(f"Bill of ${bill_amount} paid successfully!")
            st.write(f"Remaining balance: ${users['James']['balance']}")
            return True
        else:
            st.error("Insufficient funds!")
    return False

# Function for Mini Statement
def mini_statement():
    st.subheader("Mini Statement")
    st.write(f"Current Balance: ${users['James']['balance']}")
    st.write("Last 5 transactions (simulated):")
    st.write("""
    - Withdrawal: $100
    - Deposit: $200
    - Bill Payment: $50
    - Withdrawal: $300
    - Deposit: $500
    """)
    return True

# Function for Internal Transfer
def internal_transfer():
    st.subheader("Internal Transfer")
    transfer_amount = st.number_input("Enter amount to transfer:", min_value=0, step=10)
    recipient = st.text_input("Enter recipient name:")
    if st.button("Transfer"):
        if transfer_amount <= users["James"]["balance"]:
            users["James"]["balance"] -= transfer_amount
            st.success(f"${transfer_amount} transferred to {recipient} successfully!")
            st.write(f"Remaining balance: ${users['James']['balance']}")
            return True
        else:
            st.error("Insufficient funds!")
    return False

# Function for PIN Change
def pin_change():
    st.subheader("PIN Change")
    new_pin = st.text_input("Enter new PIN:", type="password")
    confirm_pin = st.text_input("Confirm new PIN:", type="password")
    if st.button("Change PIN"):
        if new_pin == confirm_pin and len(new_pin) == 4:
            users["James"]["pin"] = new_pin
            st.success("PIN changed successfully!")
            return True
        else:
            st.error("PIN mismatch or invalid length!")
    return False

# Main app function
def atm_app():
    st.title("Cardless ATM Interface")

    if "fingerprint_authenticated" not in st.session_state:
        st.session_state.fingerprint_authenticated = False
    if "pin_authenticated" not in st.session_state:
        st.session_state.pin_authenticated = False

    # Manage authentication steps
    if not st.session_state.fingerprint_authenticated:
        st.header("Fingerprint Authentication")
        if fingerprint_authentication():
            if st.button("Next", key="fingerprint_next", help="Go to PIN authentication", disabled=False):
                pass  # This button is just to allow user to move to next step
    elif not st.session_state.pin_authenticated:
        st.header("PIN Authentication")
        if pin_authentication():
            if st.button("Next", key="pin_next", help="Go to ATM options", disabled=False):
                pass  # Continue to next step
    else:
        st.header("Welcome to Sayali's Bank ATM")

        # Display options
        option = st.selectbox("Choose your transaction", [
            "Balance Inquiry",
            "Money Withdrawal",
            "Money Deposit",
            "Bill Payment",
            "Mini Statement",
            "Internal Transfer",
            "PIN Change",
            "Exit/Take Card"
        ])

        # Display the selected option's functionality
        if option == "Balance Inquiry":
            if balance_inquiry():
                if st.button("Next", key="balance_next", help="Return to menu"):
                    pass
        elif option == "Money Withdrawal":
            if money_withdrawal():
                if st.button("Next", key="withdraw_next", help="Return to menu"):
                    pass
        elif option == "Money Deposit":
            if money_deposit():
                if st.button("Next", key="deposit_next", help="Return to menu"):
                    pass
        elif option == "Bill Payment":
            if bill_payment():
                if st.button("Next", key="bill_next", help="Return to menu"):
                    pass
        elif option == "Mini Statement":
            if mini_statement():
                if st.button("Next", key="statement_next", help="Return to menu"):
                    pass
        elif option == "Internal Transfer":
            if internal_transfer():
                if st.button("Next", key="transfer_next", help="Return to menu"):
                    pass
        elif option == "PIN Change":
            if pin_change():
                if st.button("Next", key="pinchange_next", help="Return to menu"):
                    pass
        elif option == "Exit/Take Card":
            st.session_state.fingerprint_authenticated = False
            st.session_state.pin_authenticated = False
            st.write("Thank you for using the ATM. Goodbye!")

# Run the app
if __name__ == "__main__":
    atm_app()
