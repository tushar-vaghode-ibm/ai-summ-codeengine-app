from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.foundation_models import Model
import json
import streamlit as st

# import vairables
import os
WATSONX_URL = os.environ.get('WATSONX_URL', 'https://us-south.ml.cloud.ibm.com')
WATSONX_APIKEY = os.environ.get('WATSONX_APIKEY')
WATSONX_LLM_ID = os.environ.get('DEFAULT_WATSONX_MODEL_ID', 'GRANITE_13B_CHAT_V2')
WATSONX_PROJECT_ID = os.environ.get('WATSONX_PROJECT_ID')

# Set page configuration
st.set_page_config(
  page_title="AI Summarization using serverless architecture in IBM Cloud",
  page_icon="🌐",
  layout="wide",
  initial_sidebar_state="expanded",
)

# Add a title and a subtitle
st.title("AI Summarization using serverless architecture in IBM Cloud")

# st.header("Input Section")
with st.form(key='myform'):
  input_value = st.text_area("Ask a question or enter your input text for summarization:", "What are key capabilities of IBM watsonx.ai?", height=50)
  submit_button = st.form_submit_button(label="Submit")

# setup watsonx.ai connection
my_credentials = {
    "url"    : WATSONX_URL,
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


# Define a function to process the input
def process_input(input_value):
  return model.generate_text(input_value)

# Display the output
# st.header("Output Section")
st.text_area("AI generated output:", process_input(input_value), height=400, disabled=True)
