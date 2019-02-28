import jwt
from database import getDbConnection
import bcrypt
import os

def loginUser(username, password):
  dbconn = getDbConnection()
  cursor = dbconn.cursor()
  cursor.execute('SELECT id, username, password_salt FROM users where username = %s;', (username,))
  id, username, password_salt = cursor.fetchone()
  if id is None:
    return None
  if bcrypt.checkpw(password.encode('utf8'), password_salt.encode('utf8')):
    token = jwt.encode({'user_id': id}, os.environ['JWT_SECRET'], algorithm='HS256')
    return {'access_token': token.decode('utf8')}
  else:
    return None


  
  