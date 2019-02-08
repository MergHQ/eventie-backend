import datetime
import uuid
from database import getDbConnection

def getUpcomingEvents():
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  cursor.execute('SELECT * FROM events where time >= now();')
  result = cursor.fetchall()
  return list(map(createEventObject, result))

def getPastEvents():
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  cursor.execute('SELECT * FROM events where time < now();')
  result = cursor.fetchall()
  return list(map(createEventObject, result))

def createEvent(event):
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  postData = validatePostBody(event)
  cursor.execute('INSERT INTO events values (%s,%s,%s,%s,%s,%s,%s)',
  postData)
  return postData

def validatePostBody(rawPostBody):
  return (str(uuid.uuid4()), rawPostBody['name'], rawPostBody['description'], rawPostBody['registration_start'], rawPostBody['registration_end'], rawPostBody['time'], rawPostBody['max_participants'])

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