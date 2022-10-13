from fastapi import FastAPI
import uvicorn as u

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "Working"}


if __name__ == '__main__':
    u.run(app, host="0.0.0.0", port=5000, debug=True)
