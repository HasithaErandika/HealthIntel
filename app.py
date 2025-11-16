import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet  

from io import BytesIO
import base64

# Check if reportlab is available
try:
    import reportlab
    reportlab_available = True
except ImportError:
    reportlab_available = False

# =============================
# CONFIGURATION
# =============================
st.set_page_config(
    page_title="Diabetes Risk Assessment Tool",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with Tailwind-inspired styling
st.markdown("""
    <style>
    .main {
        background-color: #f9fafb;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 500;
        transition: background-color 0.2s;
    }
    .stButton>button:hover {
        background-color: #2563eb;
    }
    .stSlider .stSliderLabel, .stSelectbox label {
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 8px;
    }
    .stMetric {
        background-color: #eff6ff;
        padding: 16px;
        border-radius: 8px;
        border: 1px solid #bfdbfe;
        color: black !important;
    }
    .stMetric label {
        color: black !important;
    }
    .stMetric .metric-value {
        color: black !important;
    }
    .stAlert {
        border-radius: 8px;
        padding: 16px;
    }
    .section-header {
        color: #1e40af;
        font-size: 28px;
        font-weight: 700;
        margin-top: 24px;
        margin-bottom: 16px;
    }
    .feature-group {
        background-color: #ffffff;
        padding: 16px;
        border-radius: 8px;
        border: 1px solid #e5e7eb;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model(model_path):
    try:
        model = joblib.load(model_path)
        st.write("**Model Info**")
        st.write(f"Model type: {type(model).__name__}")
        if hasattr(model, 'calibrated_classifiers_'):
            st.write(f"Calibrated classifiers: {len(model.calibrated_classifiers_)}")
            if hasattr(model.calibrated_classifiers_[0], 'base_estimator'):
                st.write(f"Base estimator: {type(model.calibrated_classifiers_[0].base_estimator).__name__}")
            else:
                st.write("No base_estimator attribute in calibrated classifier")
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

# Generate PDF report (only if reportlab is available)
def generate_pdf_report(features, probability, prediction):
    if not reportlab_available:
        return None
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Diabetes Risk Assessment Report", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Generated on: {pd.Timestamp.now()}", styles['Normal']))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Prediction Results", styles['Heading2']))
    risk = "High" if prediction == 1 else "Low"
    story.append(Paragraph(f"Diabetes Risk: {risk} ({probability:.2%} probability)", styles['Normal']))
    story.append(Paragraph(f"Recommendation: {'Order HbA1c/glucose test' if prediction == 1 else 'Continue routine monitoring'}", styles['Normal']))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Input Features", styles['Heading2']))
    for feature, value in features.items():
        story.append(Paragraph(f"{feature}: {value}", styles['Normal']))
    story.append(Spacer(1, 12))

    doc.build(story)
    buffer.seek(0)
    return buffer

# Feature input function
def get_feature_inputs():
    st.markdown("<h2 class='section-header'>🩺 Patient Information</h2>", unsafe_allow_html=True)
    st.markdown("Provide accurate patient health and demographic information for diabetes risk assessment.")

    # Demographics & Socioeconomics
    with st.expander("Demographics & Socioeconomics", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            age_cat = st.selectbox(
                "Age Category", [1, 2, 3, 4, 5, 6],
                format_func=lambda x: {
                    1: "18-24", 2: "25-34", 3: "35-44", 4: "45-54", 5: "55-64", 6: "65+"
                }[x],
                help="Age group."
            )
        with col2:
            low_income = st.selectbox(
                "Low Income", [0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help="Household income below poverty level."
            )
        with col3:
            college_graduate = st.selectbox(
                "College Graduate", [0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help="College degree or higher."
            )

    # Anthropometrics & Clinical History
    with st.expander("Anthropometrics & Clinical History", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            bmi = st.slider(
                "BMI", 15.0, 50.0, 25.0, 0.1,
                help="Body Mass Index."
            )
        with col2:
            has_high_bp = st.selectbox(
                "High Blood Pressure", [0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help="Diagnosed with high blood pressure."
            )
        with col3:
            had_cvd = st.selectbox(
                "Cardiovascular Disease", [0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help="History of CVD."
            )

    # Lifestyle & Behavior
    with st.expander("Lifestyle & Behavior", expanded=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            ever_smoked_100 = st.selectbox(
                "Ever Smoked 100 Cigarettes", [0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help="Has smoked at least 100 cigarettes in lifetime."
            )
        with col2:
            is_binge_drinker = st.selectbox(
                "Binge Drinker", [0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help="Engages in binge drinking."
            )
        with col3:
            total_fv_servings = st.slider(
                "Total Fruit/Vegetable Servings", 0, 300, 100,
                help="Total servings of fruits and vegetables."
            )
        with col4:
            alcohol_days_year = st.slider(
                "Alcohol Days per Year", 0, 365, 0,
                help="Number of days alcohol was consumed in the past year."
            )

    # Health Status & Comorbidities
    with st.expander("Health Status & Comorbidities", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            has_kidney_disease = st.selectbox(
                "Kidney Disease", [0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help="Diagnosed with kidney disease."
            )
            has_arthritis = st.selectbox(
                "Arthritis", [0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help="Diagnosed with arthritis."
            )
        with col2:
            has_depression = st.selectbox(
                "Depression", [0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help="Diagnosed with depression."
            )
            general_health_risk = st.selectbox(
                "General Health Risk", [0, 1],
                format_func=lambda x: "Low" if x == 0 else "High",
                help="General health risk level."
            )
        with col3:
            chronic_conditions_standard = st.selectbox(
                "Chronic Conditions Standard", [0, 1],
                format_func=lambda x: "<=3 Conditions" if x == 0 else ">3 Conditions",
                help="Greater than 3 chronic conditions or not."
            )
            physical_health_bad = st.selectbox(
                "Physical Health Bad", [0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help="Experiences bad physical health."
            )

    # Other Relevant Factors
    with st.expander("Other Relevant Factors", expanded=True):
        col1, _, _ = st.columns(3)
        with col1:
            lives_alone = st.selectbox(
                "Lives Alone", [0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help="Lives alone."
            )

    features = {
        'age_cat': age_cat,
        'low_income': low_income,
        'college_graduate': college_graduate,
        'BMI': bmi,
        'has_high_bp': has_high_bp,
        'had_cvd': had_cvd,
        'ever_smoked_100': ever_smoked_100,
        'is_binge_drinker': is_binge_drinker,
        'total_fv_servings': total_fv_servings,
        'alcohol_days_year': alcohol_days_year,
        'has_kidney_disease': has_kidney_disease,
        'has_arthritis': has_arthritis,
        'has_depression': has_depression,
        'general_health_risk': general_health_risk,
        'chronic_conditions_standard': chronic_conditions_standard,
        'physical_health_bad': physical_health_bad,
        'lives_alone': lives_alone
    }
    return features

# Main app
def main():
    st.title("🩺 Diabetes Risk Assessment Tool")
    st.markdown("""
    This tool uses a machine learning model trained on [CDC BRFSS](https://www.cdc.gov/brfss/) data to assess diabetes risk. 
    **Always confirm positive predictions with HbA1c or glucose tests.**
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.header("About This Tool")
        st.markdown("""
        Powered by a CatBoost machine learning model trained on BRFSS data.
        
        **Note**: This is a screening tool. Consult a healthcare provider for diagnosis.
        """)
        st.markdown("---")

    # Model path
    model_path = "models/catboost_tuned_model.joblib"
    threshold = 0.5  # Default threshold for binary classification

    # Load model
    model = load_model(model_path)
    if model is None:
        return
    st.success("✅ Model loaded successfully")

    # Feature inputs
    features = get_feature_inputs()

    # Action buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        predict_button = st.button("🔍 Assess Risk", type="primary")
    with col2:
        reset_button = st.button("🔄 Reset Inputs")

    if reset_button:
        st.rerun()

    if predict_button:
        if None in features.values():
            st.error("❌ Please fill in all feature inputs.")
            return

        with st.spinner("Calculating risk..."):
            progress_bar = st.progress(0)
            input_df = pd.DataFrame([features])
            progress_bar.progress(20)

            try:
                probability = model.predict_proba(input_df)[0, 1]
                prediction = 1 if probability >= threshold else 0
                progress_bar.progress(100)
            except Exception as e:
                st.error(f"❌ Error making prediction: {e}")
                progress_bar.progress(100)
                return

            st.markdown("<h2 class='section-header'>📊 Assessment Results</h2>", unsafe_allow_html=True)
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown("<h3>Risk Assessment</h3>", unsafe_allow_html=True)
                if prediction == 1:
                    st.error(f"🔴 **HIGH RISK**: {probability:.2%} probability of diabetes")
                    st.warning("**Recommendation**: Order HbA1c or fasting glucose test.")
                else:
                    st.success(f"🟢 **LOW RISK**: {probability:.2%} probability of diabetes")
                    st.info("**Recommendation**: Continue routine monitoring.")
                st.metric("Risk Threshold", f"50.0%", "Standard 50% threshold")

                # Probability pie chart
                st.markdown("<h3>Probability Distribution</h3>", unsafe_allow_html=True)
                fig, ax = plt.subplots(figsize=(4, 4))
                categories = ['Low Risk', 'High Risk']
                probs = [1 - probability, probability]
                colors = ['green', 'red']
                ax.pie(probs, labels=categories, colors=colors, autopct='%1.1f%%', startangle=90)
                ax.axis('equal')
                st.pyplot(fig)

            with col2:
                st.markdown("<h3>Model Prediction Details</h3>", unsafe_allow_html=True)
                # Feature importances
                importances = model.get_feature_importance()
                feature_names = input_df.columns
                imp_df = pd.DataFrame({'feature': feature_names, 'importance': importances})
                imp_df = imp_df.sort_values('importance', ascending=False).head(10)
                fig2, ax2 = plt.subplots(figsize=(4, 5))
                ax2.barh(imp_df['feature'], imp_df['importance'], color='blue')
                ax2.set_xlabel('Importance')
                ax2.invert_yaxis()
                st.pyplot(fig2)

            if reportlab_available:
                pdf_buffer = generate_pdf_report(features, probability, prediction)
                if pdf_buffer:
                    st.download_button(
                        "📥 Download Report",
                        data=pdf_buffer,
                        file_name="diabetes_risk_report.pdf",
                        mime="application/pdf"
                    )

    st.markdown("---")
    st.markdown("""
    **Disclaimer**: This is a screening tool, not a diagnostic test. Always confirm results with clinical tests (e.g., HbA1c, fasting glucose) and consult a healthcare provider.
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()