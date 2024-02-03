FROM python:3.9

RUN mkdir /mysite

WORKDIR /mysite

ADD web /mysite

RUN pip install -r requirements.txt

CMD python3 manage.py runserver 0:8000