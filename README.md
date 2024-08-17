							 DocAssist - Intelligent Medical Decision Support System 

Introduction: 

DocAssist is an intelligent medical decision support system designed to assist healthcare providers in making informed decisions based on patient hematological data. The system predicts categorized hematological parameters and generates personalized treatment recommendations, leveraging advanced machine learning models and predefined clinical guidelines.

Project Purpose:
The primary goal of DocAssist is to provide accurate, data-driven insights and treatment recommendations to healthcare professionals, improving patient outcomes through personalized medical care.

Problem Statement:
Analyzing patient hematological data and providing personalized treatment recommendations can be complex and time-consuming. This project aims to streamline this process by using machine learning models to predict categorized hematological parameters and generate corresponding treatment recommendations.

Data Sources:
The dataset used in this project was sourced from an external file, specifically an Excel spreadsheet containing various hematological parameters, demographic details, and relevant medical data.

Methodology:
1. Data Collection and Preprocessing
Introduction: The dataset was collected and loaded into the Python environment using the pandas library.
Data Loading: Data was read from an Excel file located at a specified path.
Initial Data Overview: The dataset's structure and key features were examined to ensure readiness for analysis.
Data Structure: Key features include HAEMATOCRIT, HAEMOGLOBINS, ERYTHROCYTE, LEUCOCYTE, THROMBOCYTE, MCH, MCHC, MCV, AGE, SEX, and SOURCE.
2. Exploratory Data Analysis (EDA)
Introduction: EDA was conducted to understand the dataset and uncover patterns.
Data Preparation: Preprocessing included converting categorical variables to numerical formats.
Descriptive Statistics: Summary statistics such as mean, median, mode, and standard deviation were calculated.
Grouped Statistics: Data was grouped by sex and source to calculate aggregated statistics.
Outputs: The results of the EDA were saved as CSV files for further analysis.
3. Data Visualization
Introduction: Visualizations were created to explore the distributions and variability of blood parameters.
Visualization Techniques: Histograms with KDE plots and box plots were used to understand data distributions.
Outputs: Visualizations were saved as image files for future reference.
4. Model Development
Logistic Regression: Provided a strong baseline with good accuracy across most categories.
Random Forest: Identified as the best-performing model with an average accuracy of 97.30%.
Support Vector Machine (SVM): Explored but found less suitable due to lower accuracy in predicting certain categories.
5. Model Evaluation
Random Forest: The selected model for deployment due to its high accuracy and robustness in handling complex interactions.
Evaluation Metrics: Accuracy, precision, recall, and F1-scores were used to evaluate model performance.
Feature Importance: Analyzed to understand the most influential features in the model’s predictions.
6. Treatment Recommendations
Introduction: Treatment recommendations were generated based on the predicted categories using predefined clinical guidelines.
Technique: Each predicted category was matched to a set of treatment guidelines, including diagnosis, treatment options, follow-up schedules, and patient management considerations.
7. UI Development
Introduction: A Flask-based web application was developed to allow users to input data, receive predictions, and view treatment recommendations.
Key Features: Input form for hematological parameters, prediction display, and treatment recommendation output.
Outputs: The UI was designed to be intuitive and responsive, ensuring ease of use in clinical settings.


Setup Instructions: 
Prerequisites: Python 3.x
Required Python packages: pandas, numpy, scikit-learn, Flask, joblib, matplotlib

Installation: 
a. Clone the repository:
git clone https://github.com/Sneha3392/Python_DS.git

b. Navigate to the project directory:
cd docassist

c. Install the required packages:
pip install -r requirements.txt

d. Running the Project:
Data Preparation: Ensure that the dataset is located at C:/Users/akp24/docassist-main/data/processed/dataset_with_categorized_features.xlsx.
Model Training: If necessary, retrain the Random Forest model using the provided scripts.

e. Running the Flask Application:
python app.py

f. Access the application in your web browser at http://127.0.0.1:5000/.

Usage: 
1. Input the patient’s hematological parameters into the UI.
2. Click 'Submit' to receive predictions and corresponding treatment recommendations.

Additional Information:
Project Structure
data/: Contains the raw and processed datasets.
models/: Contains the trained Random Forest model.
notebooks/: Jupyter notebooks used for exploratory data analysis and model development.
static/: Static files for the web application (e.g., CSS, JavaScript).
templates/: HTML templates for the Flask application.
app.py: Main Flask application script.
requirements.txt: List of required Python packages