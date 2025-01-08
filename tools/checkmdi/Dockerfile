FROM python:3-slim-buster as builder

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY check_mdi.py /app/check_mdi.py

CMD ["sleep", "infinity"]