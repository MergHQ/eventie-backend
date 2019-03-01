import datetime
import uuid
from services import user_service
from database import getDbConnection

def getUpcomingEvents():
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  cursor.execute('SELECT events.*, users.id as user_id, users.name as user_name FROM events left join users on (events.author_id = users.id) where time >= now();')
  result = cursor.fetchall()
  return list(map(createEventObject, result))

def getEvent(eventId):
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  cursor.execute('SELECT events.*, users.id as user_id, users.name as user_name FROM events left join users on (events.author_id = users.id) where events.id = %s', (eventId,))
  result = cursor.fetchone()
  return createEventObject(result)

def getPastEvents():
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  cursor.execute('SELECT events.*, users.id as user_id, users.name as user_name FROM events left join users on (events.author_id = users.id) where time >= now();')
  result = cursor.fetchall()
  return list(map(createEventObject, result))

def createEvent(event, userId):
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  postData = validatePostBody(event, userId)
  cursor.execute("INSERT INTO events VALUES (%s,%s,%s,%s,%s,%s,%s,%s);", postData)
  dbconn.commit()
  userres = user_service.getUser(userId)
  return createEventObject(postData + (userres['id'], userres['name'],), True)

def updateEvent(event, userId):
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  postData = validatePostBody(event, userId, True)
  cursor.execute("UPDATE events SET id  = %s, name = %s, description = %s, registration_start = %s, registration_end = %s, time = %s, max_participants = %s, author_id = %s where id = %s;", postData + (event['id'],))
  dbconn.commit()
  userres = user_service.getUser(userId)
  return createEventObject(postData + (userres['id'], userres['name'],), True)

def deleteEvent(eventId):
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  cursor.execute("DELETE FROM registrations WHERE event_id = %s", (eventId,))
  cursor.execute("DELETE FROM events WHERE id = %s", (eventId,))
  dbconn.commit()
  return {'id': eventId}

def validatePostBody(rawPostBody, userId, update=False):
  return (rawPostBody['id'] if update else str(uuid.uuid4()), rawPostBody['name'], rawPostBody['description'], rawPostBody['registrationStart' if update else 'registration_start'], rawPostBody['registrationEnd' if update else 'registration_end'], rawPostBody['time'], rawPostBody['maxParticipants' if update else 'max_participants'], userId,)

def createEventObject(rawQueryData, insert=False):
  return {
    'id': rawQueryData[0],
    'name': rawQueryData[1],
    'description': rawQueryData[2],
    'registration_start': rawQueryData[3],
    'registration_end': rawQueryData[4],
    'time': rawQueryData[5],
    'max_participants': rawQueryData[6],
    'author': {
      'id': rawQueryData[8],
      'name': rawQueryData[9]
    },
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