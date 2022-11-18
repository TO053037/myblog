FROM --platform=linux/x86_64 python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

CMD gunicorn blog.wsgi:application --bind 0.0.0.0:8000