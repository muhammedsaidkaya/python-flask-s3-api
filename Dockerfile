FROM python:alpine3.16

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5001
ENTRYPOINT python3 run.py