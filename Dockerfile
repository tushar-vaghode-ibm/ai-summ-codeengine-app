FROM docker.io/library/python:3.12.4

# File Author / Maintainer
MAINTAINER Tushar Vaghode <Tushar.Vaghode@ibm.com>
EXPOSE 8501

# Install required modules
RUN \
    apt-get update && \
    pip install --upgrade pip && \
    pip install ibm-watsonx-ai==1.0.10 && \
    pip install streamlit==1.36.0 && \
    mkdir /codeengine

# Copy code
COPY app.py /codeengine/app.py
COPY .streamlit /codeengine/.streamlit

# Run
WORKDIR /codeengine
CMD streamlit run app.py
