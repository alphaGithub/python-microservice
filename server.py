from fastapi import FastAPI
from config.config import Config
def createApp():
  Config.loadConfig()
  app = FastAPI()
  return app