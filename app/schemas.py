
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DataClientDisplaySchema(BaseModel):
    '''
    Contains:
        - `id`: int 
        - `text`: str 
        - `created_at`: datetime
    '''
    # enable to read Obj OR dict:
    model_config = ConfigDict(from_attributes=True) 

    id: int
    text: str 
    created_at: datetime

class DataClientCreationInputSchema(BaseModel):
    '''
    Contains:
        - `text`: str
    '''
    text: str

