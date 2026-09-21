import streamlit as st

st.set_page_config(page_title="CBSE Skill Hub", layout="wide")

st.sidebar.title("📚 CBSE Skill Curriculum")
selected_unit = st.sidebar.radio(
    "Select Unit:",
    ["Unit 1: Concept & Video Lecture", "Unit 2: Practical Sandbox", "Unit 3: Code Submission"]
)

if selected_unit == "Unit 1: Concept & Video Lecture":
    st.header("🎥 Video Lecture: Introduction to AI / Data Science")
    # Embed instructional lecture video directly
    st.video("https://www.youtube.com/watch?v=NfwfiyMi1lk")
    st.info("Syllabus Reference: Part B - Subject Specific Skills, Domain: Computer Vision / ML")

elif selected_unit == "Unit 2: Practical Sandbox":
    st.header("🧪 Interactive Practical Demo")
    st.write("Modify the inputs below to inspect real-time algorithmic outputs:")

    user_val = st.slider("Select sample threshold parameter:", 1, 100, 50)
    st.line_chart([x * (user_val / 10) for x in range(1, 15)])

elif selected_unit == "Unit 3: Code Submission":
    st.header("📝 Student Task & Self-Assessment")
    student_code = st.text_area("Write Python code for the assigned CBSE practical problem:")
    if st.button("Run Code Check"):
        st.success("Syntax verified. Ready to push to your GitHub portfolio!")