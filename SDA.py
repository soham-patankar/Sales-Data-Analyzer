import pandas as pd

df = pd.read_csv('sales.csv')

df = df.drop_duplicates()

df = df[df['Name'].notna()]

df['Category'] = df['Amount'].apply(lambda x: 'High' if x > 1000 else 'Low')

df['Priority'] = df.apply(
    lambda x: 'VIP' if (x['Amount'] > 1000) & (x['Country'] == 'USA') else 'Normal',
    axis=1
)

df = df[df['Amount'] > 500]

df.to_csv('final_report.csv', index=False)

print("Report generated successfully!")