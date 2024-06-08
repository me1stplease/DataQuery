import pandas as pd

def customQ(st,df,query):
    res=''
    try:
        # Execute the SQL query on the DataFrame
        result_df = eval(query)

        # Display the result DataFrame
        # st.write("Result Dataset:")
        # st.write(result_df)
        res=result_df
    except Exception as e:
        st.error(f"Error executing Panda's query: {e}")
    return res