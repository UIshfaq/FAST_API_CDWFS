from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Umair !"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
