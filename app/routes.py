

from fastapi import APIRouter 


router = APIRouter(
        prefix='/data',
        tags=['data'],
        )

@router.get('/')
def data_test():
    return {'message':'data test'}
