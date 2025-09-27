# HealthIntel

🩺 **AI-powered predictive intelligence for diabetes risk screening and education**

HealthIntel is a machine learning-based health screening tool designed for diabetes risk assessment using the Behavioral Risk Factor Surveillance System (BRFSS) dataset. The project includes comprehensive data processing, feature engineering, and model development workflows through Jupyter notebooks, with a Streamlit web application for risk prediction.

⚠️ **Important**: This tool is for educational and research purposes only. It is not a medical device and does not provide medical advice. Always consult qualified healthcare professionals for diagnosis and treatment.

## ✨ Key Features

- **📊 Comprehensive Data Processing Pipeline**: Complete BRFSS dataset analysis from raw data to model-ready features
- **🔬 Research-Ready Notebooks**: Extensive Jupyter notebooks covering EDA, feature engineering, and model development
- **🖥️ Interactive Streamlit Web App**: User-friendly interface for diabetes risk assessment
- **🔍 Model Explainability**: SHAP (SHapley Additive exPlanations) integration for transparent predictions
- **📈 Statistical Feature Selection**: Chi-square and correlation-based feature selection methods
- **📋 PDF Report Generation**: Downloadable assessment reports with explanations
- **🛡️ Privacy-First Design**: All computations performed locally, no data transmission

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ (tested with 3.10-3.12)
- Windows/macOS/Linux
- 8GB+ RAM recommended for model loading

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd HealthIntel
```

2. **Create virtual environment**
```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows Command Prompt
.venv\Scripts\activate.bat

# macOS/Linux
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Set up data** (Optional - for notebook development)
   - Download BRFSS datasets as specified in `datasetLocations.txt`
   - Place raw data in `data/raw/` directory

5. **Run the application**
```bash
streamlit run app.py
```

6. **Open your browser** to the displayed URL (typically `http://localhost:8501`)

**Note**: The models directory is currently empty. You'll need to train models using the provided notebooks or add pre-trained models to use the Streamlit application.

## 📁 Project Structure

```text
HealthIntel/
├── app.py                                    # 🖥️ Main Streamlit web application
├── README.md                                 # 📖 Project documentation
├── requirements.txt                          # 📦 Python dependencies
├── datasetLocations.txt                      # 📍 Dataset sources and structure
├── data/                                     # 📊 Data storage
│   ├── raw/                                 # Original BRFSS CSV files (2011-2015)
│   ├── processed/                           # Cleaned and engineered datasets
│   └── train-test/                          # Training and testing splits
├── models/                                   # 🤖 Trained ML models (currently empty)
├── results/                                  # 📈 Model results and metrics (currently empty)
└── notebooks/                               # 📊 Jupyter notebooks for research
    ├── 01_data_merging_and_exploratory_analysis.ipynb
    ├── 02_feature_engineering.ipynb
    ├── 03_target_focused_dataset_preparation.ipynb
    ├── 04_statistical_feature_selection.ipynb
    ├── 05_final_preprocessing_and_train_test_split.ipynb (empty)
    ├── 06_baseline_models.ipynb (empty)
    ├── 07_hyperparameter_tuning.ipynb (empty)
    ├── 08_model_evaluation.ipynb (empty)
    ├── Diabetics_ModelTraining.ipynb        # Comprehensive model training
    ├── EDA.ipynb                           # Exploratory Data Analysis
    └── IT24100886_Impute_Cleaning_ChiSQR.ipynb
```

### Key Components

- **`app.py`**: Main Streamlit application with diabetes risk assessment interface
- **`data/`**: BRFSS dataset storage with raw, processed, and train-test splits
- **`notebooks/`**: Research notebooks covering complete ML pipeline from EDA to model training
- **`requirements.txt`**: All required Python packages and dependencies
- **`datasetLocations.txt`**: Documentation of data sources and folder structure
- **`models/`**: Directory for trained models (currently empty - models need to be trained)
- **`results/`**: Directory for model performance metrics and results

## 🖥️ Web Application Features

### 📝 Input Parameters (20 Features)

The diabetes risk model evaluates 20 key health and demographic factors:

## 🖥️ Web Application

### Current Status
The Streamlit application (`app.py`) is ready for diabetes risk assessment but requires trained models to function properly. The app is designed to work with various ML models and includes comprehensive SHAP explainability features.

### 📏 Input Parameters (20 Features)

The diabetes risk model is designed to evaluate 20 key health and demographic factors:

**🏥 Clinical History**
- Chronic condition count (0-10)
- Metabolic risk score (Low/Medium/High)
- Blood pressure medication status
- High cholesterol diagnosis
- Cardiovascular conditions count
- Kidney disease history

**💪 Health Status**
- General health self-assessment (Excellent to Poor)
- Physical health bad days (categorical)
- Health-limited activity days
- Functional limitations due to health

**🫀 Medical History**
- Coronary heart disease
- Heart attack history
- Pneumonia vaccination
- Arthritis diagnosis
- Cancer screening compliance

**👤 Demographics & Access**
- Age (21-82 years)
- Income level (8 categories)
- Education level (6 categories)
- Last routine checkup
- Last cholesterol check

### 📊 Planned Outputs & Results

Once models are trained, the application will provide:

- **🎯 Risk Classification**: Low/High risk with probability percentage
- **📈 Model Performance**: Real-time display of sensitivity, specificity, precision, and AUC
- **🔍 SHAP Explanations**: 
  - Waterfall plots showing feature contributions
  - Force plots visualizing decision factors
  - Top 5 contributing factors with impact direction
- **📄 PDF Reports**: Downloadable assessment reports with complete analysis

### Getting Started with the App

1. **Train Models First**: Use the notebook pipeline to create trained models
2. **Save Models**: Export models to the `models/` directory
3. **Run Application**: `streamlit run app.py`
4. **Test Interface**: Input health parameters and review risk assessment

## 🤖 Models & Development Pipeline

### Model Development Status

**Current State**: The project includes comprehensive data processing and model development notebooks, but trained models are not yet available in the repository.

### Available Development Notebooks

1. **Data Processing Pipeline**:
   - `01_data_merging_and_exploratory_analysis.ipynb`: Data merging and initial EDA
   - `02_feature_engineering.ipynb`: Comprehensive feature engineering (3.2MB)
   - `03_target_focused_dataset_preparation.ipynb`: Target variable preparation
   - `04_statistical_feature_selection.ipynb`: Feature selection using statistical methods

2. **Model Development**:
   - `Diabetics_ModelTraining.ipynb`: Main model training notebook (1.1MB)
   - `EDA.ipynb`: Extensive exploratory data analysis (7.4MB)
   - `IT24100886_Impute_Cleaning_ChiSQR.ipynb`: Data imputation and Chi-square analysis

3. **Planned Notebooks** (currently empty):
   - `05_final_preprocessing_and_train_test_split.ipynb`
   - `06_baseline_models.ipynb`
   - `07_hyperparameter_tuning.ipynb`
   - `08_model_evaluation.ipynb`

### To Train Models

1. **Set up data**: Follow instructions in `datasetLocations.txt`
2. **Run notebooks sequentially**: Start with data processing, then model training
3. **Save trained models**: Export to `models/` directory for use with Streamlit app

### Expected Model Types

Based on the Streamlit app code, the following models are supported:
- XGBoost (with TreeExplainer for SHAP)
- CatBoost
- Random Forest
- Extra Trees
- Stacking Ensemble
- Other scikit-learn compatible models

"

## 📊 Research & Development

### 📓 Jupyter Notebooks

The `notebooks/` directory contains comprehensive research workflows:

**Data Processing Pipeline**:
- **`01_data_merging_and_exploratory_analysis.ipynb`**: Initial data merging and exploratory analysis
- **`02_feature_engineering.ipynb`**: Comprehensive feature engineering (largest notebook - 3.2MB)
- **`03_target_focused_dataset_preparation.ipynb`**: Target variable preparation and dataset focusing
- **`04_statistical_feature_selection.ipynb`**: Statistical feature selection methods

**Model Development**:
- **`Diabetics_ModelTraining.ipynb`**: Main model training pipeline with comprehensive ML workflows
- **`EDA.ipynb`**: Extensive Exploratory Data Analysis (7.4MB of analysis)
- **`IT24100886_Impute_Cleaning_ChiSQR.ipynb`**: Data imputation, cleaning, and Chi-square analysis

**Future Development** (empty notebooks ready for development):
- **`05_final_preprocessing_and_train_test_split.ipynb`**: Final preprocessing and data splitting
- **`06_baseline_models.ipynb`**: Baseline model development
- **`07_hyperparameter_tuning.ipynb`**: Hyperparameter optimization
- **`08_model_evaluation.ipynb`**: Comprehensive model evaluation

### 📈 Model Training Process

1. **Data Collection**: Survey data processing and cleaning
2. **Feature Engineering**: Creating 20 key predictive features
3. **Model Training**: Multiple algorithms with hyperparameter optimization (Optuna)
4. **Calibration**: Probability calibration for reliable risk estimates
5. **Evaluation**: Comprehensive performance metrics and validation
6. **Explainability**: SHAP integration for model interpretability

### 🔬 Reproducing Research

To reproduce the complete research pipeline:

1. **Data Setup**: 
   - Download BRFSS data as specified in `datasetLocations.txt`
   - Place raw CSV files in `data/raw/` directory

2. **Data Processing** (run in sequence):
   - `01_data_merging_and_exploratory_analysis.ipynb`: Data merging and initial analysis
   - `02_feature_engineering.ipynb`: Feature engineering pipeline
   - `03_target_focused_dataset_preparation.ipynb`: Target preparation
   - `04_statistical_feature_selection.ipynb`: Feature selection

3. **Analysis & Training**:
   - `EDA.ipynb`: Comprehensive exploratory data analysis
   - `IT24100886_Impute_Cleaning_ChiSQR.ipynb`: Data cleaning and statistical analysis
   - `Diabetics_ModelTraining.ipynb`: Model training and evaluation

4. **Future Development**:
   - Complete remaining notebooks (05-08) for full ML pipeline
   - Export trained models to `models/` directory
   - Test with Streamlit application

## 🛡️ Ethical AI & Responsible Use

### 🎯 Purpose & Scope

- **Educational Tool**: Designed for learning and research purposes
- **Decision Support**: Aids healthcare professionals, not a replacement
- **Screening Only**: Not a diagnostic device or medical advice provider

### 🔒 Privacy & Security

- **Local Processing**: All computations performed on user's device
- **No Data Transmission**: Patient information never leaves local environment
- **No PII Required**: Uses anonymized health indicators only
- **Temporary Storage**: No persistent storage of patient data

### 🎨 Transparency Features

- **Model Explainability**: SHAP values explain each prediction
- **Performance Metrics**: Clear accuracy and reliability statistics
- **Feature Descriptions**: Plain-language explanations of all inputs
- **Probability Calibration**: Reliable risk probability estimates

### ⚠️ Important Disclaimers

- **Not Medical Advice**: Always consult healthcare professionals
- **Screening Tool Only**: Requires clinical confirmation (HbA1c, glucose tests)
- **Population Limitations**: Trained on specific survey data (BRFSS 2011-2015)
- **Individual Variation**: Results may not apply to all populations
- **Clinical Validation Required**: High-risk predictions need medical follow-up

## 🔧 Troubleshooting

### Common Issues

**📁 Model Loading Errors**
```
FileNotFoundError: Model file not found
```
- **Root Cause**: The `models/` directory is currently empty
- **Solution**: Train models using the provided notebooks first
- **Steps**: 
  1. Run the notebook pipeline starting with data processing
  2. Use `Diabetics_ModelTraining.ipynb` to train and save models
  3. Export trained models to `models/` directory
- **Alternative**: Update `app.py` to handle missing models gracefully

**📦 Import Errors**
```
ModuleNotFoundError: No module named 'streamlit'
```
- **Solution**: Install missing dependencies
- **Command**: `pip install streamlit pandas joblib scikit-learn xgboost`
- **Virtual Environment**: Ensure you're in the correct environment

**🧠 Memory Issues**
```
MemoryError: Unable to load model
```
- **Solution**: This may occur with large datasets during notebook execution
- **Alternative**: Process data in chunks or reduce dataset size for development
- **Note**: The `02_feature_engineering.ipynb` (3.2MB) and `EDA.ipynb` (7.4MB) notebooks contain extensive analysis that may require adequate RAM

**📊 SHAP Plotting Issues**
- **Solution**: Restart Streamlit if plots don't render
- **Command**: `Ctrl+C` then `streamlit run app.py`
- **Check**: Ensure `matplotlib` is properly installed

**🖥️ Windows PowerShell**
- **Activation**: Use `. .venv\Scripts\Activate.ps1` (note the dot-space)
- **Alternative**: Use VS Code Python environment selector
- **Permission**: May need to set execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## 🚀 Extending the Application

### 🔄 Adding New Models

1. **Train New Model**: Use the notebook pipeline to develop additional models
2. **Save Model**: Export as `.joblib` file to `models/` directory
3. **Update App**: Modify model loading section in `app.py` if needed
4. **Test Integration**: Verify model loading and prediction pipeline

### 🎯 Adding New Conditions

1. **Data Preparation**: Adapt preprocessing notebooks for new health conditions
2. **Feature Engineering**: Develop condition-specific features using `02_feature_engineering.ipynb` as template
3. **Model Training**: Train models using `Diabetics_ModelTraining.ipynb` framework
4. **UI Extension**: Create new input forms and result displays

### 📊 Enhanced Analytics

- **Statistical Analysis**: Leverage `04_statistical_feature_selection.ipynb` for feature analysis
- **Data Processing**: Use the comprehensive preprocessing pipeline in notebooks
- **Model Comparison**: Implement multiple model evaluation using existing framework
- **Research Extension**: Add new notebooks following the numbered sequence (09, 10, etc.)

### 🎨 Future UI Improvements

- **Mobile Responsiveness**: Optimize Streamlit app for tablet/phone usage
- **Advanced Visualizations**: Enhanced SHAP plots and interactive charts
- **Model Selection**: Allow users to choose between different trained models
- **Batch Processing**: Support for multiple patient assessments

## 👥 Contributing

### 🔀 Development Workflow

1. **Fork Repository**: Create your own copy
2. **Create Branch**: `git checkout -b feature/your-feature-name`
3. **Make Changes**: Implement improvements or fixes
4. **Test Locally**: 
   - For notebooks: Test in Jupyter environment
   - For app: Run `streamlit run app.py` (with trained models)
5. **Update Documentation**: Modify README if needed
6. **Submit PR**: Include description of changes

### 📜 Code Style Guidelines

- **Readable Functions**: Keep functions small and well-documented
- **Descriptive Naming**: Use clear variable and function names
- **Error Handling**: Implement proper exception handling
- **No Sensitive Data**: Never log or expose patient information
- **Comments**: Explain complex logic and model decisions
- **Notebook Standards**: Follow the existing numbered sequence and structure

### 💡 Areas for Contribution

- **Complete Pipeline**: Finish empty notebooks (05-08) to complete the ML pipeline
- **Model Improvements**: Better algorithms or feature engineering
- **UI/UX Enhancements**: Improved user experience for Streamlit app
- **Performance Optimization**: Faster data processing and model training
- **Documentation**: Better guides and examples
- **Testing**: Unit tests and validation scripts
- **Data Analysis**: Enhanced EDA and statistical analysis

## 📄 License & Acknowledgments

### 📋 License

This project is provided for **research and educational purposes**. For distribution or commercial use beyond educational scope, please add an appropriate LICENSE file (MIT/Apache-2.0) and ensure compliance with all third-party data source licenses.

### 🙏 Acknowledgments

- **Centers for Disease Control and Prevention (CDC)** - BRFSS dataset
- **Open Source Community** - Essential libraries and frameworks:
  - scikit-learn, XGBoost, CatBoost (Machine Learning)
  - pandas, numpy (Data Processing)
  - Streamlit (Web Framework)
  - SHAP (Model Explainability)
  - matplotlib, plotly (Visualization)
  - reportlab (PDF Generation)

### 📈 Data Source

**Behavioral Risk Factor Surveillance System (BRFSS)**
- **Source**: CDC National Health Survey
- **Years**: 2011-2015 (survey data)
- **Type**: De-identified population health data
- **Location**: See `datasetLocations.txt` for download instructions and data structure
- **Usage**: Educational and research purposes under CDC data use guidelines
- **Structure**: Raw data in `data/raw/`, processed data in `data/processed/`, train-test splits in `data/train-test/`

---

## 📞 Support & Contact

For questions, issues, or contributions:

- **Issues**: Create a GitHub issue for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Documentation**: Check this README and notebook comments
- **Medical Questions**: Always consult qualified healthcare professionals

**Remember**: This tool is for educational purposes only and should never replace professional medical advice or clinical testing.

---

*HealthIntel - Empowering informed health decisions through responsible AI* 🌱


