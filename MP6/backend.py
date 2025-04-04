from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load the expanded dataset
career_data = pd.read_csv("career_guidance_pathways.csv")

@app.get("/career-guidance/")
def get_career_path(subjects: str, marks_10th: int, marks_12th: int):
    user_subjects = set(subjects.lower().split(", "))  # Convert input to lowercase & set

    # Filter careers based on marks criteria
    filtered_careers = career_data[
        (career_data["Min_10th_Marks"] <= marks_10th) &
        (career_data["Min_12th_Marks"] <= marks_12th)
    ]

    best_match = None
    max_matched_subjects = 0

    # Check careers that match subjects
    for _, row in filtered_careers.iterrows():
        required_subjects = set(row["Required_Subjects"].lower().split(", "))

        # Count how many required subjects match the user input
        matched_subjects = len(required_subjects.intersection(user_subjects))

        # Prioritize careers with more subject matches
        if matched_subjects > max_matched_subjects:
            max_matched_subjects = matched_subjects
            best_match = row

    # If no match is found
    if best_match is None:
        return {"message": "No suitable career found. Try different subjects or marks."}

    return {
        "career": best_match["Career"],
        "required_10th_marks": best_match["Min_10th_Marks"],
        "required_12th_marks": best_match["Min_12th_Marks"],
        "required_subjects": best_match["Required_Subjects"],
        "entrance_exams": best_match["Entrance_Exams"],
        "higher_education": best_match["Higher_Education"],
        "best_colleges": best_match["Best_Colleges"]
    }
