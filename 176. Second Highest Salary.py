import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salary = employee['salary'].sort_values(ascending=False).drop_duplicates()
    return pd.DataFrame({
        'secondHighestSalary' :[None if salary.size<2 else salary.iloc[1]]
    })
