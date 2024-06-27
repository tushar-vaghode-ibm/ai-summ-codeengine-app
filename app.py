import streamlit as st

# Set page configuration
st.set_page_config(
  page_title="AI Summarization using serverless architecture in IBM Cloud",
  page_icon="🌐",
  layout="wide",
  initial_sidebar_state="expanded",
)

# Add a title and a subtitle
st.title("AI Summarization using serverless architecture in IBM Cloud")
st.markdown("""
This application takes an input from the user, processes it, and displays the output.
""")

# Define a function to process the input
def process_input(input_value):
  # Replace this with any processing you need
  return input_value.upper()


# Create a sidebar for input
with st.sidebar:
  option = st.selectbox(
    "Select LLM",
    ("granite", "llama")
  )

# st.header("Input Section")
with st.form(key='myform'):
  input_value = st.text_area("Enter your input here", height=50)
  submit_button = st.form_submit_button(label="Submit")

# Process the input
output_value = process_input(input_value)

# Display the output
# st.header("Output Section")
st.text_area("Processed Output", output_value, height=300, disabled=True)
