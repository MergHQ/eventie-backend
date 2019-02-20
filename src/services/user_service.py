import uuid
from database import getDbConnection
import bcrypt

def getUser(id):
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  cursor.execute('SELECT id, username, email, name FROM users where id = %s', (id,))
  result = cursor.fetchone()
  return createUserObject(result)

def createUser(user):
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  postData = validatePostBody(user)
  cursor.execute("INSERT INTO users VALUES (%s,%s,%s,%s,%s);", postData)
  dbconn.commit()
  return createUserObject(postData)

def validatePostBody(rawPostBody):
  salt = bcrypt.gensalt()
  hashed_pw = bcrypt.hashpw(rawPostBody['password'].encode('utf8'), salt)
  return (str(uuid.uuid4()), rawPostBody['username'], rawPostBody['email'], rawPostBody['name'], hashed_pw.decode('utf8'))

def createUserObject(rawQueryData):
  return {
    'id': rawQueryData[0],
    'username': rawQueryData[1],
    'email': rawQueryData[2],
    'name': rawQueryData[3],
  }