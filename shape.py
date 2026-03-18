import pandas as pd

data={
    "names":["Lav","Rahul","Mohit","Aarav","Kiran"],
    "age":[20,21,22,23,24],
    "marks":[45,49,48,47,46]
}
df=pd.DataFrame(data)

print(df)

print(df.shape)   # it return (rows,columns)
print(df.columns) # it return column names

