FROM python:3.10-slim

WORKDIR /

COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y libgl1

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5000", "--reload", "--reload-dir", "/"]