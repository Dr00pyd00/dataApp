

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.db import DataDatabaseSqlite3
from app.schemas import DataClientDisplaySchema, DataClientCreationInputSchema
from app.dependencies import get_db 
from app.models import Data


router = APIRouter(
        prefix='/data',
        tags=['data'],
        )

@router.get('/test')
def data_test():
    return {'message':'data test'}


@router.get('/', response_model=List[DataClientDisplaySchema])
def get_all_data(db: DataDatabaseSqlite3 = Depends(get_db)):
    try:
        datas = db.get_items()
    except:
        return {'error':'get_all failed'}
    return datas 


@router.get('/{data_id}', response_model=DataClientDisplaySchema|Any)
def get_data_by_id(
        data_id: int, 
        db: DataDatabaseSqlite3 = Depends(get_db)
        ):
    data = db.get_item_by_id_or_none(data_id)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='item not found')    
    return data 


@router.post('/', response_model=DataClientDisplaySchema)
def add_item(
        payload: DataClientCreationInputSchema, 
        db: DataDatabaseSqlite3 = Depends(get_db)
        ):
    data = Data(payload.text) 
    return db.add_item(data) 


@router.put('/{data_id}', response_model=DataClientDisplaySchema ) 
def update_item(
        data_id:int, 
        payload: DataClientCreationInputSchema, 
        db: DataDatabaseSqlite3 = Depends(get_db)
        ):
    try:
        updated_data = db.update_item_text_by_id(data_id, payload.text)
    except:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='payload text can\'t be empty')
    return updated_data 


@router.delete('/{data_id}', status_code=status.HTTP_204_NO_CONTENT ) 
def delete_item(
        data_id:int, 
        db: DataDatabaseSqlite3 = Depends(get_db)
        ):
        
        deleted = db.delete_item_by_id(data_id)
        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='item not found')










