import pandas as pd
import re

print("Loading spam.csv...")
df = pd.read_csv('spam.csv', encoding='utf-8')
initial_len = len(df)

df.dropna(subset=['v1', 'v2'], inplace=True)

df.drop_duplicates(keep='first', inplace=True)

def is_valid(text):
    text = str(text)
    if len(text.strip()) == 0: return False
    if not re.search(r'[a-zA-Z0-9]', text): return False
    return True

df = df[df['v2'].apply(is_valid)]

df.to_csv('spam.csv', index=False, encoding='utf-8')

final_len = len(df)
print(f"Data cleaning complete.")
print(f"Original rows: {initial_len}")
print(f"Cleaned rows: {final_len}")
print(f"Removed {initial_len - final_len} garbage/duplicate rows.")
