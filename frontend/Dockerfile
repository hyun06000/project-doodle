FROM python:3.8.12-slim

WORKDIR /frontend
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY app/ app
ENV PYTHONPATH=/frontend/app
CMD ["uvicorn", "main:app", "--reload"]
