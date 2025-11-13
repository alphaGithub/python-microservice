import logging
from core.errors import InternalError
from fastapi import APIRouter


eventsRouter = APIRouter(prefix="/events",tag=["events"])
@eventsRouter.get("/")
async def getEvents(req):
  try:
    return {}
  except Exception as e:
    logging.error("[err] >>>>> [getEvents] fetch error!",e)
    raise InternalError('getEvents: failed to fetch')

