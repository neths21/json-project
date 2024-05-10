import pandas as pd
import streamlit as st
import os

def convert_json_to_excel(file, excel_file_path):
    df = pd.read_json(file)
    if os.path.exists(excel_file_path):
        df.to_excel(excel_file_path, index=False, mode='a', header=False)
    else:
        df.to_excel(excel_file_path, index=False)
    return excel_file_path

def main():
    st.title("JSON to Excel Converter")

    # File upload
    uploaded_file = st.file_uploader("Upload JSON file", type=["json"])

    if uploaded_file is not None:
        # Display file path
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)
        # Ask for output Excel file path
        excel_file_path = st.text_input("Enter output Excel file path ")

        # Convert and download
        if st.button("Convert JSON to Excel"):
            if not excel_file_path:
                st.error("Please enter output Excel file path.")
            else:
                excel_file_path = convert_json_to_excel(uploaded_file, excel_file_path)
                st.success("JSON file converted to Excel successfully!")
                # st.write(f"[Download Excel file](/{excel_file_path})")
                st.write(f"Downloaded Excel file at: {excel_file_path}")

if __name__ == "__main__":
    main()
