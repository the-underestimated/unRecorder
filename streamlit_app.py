import streamlit as st
import pandas as pd
import os
import io
import functions
import numpy as np
import xlsxwriter

with st.sidebar:
    st.title("Procedures and Notes")
    st.subheader("App usage procedures:")
    st.write("1. Upload the txt file from the .zip file after exporting chat (You must pick *include media* when exporting the chat file)")
    st.write("2. Pick the Stock Opname start date and end date (to prevent older Stock Opname data to be extracted), and pick the appropriate WhatsApp language and time format.")

st.title("The Un-RECORDER App by Gz.")
st.write("Unrecord Data Processing Application, run in Streamlit")

dataRaw = st.file_uploader("Choose File .txt Export WA")
oldDate = st.date_input("Stock Opname Start Date: (YYYY/MM/DD)", format='YYYY/MM/DD')
newDate = st.date_input("Stock Opname End Date: (YYYY/MM/DD)", format='YYYY/MM/DD')

waLanguage = st.radio("WhatsApp Language:",["English", "Indonesian", "French"])
phoneTimeFormat = st.radio("Phone Time Format:", ["24h", "12h"], captions=["Example: 15:24","Example: 03:24 PM"])

if dataRaw and oldDate and newDate and waLanguage and phoneTimeFormat:
    if st.button("Olah Data!", type="primary"):  
        try:
            readData = pd.read_fwf(dataRaw, encoding='utf-8')
            datePattern, dateTimeSenderPattern, dateStructure = functions.datePatternAndroid(phoneTimeFormat, waLanguage)
            processedData = functions.readRawData(readData, datePattern)
            cleanData = functions.dataProcessing(processedData, dateTimeSenderPattern, oldDate, newDate, dateStructure, phoneTimeFormat)

            
            output = io.BytesIO()

            with pd.ExcelWriter(output, date_format='m/d/yyyy', datetime_format='m/d/yyyy HH:MM:SS', engine='xlsxwriter') as writer:
                cleanData.to_excel(writer, sheet_name='Data Unrecord', index=True)
            
            output.seek(0)
            st.session_state['outputData'] = output

        except Exception as errorCode:
            st.error(f"Error: {errorCode}")

    if 'outputData' in st.session_state:
        st.download_button(
            label="Download Data Unrecord",
            data=st.session_state['outputData'],
            file_name="Data Unrecord.xlsx",
            mime="text/csv"
        )