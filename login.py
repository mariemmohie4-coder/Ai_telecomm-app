import streamlit as st
import base64



def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    

def load_background():
    img = get_base64_image(
"ChatGPT Image May 1, 2026, 10_07_38 PM.png"    )

    page_bg = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image:
        linear-gradient(
            rgba(0,0,0,0.45),
            rgba(0,0,0,0.45)
        ),
        url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* CSS for Transparent Button */
    div.stButton > button {{
        background-color: transparent !important;
        color: white !important;
        border: 1px solid white !important;
        transition: 0.3s;
    }}

    div.stButton > button:hover {{
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-color: white !important;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

    [data-testid="stSidebar"] {{
        background: rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }}

    h1, h2, h3, h4, h5, h6, p, label, div {{
        color: white;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

def login():
    st.set_page_config(
        page_title="Welcome page",
        page_icon="🤖",
        layout="centered"
    )

    load_background()

    st.title("Welcome, Great to see you")
    
    st.image("518087549_1202687025203949_8625208704131875526_n.png")
    st.image("AI & telecom  Omar Ahmed (1).jpg")

    full_name = st.text_input("Username")
    ID = st.text_input("Password", type="password")

    if st.button("Login"):
        if ID == "IEEE":
            st.session_state.logged_in = True
            st.session_state.full_name = full_name
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Wrong password, ask +201099931689 about Password")
