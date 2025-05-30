FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /

COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5000"]

# CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--host", "0.0.0.0", "--port", "5000"]


# CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "api:app", "--host", "0.0.0.0", "--port", "5000"]