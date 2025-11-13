from mongoengine import connect as MongoConnect
from core.errors import DatabaseError
import logging

class Database:
  @staticmethod
  def initDB():
    try:
      MongoConnect('hello')
    except Exception as e:
      logging.error('[err] initDb failed',e)
      raise DatabaseError('Failed to initialize database')