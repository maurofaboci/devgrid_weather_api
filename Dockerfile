FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl
COPY requirements.txt requirements.txt
COPY .env .env
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
