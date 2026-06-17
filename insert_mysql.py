import pandas as pd
from sqlalchemy import create_engine

# Load cleaned dataset
df = pd.read_csv(
    r"C:\Users\Admin\Documents\employee\cleaned_employee_data.csv"
)

# Connect to MySQL
engine = create_engine(
 "mysql+pymysql://root:root@127.0.0.1:3306/employee_analytics"
)

# Insert data into MySQL
df.to_sql(
    name="employees",
    con=engine,
    if_exists="replace",
    index=False
)
5
print("Data inserted successfully!")