import streamlit as st
from matplotlib import image
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "image")
DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs.csv")
imgg= os.path.join(IMAGE_PATH, "welcome.jpg")


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
st.title("Home")

img = image.imread(imgg)
st.image(img)

st.dataframe(df)
st.title("describe")
st.write(df.describe())
st.title("Plot :")
col = ['fsa_id', 'easting', 'northing', 'latitude', 'longitude']
selected_column = st.selectbox('Select a column to plot:', col)
if selected_column in ['fsa_id', 'easting', 'northing']:
    fig, ax = plt.subplots()
    ax.hist(df[selected_column], bins=20)
    ax.set_title(f'Histogram of the {selected_column} column')
    ax.set_xlabel(selected_column)
    ax.set_ylabel('Count')
    st.pyplot(fig)
else:
    fig, ax = plt.subplots()
    ax.scatter(df['longitude'], df['latitude'], alpha=0.5)
    ax.set_title('Scatter plot of the longitude vs. latitude columns')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    st.pyplot(fig)

