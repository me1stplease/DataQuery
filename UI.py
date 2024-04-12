import streamlit as st
import pandas as pd
from APICall import GeminiCall as GenAI

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
            
            if st.button("Read file"):
                try:
                    chunk = pd.read_csv(file_path, delimiter=delimiter, encoding='latin-1', chunksize=1000)
                    df=pd.concat(chunk)

                    if st.button("Show Data Sample"):
                        show_data_sample(df)
                    
                    with st.expander("See explanation"):

                        st.write("Early Test in one go")

                        if st.button("Generate Result"):
                            pass


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
