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
  cursor.execute("INSERT INTO events VALUES (%s,%s,%s,%s,%s,%s,%s);", postData)
  dbconn.commit()
  return createEventObject(postData)

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
    'max_participants': rawQueryData[6],
    'participants': getEventRegistrations(rawQueryData[0])
  }

def getEventRegistrations(eventId):
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  cursor.execute('SELECT users.id, users.username FROM registrations inner join users on (users.id = registrations.user_id) where event_id = %s;', (eventId,))
  result = cursor.fetchall()
  return list(map(createParticipantObject, result))

def createEventRegistration(eventId, userId):
  validation = validateRegistration(eventId, userId)
  if validation is False:
    return None
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  cursor.execute('INSERT INTO registrations VALUES (%s, %s);', (userId, eventId,))
  dbconn.commit()
  return eventId

def validateRegistration(eventId, userId):
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  cursor.execute('SELECT count(user_id) FROM registrations where event_id = %s and user_id = %s;', (eventId,userId,))
  result = cursor.fetchone()
  return True if result[0] == 0 else False

def createParticipantObject(rawObject):
  return {
    'user_id': rawObject[0],
    'username': rawObject[1]
  }