import streamlit as st
from supabase import create_client, Client

# Supabase configuration
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def show_login():
    st.title("🔐 Login")

    # Create tabs for Sign In and Sign Up
    tab1, tab2 = st.tabs(["Sign In", "Sign Up"])

    # ---------- SIGN IN TAB ----------
    with tab1:
        email = st.text_input("Email", key="signin_email")
        password = st.text_input("Password", type="password", key="signin_password")

        if st.button("Login", key="login_btn"):
            if not email or not password:
                st.error("Enter email & password")
            else:
                try:
                    # Sign in with Supabase Auth
                    response = supabase.auth.sign_in_with_password({
                        "email": email,
                        "password": password
                    })
                    
                    if response.user:
                        # Get user profile
                        profile = supabase.table("profiles").select("*").eq("id", response.user.id).execute()
                        
                        # Store in session state
                        st.session_state.user = {
                            "id": response.user.id,
                            "email": response.user.email,
                            "full_name": profile.data[0]["full_name"] if profile.data else "",
                            "role": profile.data[0]["role"] if profile.data else "teacher"
                        }
                        
                        st.success(f"Welcome back, {st.session_state.user['full_name'] or email}!")
                        st.rerun()
                    else:
                        st.error("Invalid email or password")
                        
                except Exception as e:
                    st.error(f"Login error: {str(e)}")

    # ---------- SIGN UP TAB ----------
    with tab2:
        new_full_name = st.text_input("Full Name", key="signup_fullname")
        new_email = st.text_input("Email", key="signup_email")
        new_password = st.text_input("Choose Password", type="password", key="signup_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
        role = st.selectbox("Role", ["teacher", "admin"], key="signup_role")

        if st.button("Sign Up", key="signup_btn"):
            # Validation
            if not new_full_name or not new_email or not new_password:
                st.error("Please fill in all fields")
            elif len(new_password) < 6:
                st.error("Password must be at least 6 characters")
            elif new_password != confirm_password:
                st.error("Passwords do not match")
            elif "@" not in new_email:
                st.error("Please enter a valid email")
            else:
                try:
                    # Sign up with Supabase Auth
                    response = supabase.auth.sign_up({
                        "email": new_email,
                        "password": new_password
                    })
                    
                    if response.user:
                        # Create profile
                        supabase.table("profiles").insert({
                            "id": response.user.id,
                            "full_name": new_full_name,
                            "role": role
                        }).execute()
                        
                        st.success("✅ Account created! Please check your email to verify, then sign in.")
                        st.balloons()
                    else:
                        st.error("Sign up failed. Email may already exist.")
                        
                except Exception as e:
                    st.error(f"Sign up error: {str(e)}")