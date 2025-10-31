import streamlit as st
import os
from transformers import pipeline
import boto3
import torch

bucket_name="mlops-30-102025"

local_path = "tinybert-sentiment-analysis"
s3_prefix = 'ml-model/tinybert-sentiment-analysis'

s3=boto3.client("s3", region_name='us-east-1')

def download_dir(local_path, s3_prefix):
    os.makedirs(local_path, exist_ok=True)
    paginator = s3.get_paginator('list_objects_v2')
    
    for result in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
        if 'Contents' in result:
            for key in result['Contents']:
                s3_key = key['Key'] #type: ignore

                # Build local path
                relative_path = os.path.relpath(s3_key, s3_prefix)
                local_file = os.path.join(local_path, relative_path)

                # ✅ Ensure parent folders exist
                os.makedirs(os.path.dirname(local_file), exist_ok=True)

                # print(f"⬇️ Downloading {s3_key} → {local_file}")
                s3.download_file(bucket_name, s3_key, local_file)

st.title("Machine learning model deployment on the server")
st.markdown("### _Sentiment Analysis using TinyBERT tranformer_:")

button = st.button("Download model")
st.text("Please click on Download button for using first time.")
if button:
    try:
        with st.spinner("Please wait....Downloading."):
            download_dir(local_path=local_path, s3_prefix=s3_prefix)
    except Exception as e:
        st.write('Facing problem for downloading model from AWS s3 server:', {e})
        st.warning("Sorry, Can't use this model without download.")

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')


text = st.text_area("Enter your review.")
predict = st.button("Predict")
classifier = pipeline('text-classification', model='tinybert-sentiment-analysiskk', device=device)

if predict:
    with st.spinner("Predicting...."):
        output=classifier(text)
        st.write(output)


