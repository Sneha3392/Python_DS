
import logging

# Set up logging if it's not already configured
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

def generate_treatment_recommendation(predictions, guidelines):
    recommendation = {}
    logging.debug(f"Predictions received in generate_treatment_recommendation: {predictions}")
    logging.debug(f"Treatment guidelines: {guidelines}")
    for param, category in predictions.items():
        if param in guidelines and category in guidelines[param]:
            logging.debug(f"Successfully retrieved guideline: {guidelines[param][category]}")
            recommendation[param] = guidelines[param][category]
         
        else:
            logging.debug(f"Failed to retrieve guideline for {param} with category {category}")
            recommendation[param] = {
                'Diagnosis': 'No specific diagnosis found',
                'Treatment': 'No specific treatment guideline found',
                'Likelihood of Improvement': 'Unknown',
                'Risk Assessment': 'Unknown',
                'Key Factors': 'None',
                'Next Lab Test': 'None',
                'Follow-up Appointment': 'None',
                'Informed Consent': 'None',
                'Patient Compliance': 'None',
                'Side Effects': 'None'
            }
    return recommendation
