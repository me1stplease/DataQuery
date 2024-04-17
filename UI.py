import streamlit as st
import pandas as pd
from APICall import GeminiCall as GenAI
from countMatch import countCheck
from dateValidation import dateVal
from duplicateRecords import dupRecord
from mandatoryCheck import manCheck
from percentageValidation import percentValid

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
                # df=pd.concat(chunk)

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

                        resFile.close()

                        resFile = open('result.txt', 'r')
                        st.download_button('Download Result', resFile) 
                        resFile.close()

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
