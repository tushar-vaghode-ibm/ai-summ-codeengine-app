FROM docker.io/library/python:3.9

# File Author / Maintainer
MAINTAINER Tushar Vaghode <Tushar.Vaghode@ibm.com>
EXPOSE 8501

RUN \
    apt-get update && \
    pip install --upgrade pip && \
    pip install streamlit && \
    mkdir /codeengine

COPY app.py /codeengine

WORKDIR /codeengine
CMD streamlit run app.py
