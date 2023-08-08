import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    rearranged_rows = []

    for _, row in products.iterrows():
        product_id = row['product_id']

        for store_col in ['store1', 'store2', 'store3']:
            price = row[store_col]
            if pd.notna(price):
                rearranged_rows.append((product_id,store_col, price))

    result =pd.DataFrame(rearranged_rows, columns=['product_id','store', 'price'])

    return result
