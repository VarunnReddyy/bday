import streamlit as st
import random
import time  # Import time to simulate loading
from datetime import datetime, timedelta
import pytz  # Make sure to install pytz if you haven't already

# Set the page configuration with custom favicon
st.set_page_config(
    page_title="Birthday Baby",  # Your custom title
    page_icon="/Users/varunreddym/Desktop/bday/icon.ico"  # Replace with the path to your favicon
)

# Create a session state variable to track login status
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Fun question authentication
def login():
    st.title("Welcome to Your Birthday Surprise!")
    
    # Ask a fun question as a text input instead of MCQ
    st.write("To enter, answer this question correctly:")
    question = st.text_input("Whom i admire the most?(enter both first and lastname with a space in between and also if it says correct answer press R or top right corner you can find an option rerun click it )")

    # Convert both input and the correct answer to lowercase for comparison
    if question:
        if question.lower() == "virat kohli":  # Replace with the correct answer in lowercase
            st.session_state.authenticated = True
            st.success("Correct answer! Redirecting...")
            time.sleep(1)  # Simulate delay before redirecting
            # st.experimental_rerun()  # Rerun the app after successful login
        else:
            st.error("Incorrect answer! Please try again.")

# Check if the user is authenticated
if not st.session_state.authenticated:
    login()
else:
    # List of love notes to display randomly on page refresh
    love_notes = [
        "You're the best thing that's ever happened to me.",
        "I love you more than words can say!",
        "You make every day brighter, my love.",
        "Happy Birthday to the most amazing person ever!",
        "You are my sunshine on a rainy day.",
        "I am the luckiest person in the world to have you.",
        "Every moment with you is a treasure.",
        "You complete me in every way!"
    ]

    # Randomly select one love note to display
    selected_message = random.choice(love_notes)

    # Add CSS for styling, including background image
    st.markdown("""
    <style>
        /* Full screen background image */
        .stApp {
            background-image: url('pybday.jpg');  /* Replace with your background image path */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            opacity: 0.9; /* Control background image opacity */
        }

        /* Reduce opacity for the background layer while keeping content opaque */
        .stApp::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(255, 255, 255, 0.6); /* Semi-transparent white overlay */
            z-index: -1; /* Ensures the background is behind the content */
        }

        /* Style for the first message box */
        .first-message {
            background-color: #FFDDC1;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 10px;
        }

        /* Style for the second message box */
        .second-message {
            background-color: #D4F1F4;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }

        .first-message span {
            font-size: 24px;
            color: #FF4500; /* Color for the first message */
        }

        .second-message span {
            font-size: 20px;
            color: #2E8B57; /* Color for the love note */
        }

        .content {
            margin-top: 20px;
            font-size: 18px;
            line-height: 1.5;
        }

        .countdown {
            font-size: 30px;
            color: #FF4500; /* Color for the countdown */
            text-align: center;
            margin-top: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Add countdown timer for her birthday
    ist = pytz.timezone("Asia/Kolkata")  # Indian Standard Time
    birthday_time = ist.localize(datetime(2024, 10, 21, 0, 0, 0))  # Birthday at midnight

    # Get the current time in IST
    current_time = datetime.now(ist)

    # Calculate the time difference
    time_difference = birthday_time - current_time

    if time_difference.total_seconds() > 0:
        countdown_text = f"Countdown to Birthday: {str(time_difference).split('.')[0]}"
        st.markdown(f'<div class="countdown">{countdown_text}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="countdown">Happy Birthday!</div>', unsafe_allow_html=True)

    # Add sidebar for tab selection
    tab = st.sidebar.selectbox("Explore:", ["Welcome", "Memories","Music", "Special Wishes"])

    # Display the welcome message with a random love note only in the Welcome tab
    if tab == "Welcome":
        st.markdown(f"""
        <div class="first-message">
            <span>Many more happy returns of the day, Papa!</span>
        </div>
        <div class="second-message">
            <span>{selected_message}</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="content">Its your Birthday papa ivala 🥳</div>', unsafe_allow_html=True)
        st.write("I’m so excited to share this with you papaaa...")
        st.image("welcomepage.jpeg")  # Specific image for the Welcome tab

    else:
        # For other tabs, display only their content
        st.header(tab)  # Show the selected tab name as the header
        st.write("Welcome to the", tab, "tab!")

    if tab == "Memories":
        st.header("Its Baby sindhu to big sindhu😂")
        st.write("See this cute papa")
        video_path = ("https://drive.google.com/file/d/1WazHaPnmkKSBuQEjyazJpCL6pJZfNiUe/view?usp=sharing")  # Path to your local video file

        # Display loading message while the video loads
        with st.spinner("Sorry papa wait chey...🤧"):
            time.sleep(2)  # Simulate loading time
            st.video(video_path)  # This will display the video in the "Memory Lane" tab

    elif tab == "Music":
        st.header("I learnt this papa to surprise you🙂‍↔️")
        st.write("And btw adhe antha perfect m kadhu edho nka nak ochinattu try chesina nak 🫣")
        video_path_music = "music.mp4"  # Path to music video

        # Display loading message while the video loads
        with st.spinner("Sorry papa wait chey...🤧"):
            time.sleep(2)  # Simulate loading time
            st.video(video_path_music)  # Display the music video

    elif tab == "Special Wishes":
        st.header("Special Birthday Wishes")
        st.write("Just a few pictures of us together :)")
        video_splwishes_path=("https://drive.google.com/file/d/1d_Gw4x9e1HsA4rkpmt_G2cs3wHijwT4i/view?usp=sharing")
        # st.video("/Users/varunreddym/Desktop/bday/splwishes.mp4")  
        # Display loading message while the video loads
        with st.spinner("Sorry papa wait chey...🤧"):
            time.sleep(2)  # Simulate loading time
            st.video(video_splwishes_path)
