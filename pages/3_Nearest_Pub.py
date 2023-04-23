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

lat = st.number_input(label="Enter Latitude Here")
lon = st.number_input(label="Enter Longitude Here")
def euclidean_distance(lat1, lon1, lat2, lon2):
    return ((lat1-lat2)**2 + (lon1-lon2)**2)**0.5
df['distance'] = df.apply(lambda row: euclidean_distance(lat, lon, row['latitude'], row['longitude']), axis=1)
df_nearest = df.nsmallest(5, 'distance')
st.map(df_nearest)