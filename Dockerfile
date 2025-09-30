FROM python:3.12-slim

WORKDIR /vpn-bot/

COPY requirements.txt . 

COPY ./common ./common

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

CMD ["python", "main.py"]