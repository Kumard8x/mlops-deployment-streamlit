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

button = st.button("Download model")
if button:
    with st.spinner("Please wait....Downloading."):
        download_dir(local_path=local_path, s3_prefix=s3_prefix)

text = st.text_area("Enter your review.", "Typing....")
predict = st.button("Predict")

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
classifier = pipeline('text-classification', model='tinybert-sentiment-analysis', device=device)

if predict:
    with st.spinner("Predicting...."):
        output=classifier(text)
        st.write(output)


