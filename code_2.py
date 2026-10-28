import pandas as pd

df = pd.read_csv("employee.csv")


print(df)

print("\nEmployee Details:")
print(df[["Name", "Department", "Salary"]])


avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(avg_salary)
