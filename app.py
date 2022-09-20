import pandas as pd

import streamlit as st
import streamlit.components.v1 as components


from PIL import Image
from pathlib import Path

from collections import Counter

import os

# Set the Browser Title
print(os.getcwd())
icon = Image.open(Path("./topic_modeling_logo.png"))
st.set_page_config(page_title=f"The New York Times Topic Modeling",page_icon=icon, layout="wide" )

# Company Logo & Main Header
logo = Image.open(Path("./topic_modeling_logo.png"))
st.image(logo, use_column_width='auto')
st.header("NYTimes Headlines Topic Extraction")

@st.cache
def read_data(file="./data/2021-6_2022-8_NYtimes_headlines.csv"):
    return pd.read_csv(file)


def insert_html(file_title, height=450, width=2000):
    html=open(f"./reports/{file_title}.html", 'r', encoding='utf-8')
    components.html(html.read(), height=height, width=width)

def get_text(file_title):
    txt = open(f"./reports/{file_title}.txt", 'r', encoding='utf-8').read()
    return txt.split("\n")


def pg_0_intro():
    st.markdown("#### 0. Introduction")
    st.write("-  According to MIT Sloan, it is estimated that [unstructured data make up to 80-90 percent of the world's data](https://mitsloan.mit.edu/ideas-made-to-matter/tapping-power-unstructured-data).")
    st.write("-  Unfortunately, unstructured data is not directly ingestible or searchable, unlike structured data, making it both humanly and technically challenging to interpret and consumed.")
    st.write("-  Topic modeling is one of the Natural Language Processing (NLP) tools in the machine learning arsenal that can help us to make sense out of the unstructured text data. It is used to discover the latent meaning (semantic) of texts, providing us 'topics' that represent them.")
    st.write("-  One of the most conventionally employed methods for topic modelling was Latent Dirichlet Allocation (LDA), which is statistical in nature.")
    st.write("-  However, for this site, we have employed a neural-based topic modeling called [BERTopic](https://maartengr.github.io/BERTopic/). It uses [Transformer-based (BERT) models](https://www.sbert.net/) to create vector embeddings that represent the sentences.")
    st.write("-  More will be written on the nitty-gritty details of how BERT-based topic modeling works in a separate post.")
    st.write("")

def pg_1_dataset():
    raw_data = read_data()
    st.markdown("#### 1.  The Dataset")
    st.write("- This dataset consists of New York Times _daily_ news headlines from **Aug 2019 until Jul 2022.**")
    st.write("- It was pulled directly from the NYT Developer API ([view source](https://github.com/bengsoon/NYT_topic_modeling/blob/main/00_nytimes_api.ipynb))")
    st.write("- There are **160,224 rows of headlines**.")
    st.write("- Below is the preview of the dataset:")
    st.dataframe(raw_data)

def pg_2_topic_modeling():
    st.markdown("#### 2. Topic Modeling / Extraction")
    st.write("- Topic modeling is a technique that automatically groups of **sentences/texts that are similar to each other** in meaning (semantics).")
    st.write("- Each of these groups represents a theme or a topic.")
    st.write("- Below is a visualization of the 160k rows of headlines with some examples of topics highlighted")
    # hdbscan_img = Image.open("img/hdbscan_example.png")
    # st.image(hdbscan_img, use_column_width='auto')
    st.write("")
    insert_html("visualize_documents_selected_reduced", 1000)

def pg_3_topics():
    info_df = read_data("./reports/frequency.csv").iloc[1:][["Topic", "Count", "Name"]]
    st.markdown("#### 3. Extracted Topics")
    st.write("- Below are the extracted topics / themes from the 160k rows of NYTimes's headlines:")
    st.dataframe(info_df)

def pg_4_interesting():

    st.markdown("#### 4. Interesting Topics")
    st.write("Below are some of the interesting topics that seem to provide a rather valuable insight to us about the news headlines trend in the past two years.")
    st.write("")

    st.markdown("##### 4.1 Masks and Covid")
    insert_html("masks")
    st.write("Example headlines:")
    for text in get_text("masks"):
        st.markdown("- " + text)
    st.write("")
    st.markdown("-----")
    st.write("**Insights:**")
    st.write("_We know that the Covid-19 pandemic only started towards the end of Dec 2019. But even so, the news report was initially slow to pick up in Jan 2020 and drastically spiked from Feb 2020 onwards._")
    st.markdown("-----")
    st.write("")
    st.write("")

    st.markdown("##### 4.2 Covid in India")
    insert_html("india_covid")
    st.write("Example headlines:")
    for text in get_text("india_covid"):
        st.markdown("- " + text)
    st.write("")
    st.markdown("-----")
    st.write("**Insights:**")
    st.write("_News about Covid in India did not seem extraordinary until it spiked in Mar-Jul 2021 when the country unfortunately faced tremendous Covid-19 crisis, along with news about vaccination in India._")
    st.markdown("-----")
    st.write("")
    st.write("")

    st.markdown("##### 4.3 Vaccines")
    insert_html("vaccine")
    st.write("Example headlines:")
    for text in get_text("vaccine"):
        st.markdown("- " + text)
    st.write("")
    st.markdown("-----")
    st.write("**Insights:**")
    st.write("_There had been some talks about vaccination from the outset of Covid-19 outbreak, but the news headline really peaked for vaccination in Q4 2021 when vaccines were rolled out._")
    st.markdown("-----")
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

    st.markdown("##### 4.5 Russia-Ukraine War headlines")
    insert_html("russian_ukraine")
    st.write("Example texts:")
    # st.markdown(get_text("russian_ukraine"))
    for text in get_text("russian_ukraine"):
        st.markdown("- " + text)
    st.write("")
    st.markdown("-----")
    st.write("**Insights:**")
    st.write("_There had already been some looming signs of the Russian-Ukrainian crisis in Nov 2021, although it peaked when the Russian invasion happened in February 2022._")
    st.markdown("-----")
    st.write("")
    st.write("")

    st.markdown("##### 4.6 Wildfires in California")
    insert_html("california_wildfires")
    st.write("Example headlines:")
    for text in get_text("california_wildfires"):
        st.markdown("- " + text)
    st.write("")
    st.markdown("-----")
    st.write("**Insights:**")
    st.write("_We can notice the seasonality of wildfires in California in the summertime._")
    st.markdown("-----")
    st.write("")
    st.write("")

    st.markdown("##### 4.7 Christmas from 2019-2022")
    insert_html("christmas")
    st.write("Example headlines:")
    for text in get_text("christmas"):
        st.markdown("- " + text)
    st.write("")
    st.markdown("-----")
    st.write("**Insights:**")
    st.write("_Again, there is also seasonality for Christmas headlines. However, what is also interesting is that the peak 'seasons' have seemed to move earlier in 2020-2021 (Aug 2020 and Jul 2021)._")
    st.markdown("-----")
    st.write("")
    st.write("")


if __name__ == "__main__":
    page_names_to_funcs = {
        "0. Introduction": pg_0_intro,
        "1. The Dataset": pg_1_dataset,
        "2. Topic Modeling Overview": pg_2_topic_modeling,
        "3. Topics Generated": pg_3_topics,
        "4. Interesting Topics": pg_4_interesting
    }

    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()