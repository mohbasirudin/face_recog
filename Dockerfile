FROM python:3.10-slim

WORKDIR /

COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt

CMD ["python", "app.py"]