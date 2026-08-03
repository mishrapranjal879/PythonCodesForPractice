# Pandas Practice Questions with Solutions
# Q1. Create a Pandas Series

# Question: Create a Series containing the values [10, 20, 30, 40, 50].

# Solution
# import pandas as pd

# s = pd.Series([10, 20, 30, 40, 50])
# print(s)


# Q2. Display DataFrame information
# Solution
# print(df.info())      # Data types
# print(df.shape)       # Rows and Columns
# print(df.dtypes)      # Data Types
# print(df.isnull().sum())  # Missing Values


# Q3. Rename columns
# Solution
# df.rename(columns={
#     "Name": "Student_Name",
#     "Age": "Student_Age"
# }, inplace=True)

# print(df)


# Q4. GroupBy Example
# Solution
# import pandas as pd

# data = {
#     "Department": ["IT", "HR", "IT", "HR"],
#     "Salary": [50000, 40000, 60000, 45000]
# }

# df = pd.DataFrame(data)

# print(df.groupby("Department")["Salary"].mean())


# Q5. Merge DataFrames
# Solution
# students = pd.DataFrame({
#     "ID":[1,2,3],
#     "Name":["Ram","Shyam","Mohan"]
# })

# marks = pd.DataFrame({
#     "ID":[1,2,3],
#     "Marks":[90,85,95]
# })

# result = pd.merge(students, marks, on="ID")

# print(result)