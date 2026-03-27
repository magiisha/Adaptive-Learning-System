import streamlit as st
import matplotlib.pyplot as plt
import time

# ✅ MUST BE FIRST (only once)
st.set_page_config(page_title="Adaptive Learning System", layout="wide")

# 🎨 UI Styling
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
h1 {
    text-align: center;
    color: #00ffd5;
}
.stButton>button {
    background-color: #00ffd5;
    color: black;
    border-radius: 12px;
    font-size: 18px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("📘 Adaptive Learning System")

st.markdown("### 📥 Enter Subjects and Scores")

# Number of subjects
num_subjects = st.number_input("Enter number of subjects", min_value=1, max_value=10, value=3)

subjects = []
scores = []

# Dynamic inputs
for i in range(num_subjects):
    col1, col2 = st.columns(2)
    
    with col1:
        subject = st.text_input(f"Subject {i+1} Name", key=f"sub{i}")
    with col2:
        score = st.number_input(f"{subject if subject else 'Score'}", 0, 100, key=f"score{i}")
    
    if subject:
        subjects.append(subject)
        scores.append(score)

st.markdown("---")

if st.button("🚀 Analyze Performance"):
    
    if len(subjects) == 0:
        st.warning("Please enter at least one subject")
    
    else:
        with st.spinner("🔍 AI analyzing your performance..."):
            time.sleep(1.5)

            total_score = sum(scores)
            max_score = len(scores) * 100
            percentage = total_score / max_score * 100
            
            # Performance classification
            if percentage >= 75:
                performance = "Good"
                color = "green"
            elif percentage >= 50:
                performance = "Average"
                color = "orange"
            else:
                performance = "Poor"
                color = "red"

        # 🎯 RESULT CARD
        st.markdown("## 📊 Results")
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #1f4037, #99f2c8);
            padding:20px;
            border-radius:15px;
            text-align:center;
            box-shadow:0px 0px 15px rgba(0,0,0,0.3);
        ">
            <h2 style="color:black;">Performance: {performance}</h2>
            <h3>Score: {total_score}/{max_score}</h3>
            <h3>Percentage: {round(percentage,2)}%</h3>
        </div>
        """, unsafe_allow_html=True)

        # 📊 ANALYTICS SECTION
        st.markdown("## 📊 Performance Analytics")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🥧 Subject Distribution")
            fig, ax = plt.subplots()
            ax.pie(scores, labels=subjects, autopct='%1.1f%%')
            st.pyplot(fig)

        with col2:
            st.markdown("### 📊 Score Comparison")
            st.bar_chart(scores)

        # 🔍 INSIGHTS
        highest = subjects[scores.index(max(scores))]
        lowest = subjects[scores.index(min(scores))]

        st.markdown("### 🔍 Insights")
        st.write(f"🏆 Strongest Subject: {highest}")
        st.write(f"⚠️ Needs Attention: {lowest}")

        # 📊 PROGRESS BAR
        st.markdown("### 📊 Performance Level")
        st.progress(int(percentage))

        # 🧠 SMART STUDY PLAN
        st.markdown("### 🧠 Personalized Study Plan")

        weak_subjects = [subjects[i] for i in range(len(scores)) if scores[i] < 60]

        if weak_subjects:
            for sub in weak_subjects:
                st.write(f"📘 **{sub} Study Plan:**")
                st.write("- Complete pending syllabus topics")
                st.write("- Practice 10–15 problems daily")
                st.write("- Revise concepts every 2 days")
                st.write("- Take weekly mock tests")
        else:
            st.success("🎉 Excellent performance! Focus on advanced learning.")

        # 📅 WEEKLY PLAN
        st.markdown("### 📅 Weekly Study Schedule")
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        for i, day in enumerate(days):
            subject = subjects[i % len(subjects)]
            st.write(f"{day}: Study {subject} for 1–2 hours")

st.markdown("---")
st.markdown("<center>Made with ❤️ using AI-driven Analytics</center>", unsafe_allow_html=True)
