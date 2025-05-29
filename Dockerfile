FROM python:3.10-slim

WORKDIR /

COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--reload-dir", "/"]