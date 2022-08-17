import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
import streamlit.components.v1 as components


from PIL import Image
from pathlib import Path

import logging
import re

import json
from collections import Counter

# Set the Browser Title
icon = Image.open(Path("./img/topic_modeling_logo.png"))
st.set_page_config(page_title=f"The New York Times Topic Modeling",page_icon=icon, layout="wide" )

# Company Logo & Main Header
logo = Image.open(Path("./img/topic_modeling_logo.png"))
st.image(logo, use_column_width='auto')
# st.header("NYTimes Headlines Topic Extraction")

@st.cache
def read_data(file="../data/2021-6_2022-8_NYtimes_headlines.csv"):
    return pd.read_csv(file)


def insert_html(file_title, height=450, width=2000):
    html=open(f"../reports/{file_title}.html", 'r', encoding='utf-8')
    components.html(html.read(), height=height, width=width)

def get_text(file_title):
    txt = open(f"../reports/{file_title}.txt", 'r', encoding='utf-8').read()
    return txt.split("\n")


def pg_1_intro():
    raw_data = read_data()
    st.markdown("#### 1.  The Dataset")
    st.write("- This dataset consists of New York Times _daily_ news headlines from **Aug 2019 until Jul 2022.**")
    st.write("- There are **160,224 rows of headlines**.")
    st.write("- Below is the preview of the dataset:")
    st.dataframe(raw_data)

    st.markdown("#### 2. Topic Modeling / Extraction")
    st.write("- Topic modeling is a technique that automatically groups of **sentences/texts that are similar to each other** in meaning (semantics).")
    st.write("- Each of these groups represents a theme or a topic.")
    st.write("- Below is a visualization of the 160k rows of headlines with some examples of topics highlighted")
    # hdbscan_img = Image.open("img/hdbscan_example.png")
    # st.image(hdbscan_img, use_column_width='auto')
    st.write("")
    insert_html("visualize_documents_selected_reduced", 1000)

def pg_2_topics():
    info_df = read_data("../reports/frequency.csv").iloc[1:][["Topic", "Count", "Name"]]
    st.markdown("#### 3. Extracted Topics")
    st.write("- Below are the extracted topics / themes from the 160k rows of NYTimes's headlines:")
    st.dataframe(info_df)

    st.markdown("#### 4. Interesting Topics")
    st.write("")

    st.markdown("##### 4.1 Masks and Covid")
    insert_html("masks")
    st.write("Example headlines:")
    for text in get_text("masks"):
        st.markdown("- " + text)
    st.write("")
    st.write("")
    st.write("")

    st.markdown("##### 4.2 Covid in India")
    insert_html("india_covid")
    st.write("Example headlines:")
    for text in get_text("india_covid"):
        st.markdown("- " + text)
    st.write("")
    st.write("")
    st.write("")

    st.markdown("##### 4.3 Vaccines")
    insert_html("vaccine")
    st.write("Example headlines:")
    for text in get_text("vaccine"):
        st.markdown("- " + text)
    st.write("")
    st.write("")
    st.write("")

    st.markdown("##### 4.4 Omicron")
    insert_html("omicron")
    st.write("Example headlines:")
    for text in get_text("omicron"):
        st.markdown("- " + text)
    st.write("")
    st.write("")
    st.write("")

    st.markdown("##### 4.5 Russian-Ukraine War headlines")
    insert_html("russian_ukraine")
    st.write("Example texts:")
    # st.markdown(get_text("russian_ukraine"))
    for text in get_text("russian_ukraine"):
        st.markdown("- " + text)
    st.write("")
    st.write("")
    st.write("")

    st.markdown("##### 4.6 Wildfires in California")
    insert_html("california_wildfires")
    st.write("Example headlines:")
    for text in get_text("california_wildfires"):
        st.markdown("- " + text)
    st.write("")
    st.write("")
    st.write("")

    st.markdown("##### 4.7 Christmas from 2019-2022")
    insert_html("christmas")
    st.write("Example headlines:")
    for text in get_text("christmas"):
        st.markdown("- " + text)
    st.write("")
    st.write("")
    st.write("")


def pg_3_timeline():
    pass

if __name__ == "__main__":
    page_names_to_funcs = {
        "Introduction": pg_1_intro,
        "Topics Generated": pg_2_topics
    }

    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()