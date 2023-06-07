FROM python:3.8.10

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt

COPY staticfiles /home/app/uisalud_app/staticfiles
ENV TZ=America/Bogota

ADD . /app/
