from fastapi import FastAPI
from config import Config
from databases import Database
def createApp():

  Config.loadConfig()
  Database.initDB()
  app = FastAPI()
  return app