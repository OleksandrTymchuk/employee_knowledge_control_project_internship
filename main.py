import databases
import uvicorn as u
from fastapi import FastAPI
from config import settings
from fastapi.middleware.cors import CORSMiddleware

db = databases.Database(settings.DATABASE_URL)
app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "Working"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://0.0.0.0:5000',
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# @app.on_event("startup")
# def startup():
#     init_db()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
#     await app.state.redis.close()


if __name__ == '__main__':
    u.run(app, host="0.0.0.0", port=5000, debug=True)