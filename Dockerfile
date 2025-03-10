FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y wait-for-it

COPY . /app/

EXPOSE 8000

CMD python manage.py makemigrations