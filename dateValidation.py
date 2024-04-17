import pandas as pd

def dateVal(res,df,dateColumnArray):
    res.write("\n\n---DATE VALIDATION---\n\n")
    x = dateColumnArray.split(",")
    for i in x:
        column_name = df.columns[int(i.strip())]
        original_column = df[column_name].copy()
        res.writelines([column_name," : \n"])
        df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
        invalid_dates = df[df[column_name].isnull()]
        if len(invalid_dates) > 0:
            for index in invalid_dates.iterrows():
                # print("Row {}: {}".format(index, row[column_name]))
                res.writelines([str(index)," - ",str(original_column[index]),'\n'])
        else:
            res.writelines(["VALID DATES",'\n'])
    
