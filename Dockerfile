FROM python:3.7-alpine
WORKDIR /app
ADD . /app
RUN python setup.py sdist
RUN pip install dist/*
