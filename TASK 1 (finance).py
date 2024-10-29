import pandas as pd
import matplotlib.pyplot as plt

class PersonalFinanceTracker:
    def __init__(self):
        self.data = {
            'Income': [],
            'Expenses': [],
            'Category': []
        }

    def add_income(self):
        amount = float(input("Enter income amount: "))
        self.data['Income'].append(amount)
        print(f"Added income: {amount}")

    def add_expense(self):
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        self.data['Expenses'].append(amount)
        self.data['Category'].append(category)
        print(f"Added expense: {amount} in category: {category}")

    def generate_report(self):
        df = pd.DataFrame(self.data)
        total_income = sum(df['Income'])
        total_expenses = sum(df['Expenses'])
        balance = total_income - total_expenses
        
        print(f"\nTotal Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Balance: {balance}")

        # Visualization
        df.groupby('Category')['Expenses'].sum().plot(kind='bar', title='Expenses by Category')
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.show()

    def save_to_csv(self, filename='finance_data.csv'):
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

# Example usage
tracker = PersonalFinanceTracker()
while True:
    tracker.add_income()  # Allow user to add multiple incomes
    more_income = input("Do you want to add more income? (yes/no): ").lower()
    if more_income != 'yes':
        break

while True:
    tracker.add_expense()  # Allow user to add multiple expenses
    more_expense = input("Do you want to add more expenses? (yes/no): ").lower()
    if more_expense != 'yes':
        break

tracker.generate_report()
tracker.save_to_csv()
