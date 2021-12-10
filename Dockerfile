FROM python:3.9.7-slim-buster
RUN mkdir /blog-api
WORKDIR /blog-api

COPY requirements.txt /blog-api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /blog-api/

CMD ["uvicorn","api.main:app","--host","0.0.0.0", "--port","8181","--reload"]