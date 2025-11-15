FROM python:3.11-slim

ENV DISABLE_UVLOOP=1

RUN apt-get update && apt-get install -y --no-install-recommends\
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip uninstall -y uvloop || true

COPY . .

CMD ["python", "main.py"]