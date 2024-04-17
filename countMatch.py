def countCheck(res,df,expected:int):
    res.write("---COUNT VALIDATION---\n")
    total_records = df.shape[0]
    res.writelines(["Expected Count : ",str(expected),'\n'])
    res.writelines(["Actual Count : ",str(total_records),'\n'])
    if total_records==expected:
        res.write("MATCHED\n")
    else:
        res.write("NOT MATCHED\n")