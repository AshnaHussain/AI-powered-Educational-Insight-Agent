import pandas as pd

def extract_text_from_csv(file):
    df = pd.read_csv(file)
    return df.to_string(index=False)
