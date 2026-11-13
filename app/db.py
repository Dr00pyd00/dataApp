
from pathlib import Path
from pydoc import text
import sqlite3
from contextlib import contextmanager

from app.models import Data

FILENAME = 'data.db'
BASE_DIR = Path(__file__).resolve().parent.parent 
SQLITE_FILENAME = BASE_DIR / FILENAME 


class DataDatabaseSqlite3:
    '''
    DB object for Data + sqlite3.
    '''

    def __init__(self, filename: str|Path) -> None:
        self.filename: str|Path = filename 

    @contextmanager 
    def _connect(self):
        '''
        Personnal "with"
        '''
        conn = sqlite3.connect(self.filename) 
        try:
            yield conn
            conn.commit()
        except:
            conn.rollback()
            raise 
        finally:
            conn.close()
    
    def db_init(self) -> None:
        '''
        Create if not exists the table for datas.

        `Raises`: 
            - sqlite3.errors 
        '''
        with self._connect() as conn:
            cursor = conn.cursor() 
            cursor.execute("CREATE TABLE IF NOT EXISTS datas "
                           "(id INTEGER PRIMARY KEY AUTOINCREMENT,text TEXT,created_at TEXT )"
                           )
    
    def get_items(self) -> list[Data]|list:
        '''
        Get all items Data in the DB. 

        `Returns`:
            - List of [Data] or [] 

        `Raises`:
            - sqlite3.Errors for example
        '''
        with self._connect() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM datas")
            rows = cursor.fetchall()
            return [ Data.create_from_dict(dict(row)) for row in rows ]

    def add_item(self, data: Data) -> Data:
        '''
        take Data instance and add it in DB 

        `Args`:
            - data (Data) with id None

        `Returns`:
            - Data instance added with ID setup

        '''
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO datas (text, created_at) VALUES (?,?)",
                           (data.text, data.created_at.isoformat())
                           )
            data_id = cursor.lastrowid
        data.id = data_id
        return data 

    def get_item_by_id_or_none(self, data_id: int) -> Data|None:
        '''
        Try get Data instance by ID.

        `Args`:
            - data_id (int) : ID of item to find

        `Returns`:
            - None if nothing found
            - Data instance if found
        '''
        with self._connect() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM datas WHERE id = (?)", (data_id,))
            d_row = cursor.fetchone() 
            if d_row:
                return Data.create_from_dict(dict(d_row))
            return None


    def delete_item_by_id(self, data_id: int) ->bool:
        '''
        take Data.id and delete item from db.

        `Args`:
            - data_id (int) : the ID of Data to delete from db 
        `Returns`:
            - True if an item has been deleted else False
        '''
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM datas WHERE id=(?)", (data_id,))
            return cursor.rowcount > 0

    def update_item_text_by_id(self, data_id: int, new_text: str) -> Data|None:
        '''
        take Data.id and text for update item of DB.

        `Args`: 
            - data_id (int) : ID of item to update 
            - new_text (str) : text to replace item text 
        `Returns`:
            - Data instance updated 
            - None if instance disapered 
        `Raises`: 
            - Exception: if empty text 
        '''
        with self._connect() as conn:
            if new_text is None or new_text == '':
                raise Exception 
            cursor = conn.cursor()
            cursor.execute("UPDATE datas SET text = (?) WHERE id = (?)", (new_text, data_id))   

        return self.get_item_by_id_or_none(data_id)

        
            



            




