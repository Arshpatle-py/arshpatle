import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("employee.csv")

print("Employee Details:")
print(df[["Name", "Department", "Salary"]])

avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(avg_salary)

avg_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()
