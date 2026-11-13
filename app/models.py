
from datetime import datetime
from typing import Self 


class Data:
    '''
    Simple Data object contain:
        - `id` (int) : pk
        - `text` (str) : the data itself 
        - `created_at` (datetime) : date of creation
        ---
    Methods:
        - `to_dict`: return a dict contain all Data fields 
        - `create_from_dict` {args=dict} : take a dict a create Data instance 
            
    '''

    def __init__(self, text: str) -> None:
        self.id: int | None = None 
        self.text: str = text 
        self.created_at: datetime = datetime.now()

    def __str__(self) -> str:
        return f'id:{self.id} | text: {self.text} | cat: {self.created_at}'

    def to_dict(self) -> dict:
        return {
                'id': self.id,
                'text': self.text,
                'created_at': self.created_at.isoformat(),
                }

    @classmethod
    def create_from_dict(cls, data_dict: dict) -> Self | None:
        d_text = data_dict.get('text')
        d_id = data_dict.get('id')
        d_created_at = data_dict.get('created_at')
        if d_text is None or d_id is None or d_created_at is None:
            return None 
        d = cls(d_text) 
        d.id = d_id 
        d.created_at = datetime.fromisoformat(data_dict['created_at'])
        return d
            
