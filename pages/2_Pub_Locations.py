import streamlit as st
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs.csv")

def dataset():
    df = pd.read_csv(DATA_PATH)
    df.columns=['fsa_id',  'name', 'address', 'postcode', 'easting','northing',  'latitude', 'longitude',  'local_authority']
    df['easting'] = pd.to_numeric(df['easting'], errors='coerce')
    df['northing'] = pd.to_numeric(df['northing'], errors='coerce')
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    df['fsa_id'] = df['fsa_id'].astype(int)
    df['name'] = df['name'].astype(str)
    df['address'] = df['address'].astype(str)
    df['postcode'] = df['postcode'].astype(str)
    df['easting'] = df['easting'].astype(int)
    df['northing'] = df['northing'].astype(int)
    df['latitude'] = df['latitude'].astype(float)
    df['longitude'] = df['longitude'].astype(float)
    df['local_authority'] = df['local_authority'].astype(str)
    return df

df= dataset()   
df['latitude'].fillna(df['latitude'].mean(), inplace=True) # Replace null values with the mean value of the column
df['longitude'].fillna(df['longitude'].mean(), inplace=True)
df['latitude'] = df['latitude'].apply(lambda x: float(x))
df['longitude'] = df['longitude'].apply(lambda x: float(x))
df['latitude'] = df['latitude'].astype(float)
df['longitude'] = df['longitude'].astype(float)
local_authorities = sorted(set(df['local_authority']))
selected_authority = st.selectbox("Select a local authority", local_authorities)
filtered_df = df[df['local_authority'] == selected_authority]
st.text(f"Total number of pubs in {selected_authority}: {len(filtered_df)}")
st.map(filtered_df)