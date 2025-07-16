FROM python:3.13.5-alpine3.22

WORKDIR /app

COPY ["main.py", "requirements.txt", "./"]

RUN pip install -r requirements.txt

EXPOSE 5000/tcp

ENTRYPOINT ["python", "main.py"]
