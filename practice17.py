# # pandas questions----
# Pandas Practice Questions with Answers
# Q1. What is Pandas?

# Answer:
# Pandas is an open-source Python library used for data analysis and data manipulation. It provides powerful data structures like Series and DataFrame.

# import pandas as pd
# Q2. What is a Series?

# Answer:
# A Series is a one-dimensional labeled array that can store any data type.

# import pandas as pd

# s = pd.Series([10, 20, 30, 40])
# print(s)

# Output

# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64
# Q3. What is a DataFrame?

# Answer:
# A DataFrame is a two-dimensional table with rows and columns.

# import pandas as pd

# data = {
#     "Name": ["Aman", "Riya"],
#     "Age": [20, 21]
# }

# df = pd.DataFrame(data)
# print(df)

# Output

#    Name  Age
# 0  Aman   20
# 1  Riya   21
# Q4. How do you read a CSV file?

# Answer

# import pandas as pd

# df = pd.read_csv("students.csv")
# print(df)
# Q5. How do you display the first 5 rows?

# Answer

# df.head()