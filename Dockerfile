FROM python:latest

WORKDIR /usr/src/app

RUN pip install flask

COPY . .

CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0"]
