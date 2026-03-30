import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Virtual Study Lab", layout="wide")

# ---------------- SIDEBAR MENU ----------------
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Theory", "Principle", "Study Planner",
     "Weak Subject Tracker", "AI Suggestions", "Quiz", "Feedback"]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.title("📚 Virtual Study Lab with AI Planner")

    st.markdown("""
    Welcome to the **Smart Virtual Study Laboratory**.

    This platform helps students:
    - 📖 Understand study concepts
    - 🧠 Apply planning principles
    - 📅 Generate smart timetables
    - 📊 Track weak subjects
    - 🤖 Receive AI-based suggestions
    - 📝 Test knowledge
    - 💬 Provide feedback
    """)

    st.success("Navigate using the sidebar to explore all sections.")

# ---------------- THEORY ----------------
elif menu == "Theory":
    st.title("📘 Theory: Smart Study Planning")

    st.markdown("""
    Effective study planning is based on:

    ### 1️⃣ Time Management
    Allocating study hours proportionally based on subject difficulty.

    ### 2️⃣ Performance Analysis
    Identifying weak subjects using performance scores.

    ### 3️⃣ AI Recommendation Logic
    Rule-based classification:
    - Score < 40 → Weak
    - 40–70 → Moderate
    - > 70 → Strong

    ### 4️⃣ Productivity Methods
    - Spaced Repetition
    - Active Recall
    - Pomodoro Technique
    """)

# ---------------- PRINCIPLE ----------------
elif menu == "Principle":
    st.title("⚙ Working Principle")

    st.markdown("""
    The system follows these steps:

    1. Collect subject list and performance data.
    2. Classify subjects based on score.
    3. Allocate time proportionally.
    4. Generate AI-based improvement suggestions.
    5. Provide evaluation using quizzes.
    """)

    st.info("Future enhancement: Machine Learning model can predict performance trends.")

# ---------------- STUDY PLANNER ----------------
elif menu == "Study Planner":
    st.title("📅 Smart Timetable Generator")

    subjects = st.text_area("Enter subjects (comma separated)")
    hours = st.slider("Available study hours per day", 1, 12, 4)

    if st.button("Generate Timetable"):
        if subjects:
            subject_list = [s.strip() for s in subjects.split(",")]
            time_per_subject = hours / len(subject_list)

            st.success("Generated Study Plan")
            for subject in subject_list:
                st.write(f"📘 {subject} → {round(time_per_subject,1)} hours")
        else:
            st.warning("Please enter subjects.")

# ---------------- WEAK SUBJECT TRACKER ----------------
elif menu == "Weak Subject Tracker":
    st.title("📊 Weak Subject Performance Tracker")

    subject = st.text_input("Enter Subject Name")
    score = st.slider("Enter your score (%)", 0, 100)

    if st.button("Analyze"):
        if score < 40:
            st.error(f"{subject} is Weak ⚠️")
        elif score < 70:
            st.warning(f"{subject} Needs Improvement 📈")
        else:
            st.success(f"{subject} is Strong 💪")

        data = pd.DataFrame({"Subject":[subject], "Score":[score]})
        st.bar_chart(data.set_index("Subject"))

# ---------------- AI SUGGESTIONS ----------------
elif menu == "AI Suggestions":
    st.title("🤖 AI-Based Suggestions")

    weak_subjects = st.text_area("Enter weak subjects (comma separated)")

    if st.button("Generate Suggestions"):
        if weak_subjects:
            subject_list = [s.strip() for s in weak_subjects.split(",")]

            for subject in subject_list:
                st.write(f"📌 Focus 2 extra hours weekly on {subject}")
                st.write(f"📌 Practice active recall for {subject}")
                st.write(f"📌 Solve previous year questions of {subject}")
                st.write("---")
        else:
            st.warning("Enter at least one subject.")

# ---------------- QUIZ ----------------
elif menu == "Quiz":
    st.title("📝 Knowledge Assessment")

    score = 0

    q1 = st.radio("1️⃣ What method improves long-term memory?",
                  ["Cramming", "Spaced Repetition", "Skipping revision"])
    if q1 == "Spaced Repetition":
        score += 1

    q2 = st.radio("2️⃣ If a subject score is below 40%, it is:",
                  ["Strong", "Moderate", "Weak"])
    if q2 == "Weak":
        score += 1

    q3 = st.radio("3️⃣ Time allocation should depend on:",
                  ["Random choice", "Subject difficulty", "Mood only"])
    if q3 == "Subject difficulty":
        score += 1

    if st.button("Submit Quiz"):
        st.success(f"Your Score: {score}/3")

# ---------------- FEEDBACK ----------------
elif menu == "Feedback":
    st.title("💬 Feedback Form")

    name = st.text_input("Your Name")
    rating = st.slider("Rate this platform (1-5)", 1, 5)
    comments = st.text_area("Your Feedback")

    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")
