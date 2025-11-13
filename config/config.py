import logging
import os
from core.errors import ValidationError
from dotenv import load_dotenv


load_dotenv()


CONFIG_KEYS = ['SERVICE_NAME','PORT']
class Config:
  SERVICE_NAME=None
  PORT=None

  @staticmethod
  def initConfig():
    Config.SERVICE_NAME = os.getenv('SERVICE_NAME')
    Config.PORT = int(os.getenv('PORT'))

  @staticmethod
  def validateLoadConfig():
    for i in range(len(CONFIG_KEYS)):
      key = CONFIG_KEYS[i]
      if os.getenv(key) is None:
        return False
    Config.initConfig()
    return True

  @staticmethod
  def loadConfig():
    print(" ->",Config.validateLoadConfig(),type(Config.SERVICE_NAME),type(Config.PORT))
    if not Config.validateLoadConfig():
      raise ValidationError(message='Config Load failed')