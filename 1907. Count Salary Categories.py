import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'category': ['High Salary','Low Salary', 'Average Salary'],
        'accounts_count' : [
            accounts[accounts.income > 50000].shape[0],
             accounts[accounts.income < 20000].shape[0],
             accounts[(accounts.income >=20000) &(accounts.income <=50000) ].shape[0],
            
        ],
    })
