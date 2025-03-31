# import streamlit as st
# import requests
# from google import genai

# # Configure Gemini API
# GEMINI_API_KEY = "AIzaSyDHMzVnJ1J69u-IEoFkphmc2SpbZFJL164"  # Replace with your actual API key
# client = genai.Client(api_key=GEMINI_API_KEY)

# st.title("🎯 AI Career Guidance Chatbot")

# st.write("Enter your subjects and marks to get a personalized career path!")

# # User Inputs
# subjects = st.text_input("Enter your subjects (comma-separated, e.g., Math, Computer Science)")
# marks_10th = st.number_input("Enter your 10th grade marks (%)", min_value=0, max_value=100, step=1)
# marks_12th = st.number_input("Enter your 12th grade marks (%)", min_value=0, max_value=100, step=1)

# # Placeholder for results
# output_placeholder = st.empty()

# # Submit button for career guidance
# if st.button("Find My Career Path"):
#     if not subjects or marks_10th == 0 or marks_12th == 0:
#         st.warning("Please enter valid subjects and marks.")
#     else:
#         response = requests.get(
#             "http://127.0.0.1:8000/career-guidance/",
#             params={"subjects": subjects, "marks_10th": marks_10th, "marks_12th": marks_12th}
#         )

#         output_placeholder.empty()

#         if response.status_code == 200:
#             data = response.json()

#             if "message" in data:
#                 st.error(data["message"])
#             else:
#                 with output_placeholder.container():
#                     st.subheader(f"✅ Recommended Career: {data['career']}")
#                     st.write(f"🔹 **Required 10th Marks:** {data['required_10th_marks']}%")
#                     st.write(f"🔹 **Required 12th Marks:** {data['required_12th_marks']}%")
#                     st.write(f"📚 **Subjects Needed:** {data['required_subjects']}")
#                     st.write(f"📝 **Entrance Exams:** {data['entrance_exams']}")
#                     st.write(f"🎓 **Higher Education Path:** {data['higher_education']}")
#                     st.write(f"🏛 **Top Colleges:** {data['best_colleges']}")

#         else:
#             st.error("Error connecting to the career guidance system. Please try again.")

# # Chatbot Section
# st.subheader("💬 Ask AI Career Chatbot")

# user_query = st.text_input("Ask any career-related question:")

# if st.button("Ask Gemini AI"):
#     if user_query.strip():
#         try:
#             response = client.models.generate_content(
#                 model="gemini-2.0-flash",
#                 contents=user_query,
#             )
#             st.write("🤖 AI Response:")
#             st.write(response.text)
#         except Exception as e:
#             st.error(f"Error in AI response: {e}")
#     else:
#         st.warning("Please enter a question.")


# import streamlit as st
# import requests
# import google.generativeai as genai

# # Set up Gemini API Key
# genai.configure(api_key="AIzaSyDHMzVnJ1J69u-IEoFkphmc2SpbZFJL164")

# st.title("🎯 AI Career Guidance Chatbot")

# st.write("Enter your subjects and marks to get a personalized career path!")

# # User Inputs
# subjects = st.text_input("Enter your subjects (comma-separated, e.g., Math, Computer Science)")
# marks_10th = st.number_input("Enter your 10th grade marks (%)", min_value=0, max_value=100, step=1)
# marks_12th = st.number_input("Enter your 12th grade marks (%)", min_value=0, max_value=100, step=1)

# # Placeholder for results
# output_placeholder = st.empty()
# show_chatbot = False  # Flag to control chatbot visibility

# # Submit button
# if st.button("Find My Career Path"):
#     if not subjects or marks_10th == 0 or marks_12th == 0:
#         st.warning("Please enter valid subjects and marks.")
#     else:
#         # Call the backend API
#         response = requests.get(
#             "http://127.0.0.1:8000/career-guidance/",
#             params={"subjects": subjects, "marks_10th": marks_10th, "marks_12th": marks_12th}
#         )

#         # Clear previous results
#         output_placeholder.empty()

#         if response.status_code == 200:
#             data = response.json()

#             if "message" in data:
#                 st.error(data["message"])
#             else:
#                 # Display the full career pathway
#                 with output_placeholder.container():
#                     st.subheader(f"✅ Recommended Career: {data['career']}")
#                     st.write(f"🔹 **Required 10th Marks:** {data['required_10th_marks']}%")
#                     st.write(f"🔹 **Required 12th Marks:** {data['required_12th_marks']}%")
#                     st.write(f"📚 **Subjects Needed:** {data['required_subjects']}")
#                     st.write(f"📝 **Entrance Exams:** {data['entrance_exams']}")
#                     st.write(f"🎓 **Higher Education Path:** {data['higher_education']}")
#                     st.write(f"🏛 **Top Colleges:** {data['best_colleges']}")

#                 # Enable chatbot after displaying career path
#                 show_chatbot = True
#         else:
#             st.error("Error connecting to the career guidance system. Please try again.")

# # **Chatbot Section (Only shows after career pathway)**
# if show_chatbot:
#     st.subheader("💬 Ask the AI Chatbot")

#     user_query = st.text_input("Ask about this career or anything else:")
#     if st.button("Chat with AI"):
#         if user_query:
#             response = genai.generate_content(model="gemini-2.0-pro", contents=user_query)
#             st.write("🤖 AI Response:")
#             st.write(response.text)
#         else:
#             st.warning("Please enter a question.")

# import streamlit as st
# import requests
# import google.generativeai as genai

# # Set up Gemini API Key
# genai.configure(api_key="AIzaSyDHMzVnJ1J69u-IEoFkphmc2SpbZFJL164")

# st.title("🎯 AI Career Guidance Chatbot")

# st.write("Enter your subjects and marks to get a personalized career path!")

# # Initialize session state variables
# if "career_data" not in st.session_state:
#     st.session_state.career_data = None
# if "show_chatbot" not in st.session_state:
#     st.session_state.show_chatbot = False

# # User Inputs
# subjects = st.text_input("Enter your subjects (comma-separated, e.g., Math, Computer Science)")
# marks_10th = st.number_input("Enter your 10th grade marks (%)", min_value=0, max_value=100, step=1)
# marks_12th = st.number_input("Enter your 12th grade marks (%)", min_value=0, max_value=100, step=1)

# # Submit button
# if st.button("Find My Career Path"):
#     if not subjects or marks_10th == 0 or marks_12th == 0:
#         st.warning("Please enter valid subjects and marks.")
#     else:
#         # Call the backend API
#         response = requests.get(
#             "http://127.0.0.1:8000/career-guidance/",
#             params={"subjects": subjects, "marks_10th": marks_10th, "marks_12th": marks_12th}
#         )

#         if response.status_code == 200:
#             data = response.json()

#             if "message" in data:
#                 st.error(data["message"])
#             else:
#                 # Store results in session state
#                 st.session_state.career_data = data
#                 st.session_state.show_chatbot = True  # Enable chatbot

#         else:
#             st.error("Error connecting to the career guidance system. Please try again.")

# # Display Career Results from session state
# if st.session_state.career_data:
#     data = st.session_state.career_data
#     st.subheader(f"✅ Recommended Career: {data['career']}")
#     st.write(f"🔹 **Required 10th Marks:** {data['required_10th_marks']}%")
#     st.write(f"🔹 **Required 12th Marks:** {data['required_12th_marks']}%")
#     st.write(f"📚 **Subjects Needed:** {data['required_subjects']}")
#     st.write(f"📝 **Entrance Exams:** {data['entrance_exams']}")
#     st.write(f"🎓 **Higher Education Path:** {data['higher_education']}")
#     st.write(f"🏛 **Top Colleges:** {data['best_colleges']}")

# # Chatbot Section (Only appears after career results)
# if st.session_state.show_chatbot:
#     st.subheader("💬 Ask the AI Chatbot")

#     user_query = st.text_input("Ask about this career or anything else:")
#     if st.button("Chat with AI"):
#         if user_query:
#             response = genai.generate_content(model="gemini-2.0-pro", contents=user_query)
#             st.write("🤖 AI Response:")
#             st.write(response.text)
#         else:
#             st.warning("Please enter a question.")


# import streamlit as st
# import requests
# import google.generativeai as genai

# # Set up Gemini API Key
# genai.configure(api_key="AIzaSyDHMzVnJ1J69u-IEoFkphmc2SpbZFJL164")  # Replace with your actual API key

# # Function to interact with Gemini AI chatbot
# def chat_with_gemini(user_query):
#     model = genai.GenerativeModel("gemini-2.0-flash")  # Load the model
#     response = model.generate_content(user_query)  # Generate response
#     return response.text

# # Streamlit App Title
# st.title("🎯 AI Career Guidance Chatbot")

# st.write("Enter your subjects and marks to get a personalized career path!")

# # User Inputs
# subjects = st.text_input("Enter your subjects (comma-separated, e.g., Math, Computer Science)")
# marks_10th = st.number_input("Enter your 10th grade marks (%)", min_value=0, max_value=100, step=1)
# marks_12th = st.number_input("Enter your 12th grade marks (%)", min_value=0, max_value=100, step=1)

# # Placeholder for results
# output_placeholder = st.empty()

# # Initialize session state for chatbot visibility
# if "show_chatbot" not in st.session_state:
#     st.session_state.show_chatbot = False

# # Submit button for career recommendation
# if st.button("Find My Career Path"):
#     if not subjects or marks_10th == 0 or marks_12th == 0:
#         st.warning("⚠️ Please enter valid subjects and marks.")
#     else:
#         # Call the backend API
#         response = requests.get(
#             "http://127.0.0.1:8000/career-guidance/",
#             params={"subjects": subjects, "marks_10th": marks_10th, "marks_12th": marks_12th}
#         )

#         # Clear previous results
#         output_placeholder.empty()

#         if response.status_code == 200:
#             data = response.json()

#             if "message" in data:
#                 st.error(data["message"])
#             else:
#                 # Display the full career pathway
#                 with output_placeholder.container():
#                     st.subheader(f"✅ Recommended Career: {data['career']}")
#                     st.write(f"🔹 **Required 10th Marks:** {data['required_10th_marks']}%")
#                     st.write(f"🔹 **Required 12th Marks:** {data['required_12th_marks']}%")
#                     st.write(f"📚 **Subjects Needed:** {data['required_subjects']}")
#                     st.write(f"📝 **Entrance Exams:** {data['entrance_exams']}")
#                     st.write(f"🎓 **Higher Education Path:** {data['higher_education']}")
#                     st.write(f"🏛 **Top Colleges:** {data['best_colleges']}")

#                 # Show chatbot option after displaying career path
#                 st.session_state.show_chatbot = True

#         else:
#             st.error("❌ Error connecting to the career guidance system. Please try again.")

# # Chatbot Section (Only appears after career results)
# if st.session_state.show_chatbot:
#     st.subheader("💬 Ask the AI Chatbot")

#     user_query = st.text_input("Ask about this career or anything else:")
#     if st.button("Chat with AI"):
#         if user_query:
#             response_text = chat_with_gemini(user_query)
#             st.write("🤖 AI Response:")
#             st.write(response_text)
#         else:
#             st.warning("⚠️ Please enter a question.")

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
