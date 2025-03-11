import streamlit as st
import requests

st.title("🎯 AI Career Guidance Chatbot")

st.write("Enter your subjects and marks to get a personalized career path!")

# User Inputs
subjects = st.text_input("Enter your subjects (comma-separated, e.g., Math, Computer Science)")
marks_10th = st.number_input("Enter your 10th grade marks (%)", min_value=0, max_value=100, step=1)
marks_12th = st.number_input("Enter your 12th grade marks (%)", min_value=0, max_value=100, step=1)

# Placeholder for results
output_placeholder = st.empty()

# Submit button
if st.button("Find My Career Path"):
    if not subjects or marks_10th == 0 or marks_12th == 0:
        st.warning("Please enter valid subjects and marks.")
    else:
        # Call the backend API
        response = requests.get(
            "http://127.0.0.1:8000/career-guidance/",
            params={"subjects": subjects, "marks_10th": marks_10th, "marks_12th": marks_12th}
        )

        # Clear previous results
        output_placeholder.empty()

        if response.status_code == 200:
            data = response.json()

            if "message" in data:
                st.error(data["message"])
            else:
                # Display the full career pathway
                with output_placeholder.container():
                    st.subheader(f"✅ Recommended Career: {data['career']}")
                    st.write(f"🔹 **Required 10th Marks:** {data['required_10th_marks']}%")
                    st.write(f"🔹 **Required 12th Marks:** {data['required_12th_marks']}%")
                    st.write(f"📚 **Subjects Needed:** {data['required_subjects']}")
                    st.write(f"📝 **Entrance Exams:** {data['entrance_exams']}")
                    st.write(f"🎓 **Higher Education Path:** {data['higher_education']}")
                    st.write(f"🏛 **Top Colleges:** {data['best_colleges']}")

        else:
            st.error("Error connecting to the career guidance system. Please try again.")

    # Ensure UI updates
    st.experimental_rerun()
