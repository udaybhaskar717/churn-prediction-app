## **Churn Prediction App**

### **1. Business Problem**
Customer churn is a critical concern for businesses, especially in subscription-based industries like telecommunications, banking, and SaaS platforms. Churn occurs when customers stop using a company’s products or services. Retaining existing customers is far more cost-effective than acquiring new ones.

#### **Objective**
The goal of this project is to predict customer churn based on customer behavior data. By identifying customers likely to churn, businesses can take proactive measures to retain them, such as offering discounts or personalized services.

---

### **2. Dataset**
- **Source** : (https://www.kaggle.com/datasets/blastchar/telco-customer-churn).
- **Number of features**: 19
- **Number of records**: 7043 X 21 .
- **Target Variable**: `Churn` (Binary: 1 for churned customers, 0 for retained customers).

---

### **3. Solution Approach**
The solution was developed as follows:

#### **Step 1: Exploratory Data Analysis (EDA)**
- Identified data imbalances between churned and non-churned customers.
- Visualized key features using histograms, boxplots, and correlation heatmaps.
- Preprocessed missing data and performed feature engineering.

#### **Step 2: Feature Engineering**
- Handled categorical variables via one-hot encoding.
- Standardized numerical features to improve model performance.
- Addressed data imbalance using **SMOTE** (Synthetic Minority Over-sampling Technique).

#### **Step 3: Model Development**
- Multiple machine learning models were evaluated, including:
  - Logistic Regression
  - Random Forest
  - XGBoost
  - AdaBoost (Selected Final Model)

#### **Step 4: Hyperparameter Tuning**
- Conducted hyperparameter optimization for AdaBoost using Grid Search.
- Best parameters:
  - `n_estimators`: 100
  - `learning_rate`: 0.1
  - `algorithm`: `SAMME.R`

---

### **4. Results**
#### **Model Evaluation Metrics**
| Metric          | Value       |
|------------------|-------------|
| Precision (Class 0) | 0.90   |
| Precision (Class 1) | 0.49   |
| Recall (Class 0)    | 0.70   |
| Recall (Class 1)    | 0.78   |
| Accuracy            | 72%    |
| ROC-AUC Score       | **0.83** |

#### **Confusion Matrix**
| Actual \ Predicted | 0   | 1   |
|--------------------|-----|-----|
| 0                  | 723 | 310 |
| 1                  | 82  | 292 |

---

#### **Key Insights**
1. The **ROC-AUC score of 0.83** demonstrates good discrimination ability.
2. While recall for churned customers (Class 1) is 78%, precision is 49%, indicating the need for targeted retention efforts.

#### **ROC Curve**
![ROC Curve](path-to-your-roc-curve.png)

---

### **5. Deployment**
The model was deployed as a Flask application with the following functionality:
- **Frontend**: A user-friendly web interface for inputting customer data and predicting churn.
- **Backend**: Flask API integrated with the trained AdaBoost model for inference.

#### **Steps to Run Locally**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/churn-prediction-app.git
   cd churn-prediction-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask application:
   ```bash
   python app.py
   ```

4. Open the app in your browser:
   - Navigate to `http://127.0.0.1:5000`.

#### **Docker Deployment**
1. Build the Docker image:
   ```bash
   docker build -t churn-prediction-app .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 churn-prediction-app
   ```

3. Access the app at `http://localhost:5000`.

---

### **6. Future Enhancements**
- **Improve Recall**: Experiment with ensemble models and advanced techniques like stacked models to improve precision for churned customers.
- **Feature Importance**: Perform SHAP analysis to understand key drivers of churn.
- **Scalability**: Deploy the application on AWS EC2 for production use.
- **Monitoring**: Implement MLFlow for logging model performance over time.

---

### **7. Repository Structure**
```
churn-prediction-app/
│
├── app.py                   # Flask backend
├── Dockerfile               # Docker configuration
├── requirements.txt         # Dependencies
├── static/                  # CSS and JavaScript files
├── templates/
│   └── index.html           # Frontend HTML file
├── model/                   # Trained model artifacts
└── README.md                # Project description
```

---

### **8. Conclusion**
This project successfully predicts customer churn with a focus on business impact. The results, along with the deployment process, showcase an end-to-end machine learning pipeline. This demonstrates the ability to transform raw data into actionable insights while building scalable, deployable systems.
