import re
import streamlit as st

# Page styling 
st.set_page_config(page_title="Password Strength Checker", page_icon="🔑", layout="centered")

st.markdown(
    """
    <style>
        /* Background with glass effect */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(to right, #e3f2fd, #ffffff);
            color: #333;
            font-family: 'Poppins', sans-serif;
        }
        
        /* Glassmorphism Card */
        .glass-card {
            background: rgba(255, 255, 255, 0.3);
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        /* Input Field */
        input[type="password"] {
            border-radius: 10px;
            padding: 12px;
            border: 2px solid #90caf9;
            width: 100%;
            font-size: 16px;
            background: rgba(255, 255, 255, 0.6);
            transition: 0.3s;
        }
        input[type="password"]:focus {
            border-color: #1e88e5;
            outline: none;
        }
        
        /* Button Styling */
        .stButton > button {
            background: linear-gradient(135deg, #42a5f5, #1e88e5) !important;
            color: white;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 18px;
            transition: 0.3s;
            border: none;
            font-weight: bold;
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, #1e88e5, #1565c0) !important;
        }

        /* Title Styling */
        .stMarkdown h1 {
            color: #1e88e5;
            font-weight: bold;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Title and Description
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its security level. 🔎")
st.markdown('</div>', unsafe_allow_html=True)

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be *at least 8 characters long*.")

    # Check uppercase & lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include *both uppercase and lowercase letters*.")
    
    # Check numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add *at least one number*.")
    
    # Check special characters
    if re.search(r"[!@#$%^&*()_+{}\[\]:;'<>,.?/~`|\\]", password):
        score += 1
    else:
        feedback.append("❌ Include *at least one special character (!@#$%^&*)*.")

    # Display result
    if score == 4:
        st.success("✅ *Strong Password* - Your password is secure.")
    elif score == 3:
        st.warning("⚠ *Moderate Password* - Consider improving security.")
    else:
        st.error("❌ *Weak Password* - Follow the suggestions below.")
    
    # Progress bar
    st.progress(score / 4)
    
    # Feedback
    if feedback:
        with st.expander("🔎 *Improve Your Password*"):
            for item in feedback:
                st.write(item)

# Input Field
password = st.text_input("Enter your Password", type="password", help="Ensure your password is strong 🔐")

# Button
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠ Please enter a password first!")
