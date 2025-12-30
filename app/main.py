from fastapi import FastAPI, HTTPException
import uvicorn


app = FastAPI()


@app.get()