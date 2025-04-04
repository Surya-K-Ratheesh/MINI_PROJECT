from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

# Load the expanded dataset
career_data = pd.read_csv("career_guidance_pathways.csv")
career_data_unqualified = pd.read_csv("career_guidance_pathways_no_qualification.csv")

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


@app.get("/career-guidance-unqualified/")
def get_career_path_unqualified(interests: str):
    # Normalize user interests: lowercase and strip whitespace
    user_interests = set(i.strip().lower() for i in interests.split(","))

    best_match = None
    max_matches = 0

    for _, row in career_data_unqualified.iterrows():
        # Extract required subjects and normalize
        required_subjects_raw = row["Required_Subjects"]
        if pd.isna(required_subjects_raw):
            continue

        career_keywords = set(s.strip().lower() for s in required_subjects_raw.split(","))
        print("DBGXXX:", career_keywords, user_interests)

        match_count = len(user_interests.intersection(career_keywords))

        if match_count > max_matches:
            max_matches = match_count
            best_match = row

    if best_match is None:
        return {"message": "No career matched your interests. Try rephrasing them."}

    clean_data = best_match.fillna("N/A").to_dict()

    return JSONResponse(content={
        "career": clean_data["Career"],
        "required_10th_marks": clean_data["Min_10th_Marks"],
        "required_12th_marks": clean_data["Min_12th_Marks"],
        "required_subjects": clean_data["Required_Subjects"],
        "entrance_exams": clean_data["Entrance_Exams"],
        "higher_education": clean_data["Higher_Education"],
        "best_colleges": clean_data["Best_Colleges"],
    })
