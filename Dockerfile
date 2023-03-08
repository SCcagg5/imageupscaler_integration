FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY api.py .

ENV UPSCALER_TOKEN=

CMD ["python", "api.py"]
