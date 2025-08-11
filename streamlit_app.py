import streamlit as st
import pickle
import re
import numpy as np
import pandas as pd
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="Resume Category Predictor",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 3rem;
    }
    
    .prediction-box {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        border: 1px solid #c3e6cb;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        text-align: center;
    }
    
    .category-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.2rem;
        display: inline-block;
        margin: 10px 0;
    }
    
    .error-box {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
        border: 1px solid #f5c6cb;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        text-align: center;
        color: #721c24;
    }
    
    .info-box {
        background: #f8f9fa;
        border-left: 4px solid #667eea;
        padding: 15px;
        margin: 20px 0;
        border-radius: 5px;
    }
    
    /* Text area styling for better visibility */
    .stTextArea > div > div > textarea {
        background-color: white !important;
        border: 2px solid #e1e5e9 !important;
        border-radius: 10px !important;
        padding: 15px !important;
        color: #333 !important;
        font-size: 14px !important;
        line-height: 1.5 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
        background-color: white !important;
    }
    
    .stTextArea > div > div > textarea:hover {
        background-color: #fafafa !important;
        border-color: #667eea !important;
    }
    
    .stTextArea > div > div > textarea::placeholder {
        color: #999 !important;
        opacity: 1 !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 15px 30px;
        font-weight: bold;
        font-size: 1.1rem;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
    }
    
    .sample-btn {
        background: #667eea;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 6px;
        font-size: 0.9rem;
        cursor: pointer;
        margin-top: 10px;
        transition: background 0.3s ease;
    }
    
    .sample-btn:hover {
        background: #5a6fd8;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_models():
    """Load the trained models"""
    try:
        with open('tfidf.pkl', 'rb') as f:
            tfidf = pickle.load(f)
        with open('clf.pkl', 'rb') as f:
            clf = pickle.load(f)
        with open('encoder.pkl', 'rb') as f:
            le = pickle.load(f)
        return tfidf, clf, le
    except FileNotFoundError:
        st.error("❌ Model files not found! Please ensure tfidf.pkl, clf.pkl, and encoder.pkl are in the current directory.")
        st.stop()

def cleanResume(txt):
    """Clean resume text by removing URLs, special characters, etc."""
    cleanTxt = re.sub(r'http\S+\s*', '', txt)
    cleanTxt = re.sub(r'RT|cc', '', cleanTxt)
    cleanTxt = re.sub(r'#\S+', '', cleanTxt)
    cleanTxt = re.sub(r'@\S+', '', cleanTxt)
    cleanTxt = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', cleanTxt)
    cleanTxt = re.sub(r'\s+', ' ', cleanTxt)
    cleanTxt = re.sub(r'([^\s\w]|_)+', '', cleanTxt)
    cleanTxt = re.sub(r'\d+', '', cleanTxt)
    cleanTxt = re.sub(r'^\s+|\s+$', '', cleanTxt)
    return cleanTxt

def predict_category(resume_text, tfidf, clf, le):
    """Predict the category of a resume"""
    try:
        # Clean the resume text
        cleaned_text = cleanResume(resume_text)
        
        # Vectorize the cleaned text
        vectorized_text = tfidf.transform([cleaned_text])
        
        # Convert sparse matrix to dense
        vectorized_text = vectorized_text.toarray()
        
        # Make prediction
        predicted_category = clf.predict(vectorized_text)
        
        # Get the category name
        predicted_category_name = le.inverse_transform(predicted_category)
        
        return predicted_category_name[0]
    except Exception as e:
        return f"Error in prediction: {str(e)}"

def get_sample_resume():
    """Return a sample resume for testing"""
    return """JOHN DOE
Software Engineer
john.doe@email.com | (555) 123-4567 | linkedin.com/in/johndoe

PROFESSIONAL SUMMARY
Experienced software engineer with 5+ years of expertise in full-stack development, specializing in Python, JavaScript, and cloud technologies. Proven track record of delivering scalable solutions and leading development teams.

TECHNICAL SKILLS
• Programming Languages: Python, JavaScript, Java, C++
• Web Technologies: React, Node.js, Django, Flask
• Databases: PostgreSQL, MongoDB, MySQL
• Cloud Platforms: AWS, Azure, Google Cloud
• Tools: Git, Docker, Kubernetes, Jenkins

WORK EXPERIENCE
Senior Software Engineer | TechCorp Inc. | 2020 - Present
• Led development of microservices architecture serving 1M+ users
• Implemented CI/CD pipelines reducing deployment time by 60%
• Mentored junior developers and conducted code reviews

Software Developer | StartupXYZ | 2018 - 2020
• Developed RESTful APIs using Python Flask and Django
• Built responsive web applications using React and Node.js
• Collaborated with cross-functional teams in agile environment

EDUCATION
Bachelor of Science in Computer Science
University of Technology | 2014 - 2018
GPA: 3.8/4.0

PROJECTS
• E-commerce Platform: Full-stack application with React frontend and Python backend
• Machine Learning Dashboard: Real-time data visualization using Python and D3.js
• Mobile App: Cross-platform app using React Native and Firebase

CERTIFICATIONS
• AWS Certified Solutions Architect
• Google Cloud Professional Developer
• Certified Scrum Master (CSM)"""

def main():
    # Load models
    tfidf, clf, le = load_models()
    
    # Header
    st.markdown('<h1 class="main-header">📄 Resume Category Predictor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Upload your resume text and get instant category predictions using AI</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("""
        This application uses machine learning to predict job categories from resume text.
        
        **How it works:**
        1. Text preprocessing
        2. Feature extraction (TF-IDF)
        3. AI prediction
        4. Category classification
        
        **Supported categories:**
        - Data Science
        - Python Developer
        - Java Developer
        - Web Designing
        - DevOps Engineer
        - And many more...
        """)
        
        st.header("📊 Model Info")
        st.info(f"**Total Categories:** {len(le.classes_)}")
        
        # Display all categories
        st.subheader("Available Categories:")
        categories_df = pd.DataFrame(le.classes_, columns=['Categories'])
        st.dataframe(categories_df, use_container_width=True)
    
    # Main content
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Resume input
        st.subheader("📝 Enter Your Resume Text")
        
        # Sample resume button
        if st.button("📋 Load Sample Resume", help="Load a sample resume for testing"):
            st.session_state.resume_text = get_sample_resume()
        
        # Text area for resume input
        resume_text = st.text_area(
            "Paste your resume text here...",
            value=st.session_state.get('resume_text', ''),
            height=300,
            placeholder="Include your skills, experience, education, and any relevant information...",
            help="The more detailed your resume, the better the prediction accuracy"
        )
        
        # Character count
        char_count = len(resume_text) if resume_text else 0
        st.caption(f"📊 Character count: {char_count}")
        
        # Prediction button
        if st.button("🔮 Predict Category", type="primary"):
            if not resume_text.strip():
                st.error("❌ Please enter your resume text.")
            else:
                with st.spinner("🤖 Analyzing your resume..."):
                    predicted_category = predict_category(resume_text, tfidf, clf, le)
                
                if predicted_category.startswith("Error"):
                    st.markdown(f'<div class="error-box"><h3>❌ Error</h3><p>{predicted_category}</p></div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'''
                    <div class="prediction-box">
                        <h3>✅ Prediction Result</h3>
                        <p>Your resume is predicted to belong to the category:</p>
                        <div class="category-badge">{predicted_category}</div>
                    </div>
                    ''', unsafe_allow_html=True)
                    
                    # Show confidence info
                    st.info("💡 **Note:** This prediction is based on the patterns learned from the training data. For best results, ensure your resume contains relevant keywords and skills for the target category.")
        


if __name__ == "__main__":
    main()
