import pandas as pd

def rangeVal(res,df,col,start_range,end_range):
    res.write("\n\n---RANGE VALIDATION---\n\n")
    column_name = df.columns[int(col.strip())+1]
    res.write("Column '{}':\n".format(column_name))
    for index, row in df.iterrows():
        value = row[column_name]
        if value < start_range or value > end_range:
            res.write(f"Row {index}: {value}\n")
