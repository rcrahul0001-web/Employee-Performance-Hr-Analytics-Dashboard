# 👥 Employee Performance & HR Analytics Dashboard

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

---

## 📌 Project Overview

This project delivers a comprehensive **HR Analytics solution** built on Python, MySQL, and Power BI. It analyzes employee performance, attrition patterns, salary trends, job satisfaction, and workforce distribution across departments — transforming raw HR data into **actionable business insights** through interactive, two-page Power BI dashboards.

---

## 🛠️ Tools & Technologies

| Category | Tools |
|---|---|
| Data Analysis | Python (Pandas, NumPy) |
| Visualization (EDA) | Matplotlib, Seaborn |
| Database | MySQL, SQLAlchemy |
| BI Dashboard | Power BI |
| Data Source | CSV Dataset |

---

## 📊 Project Workflow

```
HR Employee Dataset (CSV)
        ↓
Data Cleaning & Preprocessing (Python)
        ↓
Load into MySQL Database (SQLAlchemy)
        ↓
Exploratory Data Analysis (Python)
        ↓
Power BI Dashboard Development
        ↓
Business Insights & Recommendations
```

---

## 📈 Key Analysis Performed

### 🐍 Python — Exploratory Data Analysis
- Employee Attrition Count & Rate
- Employees by Department
- Monthly Income Distribution
- Overtime vs Attrition Analysis

### 📊 Power BI — Page 1: Employee Performance Dashboard
**KPI Cards:** Total Employees · Average Salary · Attrition Count · Average Experience

**Visuals:**
- Department-wise Employee Distribution
- Gender Distribution
- Salary by Job Role
- Experience Distribution
- Education Field Analysis

### 📊 Power BI — Page 2: Employee Performance Analysis
**KPI Cards:** Average Income · Overtime Employees · Avg Performance Rating · Job Satisfaction Score

**Visuals:**
- Performance by Department
- Salary vs Performance Rating
- Overtime Analysis
- Education vs Performance
- Job Role Performance Breakdown

---

## 🖼️ Dashboard Preview

| Page 1 — Employee Overview | 
|---|---|
| ![Dashboard Page 1]<img width="1432" height="796" alt="Screenshot 2026-06-18 140419" src="https://github.com/user-attachments/assets/34542429-075f-4e33-a86f-e77757e7a754" />
 
Page 2 — Performance Analysis |
) | ![Dashboard Page 2]<img width="1427" height="802" alt="Screenshot 2026-06-18 140451" src="https://github.com/user-attachments/assets/510283e9-129c-4bea-847e-b239f675dd2f" />
 


---

## 🔍 Key Insights

- 📌 **Research & Development** has the highest employee headcount across all departments.
- ⚠️ **Attrition rate is ~17%**, signaling a meaningful retention challenge for the organization.
- ⏱️ **Overtime employees exhibit higher attrition**, suggesting burnout may be a contributing factor.
- 💰 **Salary distribution is concentrated in lower-to-mid income ranges**, with limited high earners.
- 📊 **Performance ratings are relatively consistent across departments**, with no single outlier department.
- 😐 **Job satisfaction scores indicate room for improvement** in employee engagement initiatives.

---

## 📂 Project Structure

```
Employee-Performance-Dashboard/
│
├── Dataset/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── Python/
│   ├── clean_data.py          # Data cleaning & preprocessing
│   ├── load_data.py           # Load CSV into DataFrame
│   ├── insert_mysql.py        # Push cleaned data to MySQL via SQLAlchemy
│   └── visualize_data.py      # EDA charts with Matplotlib & Seaborn
│
├── PowerBI/
│   └── Employee Dashboard.pbix
│
├── Images/
│   ├── Dashboard_Page1.png
│   └── Dashboard_Page2.png
│
└── README.md
```

---

## 🚀 Skills Demonstrated

- ✅ Data Cleaning & Preprocessing
- ✅ SQL Database Management
- ✅ Exploratory Data Analysis (EDA)
- ✅ Data Visualization (Python + Power BI)
- ✅ Dashboard Development
- ✅ HR Analytics
- ✅ Business Intelligence
- ✅ Data Storytelling

---

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/rcrahul0001-web/Employee-Performance-Dashboard.git
   cd Employee-Performance-Dashboard
   ```

2. **Install Python dependencies**
   ```bash
   pip install pandas matplotlib seaborn sqlalchemy pymysql
   ```

3. **Configure MySQL connection** in `insert_mysql.py` (update host, user, password, db name)

4. **Run the pipeline in order**
   ```bash
   python Python/clean_data.py
   python Python/insert_mysql.py
   python Python/visualize_data.py
   ```

5. **Open the dashboard** — launch `PowerBI/Employee Dashboard.pbix` in Power BI Desktop

---

## 👨‍💻 Author

**Rahul Chauhan**
B.Sc. Data Science | Data Analyst

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rahul-chauhan-8b82012b1)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/rcrahul0001-web)

---

*If you found this project useful, consider giving it a ⭐ on GitHub!*
