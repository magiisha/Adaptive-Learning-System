import streamlit as st
import matplotlib.pyplot as plt
import time

if st.button("🚀 Analyze Performance"):
    with st.spinner("Analyzing your performance..."):
        time.sleep(1.5)

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

st.markdown("### 📊 Score Comparison")

st.bar_chart(scores)

highest = subjects[scores.index(max(scores))]
lowest = subjects[scores.index(min(scores))]

st.markdown("### 🔍 Insights")
st.write(f"🏆 Strongest Subject: {highest}")
st.write(f"⚠️ Needs Attention: {lowest}")

st.set_page_config(layout="wide")

# Page config
st.set_page_config(page_title="Adaptive Learning System", layout="centered")

st.title("📘 Adaptive Learning System using AI-driven Analytics")

st.markdown("### 📥 Enter Subjects and Scores")

# Number of subjects
num_subjects = st.number_input("Enter number of subjects", min_value=1, max_value=10, value=3)

subjects = []
scores = []

# Dynamic input
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

        # Results
        st.markdown("## 📊 Results")
        st.markdown(f"<h3 style='color:{color};'>Performance: {performance}</h3>", unsafe_allow_html=True)

        st.metric("📈 Overall Score", f"{total_score} / {max_score}")
        st.metric("📊 Percentage", f"{round(percentage,2)}%")

        # Pie Chart
        st.markdown("### 📊 Subject-wise Distribution")
        fig, ax = plt.subplots()
        ax.pie(scores, labels=subjects, autopct='%1.1f%%')
        st.pyplot(fig)

        # Smart Recommendations (NOT basic 🔥)
        st.markdown("### 🧠 Study Plan")

        weak_subjects = [subjects[i] for i in range(len(scores)) if scores[i] < 60]

        if weak_subjects:
            for sub in weak_subjects:
                st.write(f"📌 For **{sub}**:")
                st.write("- Focus on completing pending syllabus topics")
                st.write("- Practice previous year questions")
                st.write("- Allocate 1 hour daily for revision")
                st.write("- Take weekly mock tests")
        else:
            st.success("🎉 You are performing well across all subjects. Focus on advanced practice!")

st.markdown("---")
st.markdown("<center>Made with ❤️ using AI-driven Analytics</center>", unsafe_allow_html=True)
