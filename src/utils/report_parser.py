import pandas as pd
from io import StringIO


def parse_csv_text_to_df(text: str):
    try:
        df = pd.read_csv(StringIO(text))

        # 🔑 Normalize column names
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return df

    except Exception as e:
        return None
