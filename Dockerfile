FROM python:3.8.10

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD uis_salud_app/ /app/

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000