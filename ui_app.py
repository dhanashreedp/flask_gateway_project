import streamlit as st
import requests

# Replace with your Flask Gateway URL (via ngrok or local)
BASE_URL = "http://localhost:5000"  # Or your ngrok URL if deployed

st.title("🎯 API Gateway Application")

st.markdown(
    """
    This app serves as a demo interface for your API Gateway.
    It allows you to interact with different microservices (Auth, Analytics, Data Processing)
    via the central Flask Gateway.
    """
)

st.subheader("🧾 1. Register New User")
with st.form("register_form"):
    st.markdown("Enter details to register a new user:")
    reg_username = st.text_input("Username", key="reg_username_input")
    reg_password = st.text_input("Password", type="password", key="reg_password_input")
    
    register_status_message = st.empty()

    reg_submit = st.form_submit_button("Register")
    if reg_submit:
        if not reg_username or not reg_password:
            register_status_message.error("Username and password cannot be empty.")
        else:
            register_status_message.info("Attempting to register user...")
            try:
                res = requests.post(
                    f"{BASE_URL}/api/auth/register/",
                    json={"username": reg_username, "password": reg_password}
                )

                if res.status_code == 200:
                    try:
                        register_status_message.success("Registration successful!")
                        st.json(res.json())
                    except requests.exceptions.JSONDecodeError:
                        register_status_message.error("Registration successful, but response is not valid JSON.")
                else:
                    register_status_message.warning(f"Registration failed with status {res.status_code}.")
                    try:
                        st.json(res.json())
                    except requests.exceptions.JSONDecodeError:
                        register_status_message.error("Registration failed. Backend returned non-JSON error.")

            except requests.exceptions.ConnectionError:
                register_status_message.error(f"Connection Error: Could not connect to the API Gateway at {BASE_URL}. "
                                             "Please ensure your Flask Gateway is running and accessible.")
            except requests.exceptions.Timeout:
                register_status_message.error("Request timed out. The API Gateway might be slow or unresponsive.")
            except requests.exceptions.RequestException as e:
                register_status_message.error(f"An error occurred during the request: {e}")
            except Exception as e:
                register_status_message.error(f"An unexpected error occurred: {e}")

st.subheader("🔐 2. Login")
with st.form("login_form"):
    st.markdown("Enter credentials to log in:")
    login_username = st.text_input("Username", key="login_username_input")
    login_password = st.text_input("Password", type="password", key="login_password_input")
    
    login_status_message = st.empty()

    login_submit = st.form_submit_button("Login")
    if login_submit:
        if not login_username or not login_password:
            login_status_message.error("Username and password cannot be empty.")
        else:
            login_status_message.info("Attempting to log in user...")
            try:
                res = requests.post(
                    f"{BASE_URL}/api/auth/login/",
                    json={"username": login_username, "password": login_password}
                )

                if res.status_code == 200:
                    try:
                        login_status_message.success("Login successful!")
                        st.json(res.json())
                    except requests.exceptions.JSONDecodeError:
                        login_status_message.error("Login successful, but response is not valid JSON.")
                else:
                    login_status_message.warning(f"Login failed with status {res.status_code}.")
                    try:
                        st.json(res.json())
                    except requests.exceptions.JSONDecodeError:
                        login_status_message.error("Login failed. Backend returned non-JSON error.")

            except requests.exceptions.ConnectionError:
                login_status_message.error(f"Connection Error: Could not connect to the API Gateway at {BASE_URL}. "
                                            "Please ensure your Flask Gateway is running and accessible.")
            except requests.exceptions.Timeout:
                login_status_message.error("Request timed out. The API Gateway might be slow or unresponsive.")
            except requests.exceptions.RequestException as e:
                login_status_message.error(f"An error occurred during the request: {e}")
            except Exception as e:
                login_status_message.error(f"An unexpected error occurred: {e}")


st.subheader("📊 3. Track Analytics Event")
st.markdown("Click the button to send a dummy analytics event:")
if st.button("Track Event"):
    st.info("Attempting to track analytics event...")
    try:
        res = requests.get(f"{BASE_URL}/api/analytics/track/")

        if res.status_code == 200:
            try:
                st.success("Analytics event tracked successfully!")
                st.json(res.json())
            except requests.exceptions.JSONDecodeError:
                st.error("Analytics tracking successful, but response is not valid JSON.")
        else:
            st.warning(f"Analytics tracking failed with status {res.status_code}.")
            try:
                st.json(res.json())
            except requests.exceptions.JSONDecodeError:
                st.error("Analytics tracking failed. Backend returned non-JSON error.")

    except requests.exceptions.ConnectionError:
        st.error(f"Connection Error: Could not connect to the API Gateway at {BASE_URL}. "
                 "Please ensure your Flask Gateway is running and accessible.")
    except requests.exceptions.Timeout:
        st.error("Request timed out. The API Gateway might be slow or unresponsive.")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred during the request: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")


st.subheader("🧠 4. Data Processing")
st.markdown("Enter text to send for processing:")
user_input = st.text_area("Enter text to process", height=100)
if st.button("Process Text"):
    if not user_input:
        st.warning("Please enter some text to process.")
    else:
        st.info("Attempting to process text...")
        try:
            res = requests.post(
                f"{BASE_URL}/api/data/process/",
                json={"text": user_input}
            )

            if res.status_code == 200:
                try:
                    st.success("Text processed successfully!")
                    st.json(res.json())
                except requests.exceptions.JSONDecodeError:
                    st.error("Text processing successful, but response is not valid JSON.")
            else:
                st.warning(f"Text processing failed with status {res.status_code}.")
                try:
                    st.json(res.json())
                except requests.exceptions.JSONDecodeError:
                    st.error("Text processing failed. Backend returned non-JSON error.")

        except requests.exceptions.ConnectionError:
            st.error(f"Connection Error: Could not connect to the API Gateway at {BASE_URL}. "
                     "Please ensure your Flask Gateway is running and accessible.")
        except requests.exceptions.Timeout:
            st.error("Request timed out. The API Gateway might be slow or unresponsive.")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred during the request: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
