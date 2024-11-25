FROM python:3.8-slim

WORKDIR /app

RUN mkdir -p /app/api_rest

RUN apt-get update && \
    apt-get install -y git wget && \
    apt-get install build-essential -y && \
    pip install --upgrade pip setuptools && \
    rm -rf /var/lib/apt/lists/*

COPY api_rest/requirements.txt /app/api_rest/requirements.txt

RUN pip install --trusted-host pypi.python.org -r /app/api_rest/requirements.txt

COPY api_rest /app/api_rest

EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "api_rest.main:rootapp"]