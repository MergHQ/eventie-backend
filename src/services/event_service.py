import datetime
from database import getDbConnection

def getAllEvents():
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  cursor.execute('SELECT * FROM events;')
  result = cursor.fetchmany()
  return list(map(createEventObject, result))

def createEventObject(rawQueryData):
  return {
    'id': rawQueryData[0],
    'name': rawQueryData[1],
    'description': rawQueryData[2],
    'registration_start': rawQueryData[3],
    'registration_end': rawQueryData[4],
    'time': rawQueryData[5],
    'max_participants': rawQueryData[6]
  }