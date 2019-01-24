import psycopg2
import os

# Database connection params
name = os.environ['DB_NAME']
host = os.environ['DB_HOST']
user = os.environ['DB_USER']
passw = os.environ['DB_PASSWORD']
port = os.environ['DB_PORT']

conn = psycopg2.connect(dbname=name, user=user, host=host, password=passw, port=port)

def getDbConnection():
  return conn