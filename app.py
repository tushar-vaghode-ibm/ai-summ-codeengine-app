from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.foundation_models import Model
import json
import streamlit as st

st.set_page_config(
  page_title="AI Summarization using serverless architecture"
)

st.header("AI summarization using serverless architecture in IBM Cloud")
prompt = st.chat_input("Ask something")

# import vairables
import os
WATSONX_URL = os.environ.get('WATSONX_URL', 'https://us-south.ml.cloud.ibm.com')
WATSONX_APIKEY = os.environ.get('WATSONX_APIKEY')
WATSONX_LLM_ID = os.environ.get('DEFAULT_WATSONX_MODEL_ID', 'GRANITE_13B_CHAT_V2')
WATSONX_PROJECT_ID = os.environ.get('WATSONX_PROJECT_ID')

# setup watsonx.ai connection
def model_init():
  my_credentials = {
    "url" : WATSONX_URL,
    "apikey" : WATSONX_APIKEY
  }
  llm_model   = getattr(ModelTypes, WATSONX_LLM_ID)
  project_id  = WATSONX_PROJECT_ID
  space_id    = None
  verify      = False
  parameters  = {
    "decoding_method": "greedy",
    "max_new_tokens": 2000,
    "min_new_tokens": 100,
    "repetition_penalty": 1
  }
  model = Model(llm_model, my_credentials, parameters, project_id, space_id, verify)
  return model

# output section
output = ""
if prompt:
  model = model_init()
  output = model.generate_text(prompt)

st.html("<h4 style='color: gray'>AI generated output:</h4>")
with st.container(border=True, height=500):
  st.write(output)
