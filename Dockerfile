FROM python:3.4
ENV PYTHONUNBUFFERED
ADD . /code/
WORKDIR /code/ 
RUN pip install -r requirements.txt