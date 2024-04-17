import pandas as pd

def dupRecord(res,df):
    res.write("\n\n---DUPLICATE RECORD---\n\n")
    duplicate_rows = df[df.duplicated()]

    if not duplicate_rows.empty:
        # print("Duplicate records found:")
        # print(duplicate_rows)
        res.writelines(str(duplicate_rows))
    else:
        res.write("No duplicate records found.")
    