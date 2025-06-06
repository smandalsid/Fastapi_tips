import asyncio
import time

from fastapi import APIRouter, FastAPI

router = APIRouter()

@router.get("/terrible_ping")
async def first():
    time.sleep(10)
    return {"message":"first"}

# blocking task in async route will block the entire application, server thinks its a blocking task and not an I/O task and will wait before taking new requests

@router.get("/good_ping")
def second():
    time.sleep(10)
    return {"message":"second"}

# blocking task in sync route will be run in seperate thread by fastapi so that is okay, a side thread is blocked to finish the task and not the main thread

@router.get("/best_ping")
async def third():
    await asyncio.sleep(10)
    return {"message":"third"}

app = FastAPI()
app.include_router(router)

# best scenario where you await in the async route, the event loop selects next task from event queue and keeps working on them