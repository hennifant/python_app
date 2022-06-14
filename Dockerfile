FROM python:3.10.5
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
ENV FLASK_APP app.py
ENV FLASK_ENV development
COPY . app/
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

