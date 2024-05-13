import pandas as pd

def rangeVal(res,df,column_name,start_range,end_range):
    res.write("\n\n---RANGE VALIDATION---\n\n")
    
    res.write("Column '{}':\n".format(column_name))
    for index, row in df.iterrows():
        value = row[column_name]
        if value < start_range or value > end_range:
            res.write(f"Row {index}: {value}\n")
