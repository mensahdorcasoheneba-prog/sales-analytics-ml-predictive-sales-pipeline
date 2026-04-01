# sales-analytics-ml-predictive-sales-pipeline
Automated sales data processing and predictive modeling pipeline using Python. Features anomaly detection, volatility analysis, and a Logistic Regression model with 98% classification accuracy

# Global Sales Data Analytics & Predictive Modeling

This repository contains a data science pipeline designed to process large-scale sales datasets and perform predictive classification. Using **Python**, **Pandas**, and **Scikit-Learn**, the project automates data cleaning, performs financial volatility analysis, and identifies transaction types (Purchase vs. Refund) with high precision.

## 🚀 Project Overview

The project is divided into two main modules:
1.  **Data Processing & ETL:** Automates the cleaning of raw sales data, handles anomalies, and generates time-series visualizations.
2.  **Predictive Analytics:** Implements a Machine Learning model to classify transactions based on purchasing patterns.

---

## 📊 Model Performance

The predictive engine utilizes a **Logistic Regression** model trained on features including `Quantity` and `Unit_Price`. 

* **Classification Accuracy:** **98%**
* **Target Variable:** `Transaction_Type` (Purchase / Refund)
* **Library Stack:** Scikit-Learn, NumPy, Pandas

---

## 📂 Repository Structure

### 1. `data_processing.py`
This script contains the `SalesDataProcessor` class. It is responsible for:
* **Anomaly Detection:** Filtering out unrealistic price points (e.g., Unit Price > $10,000).
* **Data Imputation:** Automatically filling missing `Payment_Method` values with "Unknown".
* **Feature Engineering:** Creating the `Total_Amount` and `Transaction_Type` columns.
* **Trend Visualization:** Generating a monthly revenue report saved as `sales_trend.png`.

### 2. `predictive_model.py`
This script focuses on the Machine Learning pipeline:
* **Preprocessing:** Converting transaction quantities to absolute values for model training.
* **Train/Test Split:** Using an 80/20 split to ensure model generalizability.
* **Inference:** Includes an example usage section to test new, unseen transactions against the trained model.

---

## 🛠️ Installation & Usage

### Prerequisites
Ensure you have Python installed, then install the required dependencies:
```bash
pip install pandas numpy matplotlib scikit-learn
```

### Running the Scripts
1.  Place your `GLOBAL SALES DATA.csv` in the appropriate directory: `C:\Users\USER\Desktop\sales_data\`.
2.  Run the processing script to clean data and see trends:
    ```bash
    python data_processing.py
    ```
3.  Run the predictive model to see the accuracy score and test predictions:
    ```bash
    python predictive_model.py
    ```

---

## 📈 Visualizations
The pipeline automatically generates a **Monthly Sales Revenue Trend** graph. This allows stakeholders to identify seasonal growth and volatility across different product categories at a glance.

> **Note:** If running these scripts on a different machine, please update the file path strings in both `.py` files to match your local CSV location.

---

### ## Contact
For any questions regarding the logic or implementation of this pipeline, feel free to reach out via GitHub.
