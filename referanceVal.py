def refValid(res,df,refArray):
    res.write("\n\n---REFERANCE VALIDATION---\n\n")
    x = refArray.split("||")
    print(x)

    cols = len(df.axes[1])
    
    if len(x) != cols:
        res.write("Number of columns and reference values didn't matched.")
        # print(len(x))
        # print(x)
        # print(cols)
    else:
        for i in range(cols):
            column_name = df.columns[i]
            temp = set(x[i].split(","))
            refVal = temp-set(['-','',column_name,' '])

            column_values = set(df[column_name].unique())

            if len(refVal)>0:
                not_present_in_column = refVal - column_values

                extra_values_in_column = column_values - refVal

                if len(not_present_in_column)>0 or len(extra_values_in_column)>0:
                    res.write("Column '{}':\n".format(column_name))
                    if len(not_present_in_column)>0:
                        res.write("Values not present in the column: '{}'.\n".format(not_present_in_column))
                    if len(extra_values_in_column)>0:
                        res.write("Extra values present in the column: '{}'.\n".format(extra_values_in_column))
