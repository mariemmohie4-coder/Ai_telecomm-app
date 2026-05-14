import streamlit as st
import base64

from streamlit_pdf_viewer import pdf_viewer

def show_pdf(pdf_path):
       try:
           pdf_viewer(pdf_path)
       except Exception as e:
           st.error(f"Error: {e}")
    
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
def home(name):
    
    st.set_page_config(
        page_title="TELECOM",
        page_icon="📡",
        layout="centered"
    )
    
    img = get_base64_image("Blog-images-scaled.jpg")

    page_bg = f"""
    <style>

    [data-testid="stAppViewContainer"] {{
        background-image:
        linear-gradient(rgba(0,0,0,0.5),
        rgba(0,0,0,0.5)),
        url("data:image/jpg;base64,{img}");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Transparent Style for both Buttons and LinkButtons */
    div.stButton > button, div.stLinkButton > a {{
        background-color: transparent !important;
        color: white !important;
        border: 1px solid white !important;
        transition: 0.3s;
        text-decoration: none; /* عشان الرابط ميظهرش تحته خط */
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }}

    /* Hover effect */
    div.stButton > button:hover, div.stLinkButton > a:hover {{
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-color: white !important;
        color: white !important;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

    [data-testid="stSidebar"] {{
        background: rgba(0,0,0,0.3);
    }}

    h1, h2, h3, h4, h5, h6, p, label, div {{
        color: white;
    }}

    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)
    
    st.title("AI in Telecommunication")
    st.header(f"Welcome {name}")
    
    option = st.radio(
        "Choose what you want to read about:",
        [
            "LinkedIn Page",
            "Slides",
            "IEEE APS",
            "AI Training Summer",
            "Graduation Projects"
        ],
        horizontal=False
    )

    if option == "LinkedIn Page":
        # image for likedin account for [ omar - mariem ]
        # link for each account
        st.header("LinkedIn Page")
        st.subheader("Connect with us")
        st.image("omar_linkedin.png")
        col1, col2, col3 =st.columns(3)
        with col2:
         st.link_button("Omar on LinkedIn","https://www.linkedin.com/in/omar-ahmed-7590491ba?utm_source=share_via&utm_content=profile&utm_medium=member_android")

        st.image("mariem_linkedin.png")
        col1,col2,col3=st.columns(3)
        with col2:
         st.link_button("Mariem on LinkedIn","https://www.linkedin.com/in/mariemmohie50")
         
        

    elif option == "Slides":
        # add option to download slides from website ( you can add slides link )
        # if user push download button -- > go to drive page
        # browse slides in website
        st.header("Slides")
        st.write("Here you can add your slides links or descriptions.")
        st.link_button("Go to Google Drive to Download Slides","https://drive.google.com/file/d/1bIvXEW6EHHURYlWypauDfCIUPcWGMXLZ/view?usp=drive_link")
        st.write("Preview Slides:")
        show_pdf("test.pdf")


    elif option == "IEEE APS":
        # add IEEE AP-S Logo ( google it )
        # add information after logo ( chatgpt - google it )
        st.header("IEEE APS")
        st.image("aps-logo.png")
        st.write("IEEE Antennas and Propagation Society content goes here.")
        st.markdown("""
        ### Connecting the World Through Electromagnetic Innovation
        The **IEEE AP-S** is a premier international technical society dedicated to the advancement of electromagnetic theory and its practical applications. It serves as the global hub for engineers specializing in how wireless signals are created, transmitted, and received.
        """)
        with st.expander(" The Three Core Pillars"):
            st.markdown("""
            *   **Antennas:** Designing structures that transition waves into free space, from 5G sensors to satellite arrays.
            *   **Propagation:** Studying wave travel through media and interactions with the environment and obstacles.
            *   **EM Theory:** The mathematical backbone governing wave behavior using advanced computational simulations.
            """)

        with st.expander(" Why It Matters"):
            st.markdown("""
            *   **A Research Powerhouse:** Publishes the *IEEE Transactions on AP*, the gold standard for innovation.
            *   **Global Networking:** Annual Symposiums for discussing 5G/6G and Space Exploration.
            *   **Student Empowerment:** Provides travel grants, workshops, and a global mentor network.
            """)

        st.info("The Future is Wireless: AP-S is where complex mathematics meets the reality of global connectivity.")
        st.write("\n")
        st.subheader("IEEE AP-S Founders")
        col1,col2,col3 = st.columns([2, 2, 2])
        with col1:
            st.image("Omar Ahmed.jpg",caption="Omar Ahmed")
            st.image("Aly Eldeen.jpg",caption="Aly Eldeen")

        with col2:
             st.image("Khaled Elaskry.jpg",caption="Khaled Elaskry")
             st.image("Zaid Ismail.jpg",caption="Zaid Ismail")
        
        with col3:
            st.image("Fares Shreif.jpg", caption="Fares Shreif")
    
            

        


    elif option == "AI Training Summer":
        # add information about training ( duration - certificate - project - content )
        # add board information ( omar ahmed - omar ashraf - marwan abbas - mohammed adel - Alaa )
        # add whatsapp group link( imp )
        st.header("AI Training Summer")
        st.write("Information about the AI training program goes here.")
        st.subheader("Program Overview:")
        st.write("""
        Join an intensive summer journey designed to bridge the gap between 
        **Artificial Intelligence** and modern **Telecommunication systems**. 
        This program provides hands-on experience in building intelligent 
        solutions for the next generation of connectivity.
        """)
        col1, col2 = st.columns(2)
        with col1:
            st.info("Duration\n\nJuly 15th – August 30th (1.5 Months)")
        with col2:
            st.info("Structure\n\n4 Intensive Sessions +  Final Project")
        
        st.subheader("Training Content:")
        st.markdown("""
        - **Machine Learning Fundamentals.**
        - **Introduction to Deep Learning.**
        """)
       
        st.subheader("Final Project:")
        st.markdown(""" A specialized project focused on **AI Applications in Telecommunications.**""")

        st.success("**Certificate:** Participants will receive a certificate upon completing the final project.")
        st.subheader("Meet the Board")
        b1, b2, b3 = st.columns(3)
        with b1:
         st.image("omar_linkedin.png",caption="Head:Omar Ahmed")
         st.link_button("Omar on LinkedIn","https://www.linkedin.com/in/omar-ahmed-7590491ba?utm_source=share_via&utm_content=profile&utm_medium=member_android")
         
        with b2:
         st.image("marwan.png",caption="Vice Head:Marwan Abbas")
         st.link_button("Marwan on LinkedIn","https://www.linkedin.com/in/marwan-abbas-ba1509266?utm_source=share_via&utm_content=profile&utm_medium=member_android")
         st.image("omar ashraf.png",caption="Vice Head:Omar Ashraf")
         st.link_button("Omar on LinkedIn","https://www.linkedin.com/in/omar-ashraf-790086178?utm_source=share_via&utm_content=profile&utm_medium=member_android")


        with b3:
         st.image("mohammed adel.png",caption="Mentor:Mohammed Adel")
         st.link_button("Mohammed on LinkedIn","https://www.linkedin.com/in/mohammed-adel-b56615248?utm_source=share_via&utm_content=profile&utm_medium=member_android")
         st.image("alaa.png",caption="Mentor:Alaa Sweed")
         st.link_button("Omar on LinkedIn","https://www.linkedin.com/in/alaa-sweed-981228301?utm_source=share_via&utm_content=profile&utm_medium=member_android")


        st.subheader("Whatsapp Group:")
        st.link_button("Whatsapp Group Link","https://chat.whatsapp.com/DdHO6G4yb9H2qlfDVAGe8i")
        st.image("training.jpg",width=300)
    elif option == "Graduation Projects":
        #show_pdf("C:/Users/Mega Store/Downloads/AI_PDF.pdf")
        # slides ideas :
        # pdf for projects
        st.header("Graduation Projects")
        st.write("Ideas and descriptions for graduation projects go here.")
        st.link_button("Go to Google Drive to Download pdf","https://drive.google.com/file/d/1bIvXEW6EHHURYlWypauDfCIUPcWGMXLZ/view?usp=drive_link")
        st.write("Preview Slides:")
        show_pdf("test.pdf")


        
        
        
    if st.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()
