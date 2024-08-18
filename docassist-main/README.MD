## Please refer to the project document for detailed documentation of the steps
## Model Development Findings: Logistic Regression

During the development and evaluation of the Logistic Regression model, several key observations were made:

### Strengths:
- **High Accuracy for Majority Classes:** The model demonstrated high accuracy across most parameters, particularly for the 'normal' categories, which were well-predicted. This indicates the model's strength in handling the most common outcomes in the dataset.
- **Multi-Class Handling:** Logistic Regression handled the multi-class, multi-output nature of the problem reasonably well, giving a solid baseline performance.

### Weaknesses:
- **Lower Performance on Minority Classes:** The model showed reduced performance on less frequent categories (e.g., 'low' or 'high' ranges), as seen in the lower precision and recall for these classes. This suggests the need for additional techniques, such as class balancing or more sophisticated models.
- **Convergence Issues:** The model raised convergence warnings, indicating that it reached the maximum number of iterations before fully converging. This can be attributed to the complex nature of the dataset and the unscaled features.

### Recommendations:
- **Scaling Input Features:** Given the convergence issues, it's recommended to scale the input features using techniques like StandardScaler. Logistic Regression models often benefit from scaling, particularly when features have different ranges.
- **Increasing Iterations:** To address the convergence issues, increasing the `max_iter` parameter in the Logistic Regression model may be necessary, giving the model more iterations to fully converge.
- **Exploring Alternative Models:** Due to the observed weaknesses, especially in handling minority classes and convergence, exploring alternative models such as Random Forest or Support Vector Machines (SVM) is recommended. These models may offer better performance on this multi-class, multi-output problem and handle imbalanced data more effectively.

These findings will guide the next steps in model selection and refinement, ensuring that the final model is both accurate and robust across all categories.

### Random Forest Model Evaluation

**Overview:**
The Random Forest model demonstrated strong performance across all categories, with high accuracy and balanced precision, recall, and F1-scores. This model effectively handled the complexity of predicting medical categories, which involve interactions between various features.

**Model Performance:**

- **HAEMATOCRIT_CATEGORY:** 97.13% accuracy
- **HAEMOGLOBINS_CATEGORY:** 98.04% accuracy
- **ERYTHROCYTE_CATEGORY:** 95.31% accuracy
- **LEUCOCYTE_CATEGORY:** 97.28% accuracy
- **THROMBOCYTE_CATEGORY:** 96.68% accuracy
- **MCH_CATEGORY:** 98.19% accuracy
- **MCHC_CATEGORY:** 98.04% accuracy
- **MCV_CATEGORY:** 97.73% accuracy

**Strengths:**
- High accuracy and robust performance across all categories.
- Effective handling of complex interactions between features.
- Less prone to overfitting compared to simpler models.

**Weaknesses:**
- Slightly lower recall for some minority classes.
- Computationally intensive, which may impact deployment.

**Conclusion:**
Random Forest is a strong candidate for the final model due to its consistent and robust performance. Further tuning or comparison with other models like SVM may be necessary to finalize the best model for deployment.


## Model Evaluation: Support Vector Machine (SVM)
The Support Vector Machine (SVM) model was evaluated for predicting the categorized parameters based on the input data. The following observations were made:

### Strengths:
- The model performed reasonably well on the THROMBOCYTE_CATEGORY with an accuracy of 96.68%, demonstrating that SVM can effectively handle some categories.

### Weaknesses:
- For most categories, the model performed poorly, with several categories (e.g., HAEMATOCRIT_CATEGORY, HAEMOGLOBINS_CATEGORY, ERYTHROCYTE_CATEGORY) showing precision, recall, and F1-scores close to 0 for certain labels. This suggests that the model struggled to distinguish between the different classes.
- The warnings related to undefined metrics due to zero predictions for some classes indicate that the model is not suitable for imbalanced data or that it requires significant tuning.

### Conclusion:
Given the poor performance across most categories, SVM does not appear to be a suitable model for this multi-class, multi-output classification task. The model's inability to predict certain categories highlights the need for either tuning the hyperparameters or exploring alternative models. The next steps would involve considering different algorithms that might better capture the relationships in the data.

## Model Selection and Evaluation

### Overview
For this project, three models were evaluated to predict the categorical outcomes of hematological parameters. The models tested include:
- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)

### Model Evaluation Criteria
Each model was evaluated based on its accuracy across the following categories:
- HAEMATOCRIT_CATEGORY
- HAEMOGLOBINS_CATEGORY
- ERYTHROCYTE_CATEGORY
- LEUCOCYTE_CATEGORY
- THROMBOCYTE_CATEGORY
- MCH_CATEGORY
- MCHC_CATEGORY
- MCV_CATEGORY

### Results and Findings

1. **Logistic Regression**
   - Average Accuracy: 0.9534
   - Strengths: Provided stable accuracy across most categories.
   - Weaknesses: Struggled with certain categories, leading to lower precision and recall, especially for underrepresented classes.

2. **Random Forest** (Best Model)
   - Average Accuracy: 0.9730
   - Strengths: Achieved the highest accuracy across all categories. Particularly strong in predicting HAEMOGLOBINS_CATEGORY, MCH_CATEGORY, and MCHC_CATEGORY.
   - Weaknesses: Although very accurate, it might require more computational resources, which could be a limitation in real-time applications.

3. **Support Vector Machine (SVM)**
   - Average Accuracy: 0.9033
   - Strengths: Performed well in predicting THROMBOCYTE_CATEGORY.
   - Weaknesses: Generally lower accuracy and struggled with certain categories, leading to poor performance overall.

### Conclusion
The best model selected for this project is **Random Forest** with an average accuracy of 0.9730. This model demonstrated superior performance across all categories, making it the most suitable choice for predicting hematological parameters in this dataset. Future improvements may include further tuning of hyperparameters or exploring ensemble methods to potentially boost performance even further.
