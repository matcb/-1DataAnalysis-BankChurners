import pandas as pd
import matplotlib.pyplot as plt
 
 # importing dataset
df = pd.read_csv("./dataset/BankChurners.csv")

# showing attrited customer and existing customer
# 8500 stayed and 1627 attrited
# 1627 / 10127 = 0,16 (16% have attrited)
churn_counts = df['Attrition_Flag'].value_counts()

# visualize Attrited Customers
churn_counts.plot(kind="bar", color=['green', 'red'])
plt.title("Customer Churn Overview")
plt.xlabel("Customer Status")
plt.ylabel("Number of Customers")
plt.xticks(rotation = 0)
plt.show()
print(churn_counts)


# group by gender and attrition flag to see churn distribution
gender_churn = df.groupby(["Gender", "Attrition_Flag"]).size().unstack()
gender_churn.plot(kind='bar', stacked=True, color=['red', 'green'])
plt.title("Churn by gender")
plt.ylabel("Number of customers")
plt.show()

print(gender_churn)