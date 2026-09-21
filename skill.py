import streamlit as st

st.set_page_config(page_title="CBSE Skill Training Portal", layout="wide", page_icon="🎓")

# पाठ्यक्रम और 5-5 वीडियो मॉड्यूल्स का डेटा डिक्शनरी
COURSE_DATA = {
    "Class 6 to 8 (Middle Level)": {
        "Artificial Intelligence (AI)": [
            {"title": "Module 1: What is AI & Smart Machines", "url": "https://www.youtube.com/watch?v=2ePf9rue1Ao", "practical": "Interactive AI vs Human Activity: List 3 daily devices that use AI."},
            {"title": "Module 2: Human Intelligence vs AI", "url": "https://www.youtube.com/watch?v=ad79nYk2keg", "practical": "Compare decision-making flow between human reflex and machine rule."},
            {"title": "Module 3: Basics of Computer Vision (How machines see)", "url": "https://www.youtube.com/watch?v=OcycT1JwsYo", "practical": "Test quick-draw or Google Teachable Machine image classification."},
            {"title": "Module 4: Natural Language Processing (Talking to AI)", "url": "https://www.youtube.com/watch?v=fOvTtapxa9c", "practical": "Create a rule-based chatbot script for greeting responses."},
            {"title": "Module 5: AI Ethics & Digital Responsibility", "url": "https://www.youtube.com/watch?v=GboOXRhFzWA", "practical": "Case Study: Identify bias in automated school attendance cameras."}
        ],
        "Marketing": [
            {"title": "Module 1: Introduction to Goods and Services", "url": "https://www.youtube.com/watch?v=q6P30mODNyo", "practical": "Identify 5 goods and 5 services available around your neighborhood."},
            {"title": "Module 2: The 4 Ps of Marketing (Product, Price, Place, Promotion)", "url": "https://www.youtube.com/watch?v=Mco8vBAwOmA", "practical": "Design a 4P chart for an eco-friendly student pencil."},
            {"title": "Module 3: Understanding Customer Needs", "url": "https://www.youtube.com/watch?v=x7E26gY3Oac", "practical": "Conduct a mock survey with 3 classmates about canteen food preferences."},
            {"title": "Module 4: Designing a Creative Poster / Advertisement", "url": "https://www.youtube.com/watch?v=0kEeVb1_XjA", "practical": "Draft a creative slogan and logo for a handmade paper notebook."},
            {"title": "Module 5: Digital Selling & Online Safety", "url": "https://www.youtube.com/watch?v=y2X7CeD-2L4", "practical": "Create a safe-seller checklist for online e-commerce transactions."}
        ],
        "Coding": [
            {"title": "Module 1: Understanding Algorithms & Flowcharts", "url": "https://www.youtube.com/watch?v=eSYeHlwDCNA", "practical": "Draw a step-by-step flowchart to make tea or sharpen a pencil."},
            {"title": "Module 2: Block-Based Coding Concepts (Scratch)", "url": "https://www.youtube.com/watch?v=Z1KKzN_fG0U", "practical": "Create an animation of a sprite moving across the screen on keypress."},
            {"title": "Module 3: Loops and Repetition", "url": "https://www.youtube.com/watch?v=QvyTEx1JOUQ", "practical": "Write a loop program to print multiplication tables from 1 to 5."},
            {"title": "Module 4: Conditionals (If-Else Logic)", "url": "https://www.youtube.com/watch?v=1oEQqHj3Y-s", "practical": "Build a simple game condition: IF score >= 10 THEN Win, ELSE Keep Playing."},
            {"title": "Module 5: Mini Project: Simple Catch Game", "url": "https://www.youtube.com/watch?v=hK8N2bT-3qM", "practical": "Assemble a complete sprite catch game with score tracking."}
        ]
    },
    "Class 9 & 10 (Secondary Level)": {
        "Information Technology (IT - Code 402)": [
            {"title": "Module 1: Communication Skills (Verbal & Non-Verbal)", "url": "https://www.youtube.com/watch?v=NGb9RIB8N7c", "practical": "Draft an email format following professional digital etiquette."},
            {"title": "Module 2: Self-Management & ICT Skills", "url": "https://www.youtube.com/watch?v=4b72AuRzYg0", "practical": "File management lab: Organize files into hierarchical folders."},
            {"title": "Module 3: Digital Documentation (Word Processing)", "url": "https://www.youtube.com/watch?v=4q48bWJ6GgU", "practical": "Format a 2-page project report with Table of Contents and Headings."},
            {"title": "Module 4: Electronic Spreadsheet (Excel/Calc Basics)", "url": "https://www.youtube.com/watch?v=8VnZ6U-yWqI", "practical": "Calculate student total marks, average, and grade using SUM and AVERAGE."},
            {"title": "Module 5: Digital Presentation & Slide Transitions", "url": "https://www.youtube.com/watch?v=1hNlZtW5zEQ", "practical": "Prepare a 5-slide presentation on Cyber Safety with custom animations."}
        ],
        "Food Production (Code 409)": [
            {"title": "Module 1: Kitchen Hygiene & Food Safety Standards", "url": "https://www.youtube.com/watch?v=aG_jZ2wYm_Q", "practical": "List personal hygiene rules and write a sanitization protocol for cookware."},
            {"title": "Module 2: Kitchen Equipment & Tool Identification", "url": "https://www.youtube.com/watch?v=cM3uYfQ3PjA", "practical": "Classify 10 kitchen tools into cutting, cooking, and measuring gear."},
            {"title": "Module 3: Basic Cooking Methods (Boiling, Roasting, Steaming)", "url": "https://www.youtube.com/watch?v=8gXGv9yXyM8", "practical": "Compare nutrients preserved in steaming versus deep frying in a table."},
            {"title": "Module 4: Culinary Knife Skills & Vegetable Cuts", "url": "https://www.youtube.com/watch?v=Ydc_SaQ_eCE", "practical": "Demonstrate Julienne, Batonnet, and Dicing cuts on potatoes/carrots."},
            {"title": "Module 5: Menu Planning & Balanced Nutritious Meal", "url": "https://www.youtube.com/watch?v=5rLzW8yVvB8", "practical": "Plan a 3-course balanced lunch menu for school athletes."}
        ],
        "Artificial Intelligence (AI - Code 417)": [
            {"title": "Module 1: AI Project Cycle (Problem Scoping & Acquisition)", "url": "https://www.youtube.com/watch?v=uC0_5eR8aZw", "practical": "Create a 4Ws canvas (Who, What, Where, Why) for a traffic management issue."},
            {"title": "Module 2: Data Exploration & Representation", "url": "https://www.youtube.com/watch?v=jW94Fv_gX88", "practical": "Visualize simple numeric datasets using Matplotlib bar charts in Python."},
            {"title": "Module 3: Introduction to Python for AI", "url": "https://www.youtube.com/watch?v=rfscVS0vtbw", "practical": "Write Python code using lists and loops to calculate average test scores."},
            {"title": "Module 4: Computer Vision & Convolutional Concept", "url": "https://www.youtube.com/watch?v=2-Ol7ZB0GmU", "practical": "Load and inspect image dimensions/pixels using OpenCV or PIL."},
            {"title": "Module 5: AI Evaluation Metrics & Confusion Matrix", "url": "https://www.youtube.com/watch?v=Kdsp6soqA7g", "practical": "Calculate Precision, Recall, and Accuracy from a 2x2 confusion matrix."}
        ]
    },
    "Class 11 & 12 (Senior Secondary Level)": {
        "Information Technology (IT - Code 802)": [
            {"title": "Module 1: Computer Organization & Operating Systems", "url": "https://www.youtube.com/watch?v=vBURTt97EkA", "practical": "Configure environment variables and check OS system resources via CLI."},
            {"title": "Module 2: Relational Database Concepts & SQL Queries", "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY", "practical": "Write SQL statements: CREATE TABLE, INSERT INTO, and SELECT WHERE."},
            {"title": "Module 3: Advanced Java / OOP Fundamentals", "url": "https://www.youtube.com/watch?v=grEKMHGYyns", "practical": "Create a Student class with encapsulated attributes and getter/setter methods."},
            {"title": "Module 4: Web Applications & Client-Server Architecture", "url": "https://www.youtube.com/watch?v=2JYT5f2S74k", "practical": "Build an HTML5 registration form with client-side form validation."},
            {"title": "Module 5: Network Protocols & Cybersecurity Best Practices", "url": "https://www.youtube.com/watch?v=1V_4-45wZvg", "practical": "Trace packet routes using `ping` and `traceroute` commands."}
        ],
        "Financial Markets Management (Code 805)": [
            {"title": "Module 1: Overview of Indian Financial System & Regulators", "url": "https://www.youtube.com/watch?v=cb8so2DCkJg", "practical": "Map the roles of RBI, SEBI, and IRDAI in a single flow diagram."},
            {"title": "Module 2: Primary Markets vs Secondary Markets", "url": "https://www.youtube.com/watch?v=BfgEm17KEKM", "practical": "Document the process of an IPO from prospectus release to share listing."},
            {"title": "Module 3: Trading Mechanism & Demat Account Workflow", "url": "https://www.youtube.com/watch?v=QTV1_kRQm3s", "practical": "Simulate placing market and limit orders on a paper-trading portal."},
            {"title": "Module 4: Mutual Funds & Systematic Investment Plans (SIP)", "url": "https://www.youtube.com/watch?v=5rCbg6kS0jA", "practical": "Calculate 10-year compound returns for a monthly SIP of ₹1000."},
            {"title": "Module 5: Risk Management & Derivatives Basics", "url": "https://www.youtube.com/watch?v=7uV89w0_xKw", "practical": "Compare Equity Futures vs Options Call/Put payoff profiles."}
        ],
        "Yoga (Code 841)": [
            {"title": "Module 1: Philosophy & Origin of Yogic Sciences", "url": "https://www.youtube.com/watch?v=v7AYKMP6rOE", "practical": "Prepare a comparative chart on Ashtanga Yoga's 8 limbs (Yama to Samadhi)."},
            {"title": "Module 2: Shatkarma & Cleansing Techniques", "url": "https://www.youtube.com/watch?v=m756Gz8kI9Y", "practical": "Write safety precautions and physiological benefits for Jal Neti and Kapalbhati."},
            {"title": "Module 3: Asanas for Postural Alignment & Spine Health", "url": "https://www.youtube.com/watch?v=sTANio_2E0Q", "practical": "Step-by-step documentation of Surya Namaskar's 12 postures with breathing."},
            {"title": "Module 4: Pranayama & Respiratory Vitality", "url": "https://www.youtube.com/watch?v=1xRX1MuoqSc", "practical": "Perform 5 minutes of Anulom-Vilom; record resting heart rate before and after."},
            {"title": "Module 5: Yogic Diet (Mitahara) & Stress Reduction", "url": "https://www.youtube.com/watch?v=txkZzT2n6m4", "practical": "Design a daily Sattvic meal chart aligned with CBSE wellness guidelines."}
        ],
        "Artificial Intelligence (Code 843)": [
            {"title": "Module 1: Machine Learning Workflows & Regression", "url": "https://www.youtube.com/watch?v=ukzFI9rgwfU", "practical": "Implement Linear Regression using Python Scikit-learn on a housing price dataset."},
            {"title": "Module 2: Data Preprocessing & Feature Engineering", "url": "https://www.youtube.com/watch?v=bDhvCp3_lYw", "practical": "Handle missing values and apply standard normalization on a CSV dataset."},
            {"title": "Module 3: Classification Algorithms (Decision Trees & KNN)", "url": "https://www.youtube.com/watch?v=Rmajwe65u70", "practical": "Train a Decision Tree Classifier on the Iris flower dataset and plot the tree."},
            {"title": "Module 4: Neural Networks & Deep Learning Foundations", "url": "https://www.youtube.com/watch?v=aircAruvnKk", "practical": "Build a single-layer perceptron model to simulate binary logic gates."},
            {"title": "Module 5: Capstone AI Model Deployment", "url": "https://www.youtube.com/watch?v=NfwfiyMi1lk", "practical": "Connect your trained ML model to a Streamlit interactive web interface."}
        ]
    }
}

# --- साइडबार नेविगेशन ---
st.sidebar.title("🏫 CBSE Skill Education Portal")
selected_class_group = st.sidebar.selectbox("1. Class Group चुनें:", list(COURSE_DATA.keys()))

available_subjects = list(COURSE_DATA[selected_class_group].keys())
selected_subject = st.sidebar.selectbox("2. Subject चुनें:", available_subjects)

modules = COURSE_DATA[selected_class_group][selected_subject]
module_titles = [m["title"] for m in modules]
selected_module_title = st.sidebar.radio("3. Module चुनें (5 Modules):", module_titles)

# सेलेक्टेड मॉड्यूल का डेटा निकालना
current_module = next(m for m in modules if m["title"] == selected_module_title)

# --- मुख्य स्क्रीन डिस्प्ले ---
st.title(f"{selected_subject}")
st.caption(f"Category: {selected_class_group} | CBSE Skill Framework")
st.markdown("---")

col1, col2 = st.columns([3, 2])

with col1:
    st.subheader(f"🎥 {current_module['title']}")
    st.video(current_module["url"])

with col2:
    st.subheader("🧪 Practical Lab Task")
    st.info(current_module["practical"])
    
    st.write("#### ✍️ Student Submission Sandbox")
    student_notes = st.text_area("विद्यार्थी अपना हल या ऑब्जर्वेशन यहाँ लिखें:", height=150)
    
    uploaded_file = st.file_uploader("प्रैक्टिकल फ़ाइल/स्क्रीनशॉट अपलोड करें (PDF/PNG):", type=["png", "jpg", "pdf", "py"])
    
    if st.button("Submit Practical Work"):
        if student_notes or uploaded_file:
            st.success("✅ कार्य सफलतापूर्वक सबमिट हो गया है!")
        else:
            st.warning("कृपया सबमिट करने से पहले टेक्स्ट लिखें या फ़ाइल अटैच करें।")

st.markdown("---")
st.subheader("📊 Course Progress Tracker")
progress_val = (module_titles.index(selected_module_title) + 1) / len(module_titles)
st.progress(progress_val)
st.write(f"Completed {module_titles.index(selected_module_title) + 1} of 5 Modules")
