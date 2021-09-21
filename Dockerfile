#dockerfile,image,container

FROM python:alpine3.14

WORKDIR /FLASKAPI-app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY ./app.py ./app.py

COPY ./templates ./templates


CMD ["python", "app.py"]
