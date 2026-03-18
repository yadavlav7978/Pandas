# How to save data


import pandas as pd

data={
    "name":["Lav","Rahul"],
    "age":[20,21],
    "marks":[45,49]
}

df=pd.DataFrame(data)
print(df)

# Index=False means we don't want to save the index

# Save to CSV
df.to_csv("data.csv",index=False)

# Save to Excel
df.to_excel("data.xlsx",index=False)

# Save to JSON
df.to_json("data.json",index=False)