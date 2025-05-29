FROM python:3.10-slim

WORKDIR /

COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt

CMD ["uvicorn", "api:app", "--host", "l0koc0kss0oso8ow0ckkccgw.df.weskonek.com.sslip.io", "--port", "8000", "--reload", "--reload-dir", "/"]