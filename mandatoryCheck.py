def manCheck(res,df,mandatoryColumnArray):
    res.write("\n\n---MANDATORY CHECK---\n\n")
    x = mandatoryColumnArray.split(",")
    for i in x:
        column_name = df.columns[int(i.strip())]
        null_or_blank_rows = df[df[column_name].isnull() | (df[column_name] == '')]

        if not null_or_blank_rows.empty:
            res.write("Rows with null or blank values in column '{}':".format(column_name))
            res.write(str(null_or_blank_rows.index))
        else:
            res.write("No null or blank values found in column '{}'.".format(column_name))