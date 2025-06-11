import pandas as pd
from io import BytesIO

def parse_csv(file_bytes):
    df = pd.read_csv(BytesIO(file_bytes))
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df.sort_values('timestamp')
