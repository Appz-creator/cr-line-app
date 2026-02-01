import streamlit as st
import pandas as pd
from datetime import datetime

# Load Excel file
file_path = "PM CR FEB2026.xlsx"
df = pd.read_excel(file_path)

# Convert date columns to datetime
df["Operation Start Time"] = pd.to_datetime(df["Operation Start Time"])
df["Operation End Time"] = pd.to_datetime(df["Operation End Time"])

# App title
st.title("CR & Line Lookup by Site ID")

# Input Site ID
site_id = st.text_input("Enter Site ID")

# Current date & time
now = datetime.now()

if site_id:
    result = df[
        (df["SITE ID"].str.upper() == site_id.upper()) &
        (df["Operation Start Time"] <= now) &
        (df["Operation End Time"] >= now)
    ]

    if not result.empty:
        st.success("Active CR found for today")
        st.table(result[["SITE ID", "CR", "LINE",
                         "Operation Start Time", "Operation End Time"]])
    else:
        st.warning("No active CR found for this Site ID on current date")
