FROM python:3.8.12-slim

WORKDIR /DB
COPY mockDB/ mockDB
RUN pip install -U pip
RUN pip install -r mockDB/requirements.txt

ENV PYTHONPATH=/DB/mockDB
CMD ["bash", "/DB/mockDB/build_mockingDB_container.sh"]
