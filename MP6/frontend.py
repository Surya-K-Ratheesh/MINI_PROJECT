import streamlit as st
import requests
import google.generativeai as genai

# Set up Gemini API Key
genai.configure(api_key="AIzaSyDHMzVnJ1J69u-IEoFkphmc2SpbZFJL164")  # Replace with your actual API key

# Function to interact with Gemini AI chatbot
def chat_with_gemini(user_query):
    model = genai.GenerativeModel("gemini-2.0-flash")  # Load the model
    response = model.generate_content(user_query)  # Generate response
    return response.text

# Streamlit App Title
st.title("🎯 AI Career Guidance Chatbot")

st.write("Enter your subjects and marks to get a personalized career path!")

# User Inputs
subjects = st.text_input("Enter your subjects (comma-separated, e.g., Math, Computer Science)")
marks_10th = st.number_input("Enter your 10th grade marks (%)", min_value=0, max_value=100, step=1)
marks_12th = st.number_input("Enter your 12th grade marks (%)", min_value=0, max_value=100, step=1)

# Initialize session states
if "career_result" not in st.session_state:
    st.session_state.career_result = None  # Store career path data
if "show_chatbot" not in st.session_state:
    st.session_state.show_chatbot = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Store chat messages

# Submit button for career recommendation
if st.button("Find My Career Path"):
    if not subjects or marks_10th == 0 or marks_12th == 0:
        st.warning("⚠ Please enter valid subjects and marks.")
    else:
        # Call the backend API
        response = requests.get(
            "http://127.0.0.1:8000/career-guidance/",
            params={"subjects": subjects, "marks_10th": marks_10th, "marks_12th": marks_12th}
        )

        if response.status_code == 200:
            data = response.json()

            if "message" in data:
                st.error(data["message"])
            else:
                # Store career result in session state
                st.session_state.career_result = data
                st.session_state.show_chatbot = True  # Show chatbot after career path is found

        else:
            st.error("❌ Error connecting to the career guidance system. Please try again.")

# Career Path Section (Always Visible)
if st.session_state.career_result:
    data = st.session_state.career_result
    st.subheader(f"✅ Recommended Career: {data['career']}")
    st.write(f"🔹 *Required 10th Marks:* {data['required_10th_marks']}%")
    st.write(f"🔹 *Required 12th Marks:* {data['required_12th_marks']}%")
    st.write(f"📚 *Subjects Needed:* {data['required_subjects']}")
    st.write(f"📝 *Entrance Exams:* {data['entrance_exams']}")
    st.write(f"🎓 *Higher Education Path:* {data['higher_education']}")
    st.write(f"🏛 *Top Colleges:* {data['best_colleges']}")

# Chatbot Section (Always visible once career path is generated)
if st.session_state.show_chatbot:
    st.subheader("💬 AI Chatbot - Ask Career Questions")

    # Fixed height chat container (Scrollable)
    chat_container = st.container()
    with chat_container:

        # Display chat history in correct order (latest at bottom)
        for role, message in st.session_state.chat_history:
            with st.chat_message(role):
                st.write(message)

    # Chat input stays at the bottom
    user_query = st.text_input("Type your message here and press Enter:", key="chat_input")
    if st.button("Chat with AI"):
        if user_query:
            response_text = chat_with_gemini(user_query)
            
            # Store chat history
            st.session_state.chat_history.append(("user", user_query))
            st.session_state.chat_history.append(("assistant", response_text))

            # Refresh chat UI
            st.rerun()
        else:
            st.warning("⚠ Please enter a question.")
