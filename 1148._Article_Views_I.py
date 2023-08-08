import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    authors_view = views[views['author_id'] == views['viewer_id']]
    unique_author = authors_view['author_id'].unique()
    unique_author = sorted(unique_author)
    result_df = pd.DataFrame({'id': unique_author})

    return result_df
