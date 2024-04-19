def regexValid(res,df,regexArray):
    res.write("\n\n---PERCENTAGE VALIDATION---\n\n")
    x = regexArray.split("||")
    cols = len(df.axes[1])
    
    if len(x) != cols:
        res.write("Number of columns and regex didn't matched.")
        # print(len(x))
        # print(x)
        # print(cols)
    else:
        for i in range(cols):
            column_name = df.columns[i]
            regex_pattern = x[i].strip()
            # print(regex_pattern)

            if regex_pattern != '-':
                invalid_rows = df[~df[column_name].str.contains(regex_pattern, na=False)]

                if not invalid_rows.empty:
                    res.write("Rows with values not satisfying the regex pattern in column '{}':".format(column_name))
                    for index, row in invalid_rows.iterrows():
                        res.write("Row {}: {}".format(index, row[column_name]))
                else:
                    res.write("All values in column '{}' satisfy the regex pattern.".format(column_name))