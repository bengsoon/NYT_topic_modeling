# Topic Modeling with The New York Times Headlines (Aug 2019 - Jul 2022)

This repository is a work done for a talk that I have prepared for on Topic Modeling (titled **What Can Machine Learning Do with Your Unstructured Data?**). 

The model used was [`BERTopic`](https://maartengr.github.io/BERTopic).The work covers how semantically similar documents (in this case, NYT headlines) tend to be closer together in a vector space. It also provides a general idea of [Dynamic Topic Modeling](https://maartengr.github.io/BERTopic/getting_started/topicsovertime/topicsovertime.html), where we delved into how the frequencies of the topics / themes evolve over time.

## Reproducibility
As there are limits to the large files storage on Github, I have decided to not push the model artifacts on this repo. However, you can reproduce it by cloning the repo onto your local drive (GPU-enabled machine required) or onto a GPU-enabled Google Colab instance:

``` bash
    git clone https://github.com/bengsoon/NYT_topic_modeling/
```

Within the cloned folder, create the conda environment:
``` bash
    conda create -f environment.yml
```

Run streamlit
``` bash
    cd app
    streamlit run app.py
```

## Viewing Results
I have created a Streamlit app that presents the results of the Topic Modeling. I am still on deploying the streamlit app on Streamlit server -- stay tuned!

