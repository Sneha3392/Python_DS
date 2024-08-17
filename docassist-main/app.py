from flask import Flask, render_template, request
import joblib
import pandas as pd
import pickle
import logging
from ui.treatment_recommender import generate_treatment_recommendation  # Import the function

app = Flask(__name__)

# Set up logging for Flask
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),  # Log to 'app.log'
                        logging.StreamHandler()  # Also log to the console
                    ])

app.logger.info("Flask app logger set up")

# Load the trained model, treatment guidelines, and percentile thresholds
model_path = r'C:\Users\akp24\docassist-main\models\random_forest_model.pkl'
guidelines_path = r'C:\Users\akp24\docassist-main\models\treatment_guidelines.pkl'
thresholds_path = r'C:\Users\akp24\docassist-main\models\percentile_thresholds.pkl'

model = joblib.load(model_path)
with open(guidelines_path, 'rb') as f:
    treatment_guidelines = pickle.load(f)

with open(thresholds_path, 'rb') as f:
    percentile_thresholds = pickle.load(f)

# Define the age group bins and labels
age_bins = [0, 12, 35, 55, 75, 100]
age_labels = ['Infants and Young Children', 'Adolescents and Young Adults', 'Middle-aged Adults', 'Older Adults', 'Elderly']

def categorize_parameter(value, lower, upper):
    if value < lower:
        return 'Low'
    elif value > upper:
        return 'High'
    else:
        return 'Normal'

def preprocess_input(input_data):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Determine AGE_GROUP based on the AGE
    input_df['AGE_GROUP'] = pd.cut(input_df['AGE'], bins=age_bins, labels=age_labels, right=False)

    # Convert SEX to numerical values
    input_df['SEX'] = input_df['SEX'].map({'M': 1, 'F': 0})

    # Categorize the hematological parameters based on SEX and AGE_GROUP
    sex = 'M' if input_df['SEX'].iloc[0] == 1 else 'F'
    age_group = input_df['AGE_GROUP'].iloc[0]
    
    for param in percentile_thresholds[sex][age_group].keys():
        lower, upper = percentile_thresholds[sex][age_group][param]
        input_df[f'{param}_CATEGORY'] = input_df[param].apply(lambda x: categorize_parameter(x, lower, upper))

    # Drop unnecessary columns before prediction
    input_df = input_df.drop(columns=['AGE', 'AGE_GROUP'])

    # Ensure the DataFrame has all necessary columns and is in the correct order
    input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

    return input_df

@app.route('/')
def index():
    app.logger.info("Processing default request")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data
    input_data = {
        'SEX': request.form['SEX'],
        'AGE': int(request.form['AGE']),
        'HAEMATOCRIT': float(request.form['HAEMATOCRIT']),
        'HAEMOGLOBINS': float(request.form['HAEMOGLOBINS']),
        'ERYTHROCYTE': float(request.form['ERYTHROCYTE']),
        'LEUCOCYTE': float(request.form['LEUCOCYTE']),
        'THROMBOCYTE': float(request.form['THROMBOCYTE']),
        'MCH': float(request.form['MCH']),
        'MCHC': float(request.form['MCHC']),
        'MCV': float(request.form['MCV'])
    }

    # Preprocess the input
    input_processed_df = preprocess_input(input_data)

    # Predict categories
    predictions = model.predict(input_processed_df)[0]

    predictions_dict = {       
        'HAEMATOCRIT_CATEGORY': predictions[0],
    'HAEMOGLOBINS_CATEGORY': predictions[1],
    'ERYTHROCYTE_CATEGORY': predictions[2],
    'LEUCOCYTE_CATEGORY': predictions[3],
    'THROMBOCYTE_CATEGORY': predictions[4],
    'MCH_CATEGORY': predictions[5],
    'MCHC_CATEGORY': predictions[6],
    'MCV_CATEGORY': predictions[7]
    }

    app.logger.info(f"Processing predictions_dict: {predictions_dict}")

    # Generate treatment recommendations using the imported function
    recommendations = generate_treatment_recommendation(predictions_dict, treatment_guidelines)

    return render_template('index.html', predictions=predictions_dict, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
