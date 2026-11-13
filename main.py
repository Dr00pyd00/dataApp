
from fastapi import FastAPI

from app.routes import router 
from app.models import Data


app = FastAPI()
app.include_router(router)

@app.get('/')
def root():
    return {'message':'root'}


# test 
d = Data("un text")
d.id = 1

print(f'd = {d}')
print(f' to_dict = {d.to_dict()}')



