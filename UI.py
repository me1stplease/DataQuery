import streamlit as st
import pandas as pd
from APICall import GeminiCall as GenAI

def analyze_file(file_path, delimiter, command):
    try:
        # print("IN funct")
        # Read the file into a DataFrame using pandas
        df = pd.read_csv(file_path, delimiter=delimiter, encoding='latin-1')

        # Execute the user-provided command
        output = eval(command)
        # print("IN: "+str(output))

        # Display the command output
        st.text_area("Output", value=str(output), height=400)
    except Exception as e:
        st.error(f"Error: {e}")

def show_data_sample(file_path, delimiter):
    try:
        df = pd.read_csv(file_path, delimiter=delimiter, encoding='latin-1')
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error: {e}")

def main():
    st.title("File Analysis Tool")

    # File selection
    file_path = st.file_uploader("Upload File", type=["txt", "csv"], accept_multiple_files=False)

    if file_path is not None:
        # Delimiter selection
        delimiter = st.text_input("Delimiter Type", ",")

        # Show data sample button
        if delimiter:
            if st.button("Show Data Sample"):
                show_data_sample(file_path, delimiter)

        # Command input
        user = st.text_input("User Input")

        # Analyze button
        if st.button("Analyze"):
            command = GenAI(user)
            command =command.replace("`", "").strip() 
            # print("---")
            # print(command)
            analyze_file(file_path, delimiter, command)

if __name__ == "__main__":
    main()
