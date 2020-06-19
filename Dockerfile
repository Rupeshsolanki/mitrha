#dockerfile to run django 

FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
     & pip install Pillow

COPY . /code/
RUN pip install -r  requirements.txt

CMD ["python", "manage.py" ,"runserver" ,"0.0.0.0:8000"]


