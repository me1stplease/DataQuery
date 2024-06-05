import streamlit as st
import pandas as pd
from APICall import GeminiCall as GenAI
from countMatch import countCheck
from dateValidation import dateVal
from duplicateRecords import dupRecord
from mandatoryCheck import manCheck
from percentageValidation import percentValid
from regexVal import regexValid
from referanceVal import refValid
from rangeVal import rangeVal
from customQuery import customQ
from excelGen import template
from readExl import readIn


def analyze_file(df, command):
    try:
        # print("IN funct")
        # Read the file into a DataFrame using pandas
        # chunk = pd.read_csv(file_path, delimiter=delimiter, encoding='latin-1', chunksize=1000)
        # df=pd.concat(chunk)

        # Execute the user-provided command
        output = eval(command)
        # print("IN: "+str(output))

        # Display the command output
        st.text_area("Output", value=str(output), height=400)
    except Exception as e:
        st.error(f"Error: {e}")
        # st.write(f"Error: {e}")

def show_data_sample(df):
    try:
        # df = pd.read_csv(file_path, delimiter=delimiter, encoding='latin-1')
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error: {e}")
        # st.write(f"Error: {e}")

def main():
    st.title("File Analysis Tool")

    # File selection
    file_path = st.file_uploader("Upload File", type=["txt", "csv"], accept_multiple_files=False)

    if file_path is not None:
        
        # Delimiter selection
        delimiter = st.text_input("Delimiter Type", ",")

        # Show data sample button
        if delimiter:
            try:
                df = pd.read_csv(file_path, delimiter=delimiter, encoding='latin-1')
                column_names = df.columns.tolist()
                numerical_columns = df.select_dtypes(include=['number']).columns.tolist()
                # df=pd.concat(chunk)

                template(column_names)
                file_path = 'template.xlsx'

                # # Load the Excel file
                # df = load_excel(file_path)

                with open(file_path, 'rb') as f:
                    excel_data = f.read()

                # Download button
                st.download_button(
                    label='Download Excel file',
                    data=excel_data,
                    file_name='template.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )

                #generateTemplate
                # try:
                #     if template(column_names,st):
                #         # def load_excel(file_path):
                #         #     df = pd.read_excel(file_path, engine='openpyxl')
                #         #     return df
                        
                #         # Path to the Excel file
                #         file_path = 'template.xlsx'

                #         # # Load the Excel file
                #         # df = load_excel(file_path)

                #         with open(file_path, 'rb') as f:
                #             excel_data = f.read()

                #         # Download button
                #         st.download_button(
                #             label='Download Excel file',
                #             data=excel_data,
                #             file_name='template.xlsx',
                #             mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                #         )

                    # tempFile = open('template.xlsx', 'r')
                    # st.download_button('Download Input Template', tempFile) 
                    # tempFile.close()
                        # st.download_button(
                        #     label="Download Input Template",
                        #     data=buffer,
                        #     file_name="template.xlsx",
                        #     mime="application/vnd.ms-excel"
                        # )
                # except Exception as e:
                #     st.error(f"Error: {e}")

                if st.button("Show Data Sample"):
                    show_data_sample(df)
                    
                with st.expander("Early Tests"):

                    cnt = st.checkbox('Count Validation')
                    if cnt:
                        expectCount = st.text_input("Input the Expected Count") 

                    dt = st.checkbox('Date Column Validation')
                    if dt:
                        dateCol = st.text_input("Input the list of date type column numbers separeted with commas(',')")
                        
                    dup = st.checkbox('Duplicate record Validation')

                    mand = st.checkbox('Mandetory Field Validation')
                    if mand:
                        mandCol = st.text_input("Input the list of mandetory column numbers separeted with commas(',')") 

                    percent = st.checkbox('Percentage Column Validation')
                    if percent:
                        percentCol = st.text_input("Input the list of percentage column numbers separeted with commas(',')") 

                    regex = st.checkbox('RegEx Validation')
                    if regex:
                        regex_in_file_path = st.file_uploader("Upload regex input file", type=["xlsx"], accept_multiple_files=False)
                        if regex_in_file_path is not None:
                            try:
                                regexList = readIn(regex_in_file_path)   
                            except Exception as e:
                                st.error(f"Error: {e}")
                            #regexList = st.text_input("Input regex for the columns inplace of the their respective column name",value= '||'.join(map(str,column_names))) 

                    refer = st.checkbox('Referance Value Validation')
                    if refer:
                        refer_in_file_path = st.file_uploader("Upload referance input file", type=["xlsx"], accept_multiple_files=False)
                        if refer_in_file_path is not None:
                            try:
                                refList = readIn(refer_in_file_path)   
                            except Exception as e:
                                st.error(f"Error: {e}")
                            #refList = st.text_input("Input referance values seperatef with comas(',') inplace of the their respective column name",value= '||'.join(map(str,column_names))) 

                    ranVal = st.checkbox('Range Validation')
                    if ranVal:
                        ranCol = st.selectbox("Select the column number to be validated",numerical_columns)
                        ranS = st.text_input("Input the start of the range")
                        ranE = st.text_input("Input the end of the range") 

                    # resFile = open('result.txt', 'w')
                    if st.button("Generate Result"):
                        resFile = open('result.txt', 'w')
                        if cnt:
                            countCheck(resFile,df,expectCount)
                        if dt:
                            dateVal(resFile,df,dateCol)
                        if dup:
                            dupRecord(resFile,df)
                        if mand:
                            manCheck(resFile,df,mandCol)
                        if percent:
                            percentValid(resFile,df,percentCol)
                        if regex:
                            regexValid(resFile,df,regexList)
                        if refer:
                            refValid(resFile,df,refList)
                        if ranVal:
                            rangeVal(resFile,df,ranCol,ranS,ranE)

                        resFile.close()

                        resFile = open('result.txt', 'r')
                        st.download_button('Download Result', resFile) 
                        resFile.close()

                cusQ = st.text_input("Custom Panda's Query (consider data present in 'df')")

                # Analyze button
                if st.button("Generate Result",key='01'):
                    customQ(st,df,cusQ)

                    # resFile.close

                    # with open('result.txt','r+') as f:
                    #     st.download_button('Download Result', f) 


                # Command input
                user = st.text_input("User Input")

                # Analyze button
                if st.button("Analyze"):
                    command = GenAI(user)
                    command =command.replace("`", "").strip() 
                    # print("---")
                    # print(command)
                    analyze_file(df, command)

            except Exception as e:
                st.error(f"Error: {e}")
                # st.write(f"Error: {e}")

if __name__ == "__main__":
    main()
