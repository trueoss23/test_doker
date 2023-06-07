import asyncio
import datetime
import uvicorn
import random
from fastapi import FastAPI

app = FastAPI()
db = {}
global counter
counter = 0


@app.get("/")
async def get_current_time():
    return {db}


async def send_current_time_count_random_int():
    global counter
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        counter += 1
        random_num = random.randint(1, 100)
        db['current_time'] = current_time
        db['counter'] = counter
        db['random_int'] = random_num
        print(db)
        await asyncio.sleep(5)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(send_current_time_count_random_int())


if __name__ == "__main__":
    uvicorn.run("main:app",
                host='127.0.0.1',
                port=8000,
                reload=True)
