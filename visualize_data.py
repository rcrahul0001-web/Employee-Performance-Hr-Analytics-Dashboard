import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:root@127.0.0.1:3306/employee_analytics"
)

# Load data from MySQL
query = "SELECT * FROM employees"
df = pd.read_sql(query, engine)

# Show first rows
print(df.head())

# -----------------------------
# 1. Attrition Count Chart
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="Attrition", data=df)

plt.title("Employee Attrition Count")
plt.show()

# -----------------------------
# 2. Department Wise Employees
# -----------------------------
plt.figure(figsize=(8,5))
sns.countplot(y="Department", data=df)

plt.title("Employees by Department")
plt.show()

# -----------------------------
# 3. Monthly Income Distribution
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["MonthlyIncome"], bins=20)

plt.title("Monthly Income Distribution")
plt.show()

# -----------------------------
# 4. Overtime vs Attrition
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="OverTime", hue="Attrition", data=df)

plt.title("Overtime vs Attrition")
plt.show()   