FROM python:3.10.3-alpine

RUN mkdir /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
