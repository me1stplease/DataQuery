def percentValid(res,df,percentColumnArray):
    res.write("\n\n---PERCENTAGE VALIDATION---\n\n")
    x = percentColumnArray.split(",")
    for i in x:
        column_name = df.columns[int(i.strip())]
        
        invalid_percent_rows = df[(df[column_name] < 0) | (df[column_name] > 100)]

        if not invalid_percent_rows.empty:
            res.write("Rows with percent values outside the range [0, 100] in column '{}':".format(column_name))
            res.write(str(invalid_percent_rows.index))
        else:
            res.write("No percent values found outside the range [0, 100] in column '{}'.".format(column_name))