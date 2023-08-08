import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(
        total_time=employees['out_time'] - employees['in_time'],
        day = employees['event_day'].dt.strftime('%Y-%m-%d'),
        ).groupby(
            ['emp_id','day'], as_index =False

        )['total_time'].sum()[
            ['day','emp_id','total_time']
        ]
