import streamlit as st

# Hardcoded credentials (for demo purposes only)
USER_CREDENTIALS = {
    "admin": "password123",  # change this!
    "user": "letmein"
}

def login():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        st.title("🔐 Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.button("Login")

        if login_btn:
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.success("Logged in!")
            else:
                st.error("Invalid username or password.")
        return False
    else:
        st.sidebar.markdown(f"👤 Logged in as **{st.session_state['username']}**")
        if st.sidebar.button("Logout"):
            st.session_state["authenticated"] = False
            st.experimental_rerun()
        return True
