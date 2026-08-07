# 🛍️ RetailPulse: AI-Powered Customer Analytics & Demand Forecasting

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![Prophet](https://img.shields.io/badge/Prophet-Forecasting-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

</p>

---

# 📌 Overview

RetailPulse is an end-to-end AI-powered Retail Analytics platform developed using the **Online Retail II** dataset. The project transforms retail transaction data into interactive business intelligence dashboards, enabling data-driven decision-making through customer analytics, demand forecasting, churn prediction, inventory insights, and product performance analysis.

The application is built using **Python**, **Machine Learning**, **Streamlit**, and modern data visualization libraries to provide an intuitive analytics experience.

---

# 🎯 Problem Statement

Retail organizations generate massive volumes of transactional data every day. Extracting meaningful insights from this data is challenging due to:

- Large-scale customer transactions
- Changing customer purchasing behaviour
- Demand uncertainty
- Inventory optimization challenges
- Difficulty identifying high-value customers
- Lack of centralized business analytics

RetailPulse addresses these challenges by providing an intelligent analytics platform that converts raw retail data into actionable insights.

---

# 🚀 Key Features

- Interactive Streamlit Dashboard
- Executive Business Dashboard
- Sales Performance Analytics
- Customer Behaviour Analysis
- RFM Customer Segmentation
- Customer Churn Prediction
- Demand Forecasting
- Inventory Analytics
- Product Performance Analytics
- Country-wise Sales Analysis
- Business Insights Dashboard
- Interactive Charts & KPIs

---

# 📂 Dataset

**Dataset:** Online Retail II

**Source:** UCI Machine Learning Repository

The project uses the Online Retail II transactional dataset containing online retail sales data from a UK-based retailer. The dataset is used for customer analytics, segmentation, demand forecasting, inventory optimization, and business intelligence.

### Dataset Statistics

| Metric | Value |
|---------|------:|
| Records | **1,066,371** |
| Features | **8** |
| Customers | **5,942** |
| Products (Stock Codes) | **5,305** |
| Product Descriptions | **5,698** |
| Countries | **43** |

### Dataset Features

- Invoice
- StockCode
- Description
- Quantity
- InvoiceDate
- Price
- Customer ID
- Country

---

# 🛠 Tech Stack

## Programming Language

- Python

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Plotly
- Matplotlib
- Seaborn

## Machine Learning

- Scikit-learn
- Prophet

## Dashboard

- Streamlit

## Development Tools

- Git
- GitHub
- VS Code

---

# 🤖 Machine Learning Models

The project includes trained machine learning models for:

- Customer Churn Prediction (`churn_model.pkl`)
- Demand Forecasting using Prophet (`prophet_model.pkl`)

---

# 📊 Dashboard Modules

The Streamlit application consists of **11 interactive dashboards**.

## 🏠 Home

Project overview with KPI cards and quick navigation.

---

## 📈 Executive Dashboard

High-level business performance overview including revenue, orders, customers, and sales KPIs.

---

## 📊 Sales Analytics

- Revenue Trends
- Monthly Sales
- Sales Distribution
- Performance Metrics

---

## 👥 Customer Analytics

- Customer Behaviour
- Purchase Frequency
- Spending Analysis
- Customer KPIs

---

## 🎯 Customer Segmentation

- RFM Analysis
- Customer Segments
- Segment Distribution

---

## ⚠ Customer Churn

- Churn Prediction
- Customer Risk Analysis
- Retention Insights

---

## 📦 Inventory

- Inventory Status
- Product Availability
- Inventory KPIs

---

## 🌍 Country Analysis

- Country-wise Revenue
- Sales Distribution
- Geographic Insights

---

## 🛒 Product Analytics

- Product Performance
- Best Selling Products
- Revenue Contribution

---

## 📅 Demand Forecast

- Prophet Forecasting
- Future Sales Prediction
- Trend Visualization

---

## 💡 Business Insights

- Executive Recommendations
- Business KPIs
- Strategic Insights

---

# 📁 Project Structure

```text
RetailPulse/
│
├── 📂 app/
│   ├── 📂 .streamlit/
│   │   └── config.toml              # Streamlit configuration
│   │
│   ├── 📂 assets/
│   │   └── style.css                # Custom dashboard styling
│   │
│   ├── 📂 pages/                    # Dashboard pages
│   │
│   ├── 📂 utils/                    # Utility functions
│   │
│   └── app.py                       # Main Streamlit application
│
├── 📂 data/
│   ├── 📂 raw/                      # Original Online Retail II dataset
│   │   └── online_retail_II.xlsx
│   │
│   ├── 📂 processed/                # Processed datasets
│   │   ├── customer_churn_predictions.csv
│   │   ├── customer_features.csv
│   │   ├── customer_rfm.csv
│   │   ├── customer_segments.csv
│   │   ├── daily_sales.csv
│   │   ├── feature_importance.csv
│   │   ├── forecast.csv
│   │   ├── inventory_analysis.csv
│   │   ├── online_retail_II_cleaned.csv
│   │   └── online_retail_II_merged.csv
│   │
│   └── 📂 dashboard/                # Dashboard-ready datasets
│       ├── executive_overview.csv
│       ├── sales_analytics.csv
│       ├── customer_analytics.csv
│       ├── customer_segmentation.csv
│       ├── customer_churn.csv
│       ├── inventory_dashboard.csv
│       ├── country_analytics.csv
│       ├── product_analytics.csv
│       ├── demand_forecasting.csv
│       ├── business_insights.csv
│       └── project_summary.csv
│
├── 📂 models/
│   ├── churn_model.pkl              # Customer Churn Prediction Model
│   └── prophet_model.pkl            # Demand Forecasting Model
│
├── 📂 notebooks/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_Exploratory_Data_Analysis.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   ├── 05_Customer_Segmentation.ipynb
│   ├── 06_Demand_Forecasting.ipynb
│   ├── 07_Customer_Feature_Engineering.ipynb
│   ├── 08_Customer_Churn_Prediction.ipynb
│   ├── 09_Inventory_Optimization.ipynb
│   └── 10_Dashboard_Dataset_Preparation.ipynb
│
├── 📂 images/
│   └── dashboards/                  # Dashboard images
│
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── LICENSE                          # MIT License
└── .gitignore
```

---

# 📈 Project Workflow

```text
01_Data_Understanding
            │
            ▼
02_Data_Cleaning
            │
            ▼
03_Exploratory_Data_Analysis
            │
            ▼
04_Feature_Engineering
            │
            ▼
05_Customer_Segmentation
            │
            ▼
06_Demand_Forecasting
            │
            ▼
07_Customer_Feature_Engineering
            │
            ▼
08_Customer_Churn_Prediction
            │
            ▼
09_Inventory_Optimization
            │
            ▼
10_Dashboard_Dataset_Preparation
            │
            ▼
Interactive Streamlit Dashboard
```

---

# 📷 Dashboard Screenshots

## 🏠 Home

![Home](screenshots/dashboards/home.png)

---

## 📈 Executive Dashboard

![Executive Dashboard](screenshots/dashboards/executive_dashboard.png)

---

## 📊 Sales Analytics

![Sales Analytics](screenshots/dashboards/sales_analytics.png)

---

## 👥 Customer Analytics

![Customer Analytics](screenshots/dashboards/customer_analytics.png)

---

## 🎯 Customer Segmentation

![Customer Segmentation](screenshots/dashboards/customer_segmentation.png)

---

## ⚠ Customer Churn

![Customer Churn](screenshots/dashboards/customer_churn.png)

---

## 📦 Inventory

![Inventory](screenshots/dashboards/inventory.png)

---

## 🌍 Country Analysis

![Country Analysis](screenshots/dashboards/country_analysis.png)

---

## 🛒 Product Analytics

![Product Analytics](screenshots/dashboards/product_analytics.png)

---

## 📅 Demand Forecast

![Demand Forecast](screenshots/dashboards/demand_forecast.png)

---

## 💡 Business Insights

![Business Insights](screenshots/dashboards/business_insights.png)

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/pinkey-kavar-bika/RetailPulse.git
```

Navigate to the project directory:

```bash
cd RetailPulse
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app/app.py
```

---

# 🚀 Live Demo

The application is deployed on Streamlit Community Cloud.

**Live URL:**

```
<YOUR_STREAMLIT_URL>
```

---

# 📌 Future Improvements

- Real-time data pipeline
- Automated model retraining
- Enhanced forecasting models
- Role-based authentication
- Dashboard export functionality
- Advanced business recommendations

---

# 👥 Contributors

- Nasrin Khatoon
- Pinkey Kavar Bika
- Sheikh Moin
- RetailPulse Development Team

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
