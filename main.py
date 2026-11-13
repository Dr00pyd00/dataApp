
from fastapi import FastAPI

from app.routes import router 

app = FastAPI()
app.include_router(router)

# test app:
@app.get('/')
def root():
    return {'message':'root'}




