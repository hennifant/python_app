FROM python:3.8-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV FLASK_APP app.py
ENV FLASK_ENV development


COPY . /app

RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]

ENTRYPOINT ["sqlite3"]
