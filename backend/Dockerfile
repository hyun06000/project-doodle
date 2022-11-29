FROM python:3.8.12-slim

WORKDIR /backend
COPY model/ model
RUN pip install -U pip
RUN pip install -r model/requirements.txt

ENV PYTHONPATH=/backend/model
