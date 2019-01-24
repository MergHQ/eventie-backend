FROM nikolaik/python-nodejs:latest

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "./src/app.py"]