import streamlit as st
import pandas as pd
import os
import io
import functions
import numpy as np
import regex as re

with st.sidebar:
    st.title("Procedures and Notes")
    st.subheader("App usage procedures:")
    st.write("1. Upload the txt file from the .zip file after exporting chat (You must pick *include media* when exporting the chat file)")
    st.write("2. Pick the Stock Opname start date and end date (to prevent older Stock Opname data to be extracted), and pick the appropriate WhatsApp language and time format.")

st.title("The Un-RECORDER App by Gz.")
st.write("Unrecord Data Processing Application, run in Streamlit")

dataRaw = st.file_uploader("Choose File .txt Export WA")
oldDate = st.date_input("Stock Opname Start Date:")
newDate = st.date_input("Stock Opname End Date:")

waLanguage = st.radio("WhatsApp Language:",["English", "Indonesian", "French"])
phoneTimeFormat = st.radio("Phone Time Format:", ["12h", "24h"], captions=["Example: 03:24 PM", "Example: 15:24"])

