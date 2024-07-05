FROM docker.io/library/python:3.12.4

# File Author / Maintainer
MAINTAINER Tushar Vaghode <Tushar.Vaghode@ibm.com>
EXPOSE 8501

RUN \
    apt-get update && \
    pip install --upgrade pip && \
    pip install ibm-watsonx-ai && \
    pip install streamlit && \
    mkdir /codeengine

COPY app.py /codeengine/
COPY .streamlit /codeengine/

WORKDIR /codeengine
CMD streamlit run app.py
